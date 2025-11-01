<template>
  <div class="fixed top-0 left-0 w-full h-full z-0 pointer-events-none transition-colors duration-500" :style="{ background: bgColor }">
    <canvas ref="canvasRef" class="dither-container" />
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, computed } from 'vue'
import { useDark } from '@vueuse/core'
import * as THREE from 'three'
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer'
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass'
import { ShaderPass } from 'three/examples/jsm/postprocessing/ShaderPass'

const props = defineProps({
  waveSpeed: {
    type: Number,
    default: 0.05
  },
  waveFrequency: {
    type: Number,
    default: 3
  },
  waveAmplitude: {
    type: Number,
    default: 0.3
  },
  colorNum: {
    type: Number,
    default: 4
  },
  pixelSize: {
    type: Number,
    default: 2
  },
  disableAnimation: {
    type: Boolean,
    default: false
  },
  enableMouseInteraction: {
    type: Boolean,
    default: true
  },
  mouseRadius: {
    type: Number,
    default: 0.3
  }
})

const isDark = useDark()
const canvasRef = ref(null)
const mousePos = ref(new THREE.Vector2(0, 0))

const bgColor = computed(() => isDark.value ? '#000000' : '#ffffff')
const waveColor = computed(() => isDark.value ? [0.3, 0.3, 0.3] : [0.7, 0.7, 0.7])

let renderer = null
let scene = null
let camera = null
let composer = null
let mesh = null
let animationId = null

const waveVertexShader = `
varying vec2 vUv;
void main() {
  vUv = uv;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
`

const waveFragmentShader = `
precision highp float;
uniform vec2 resolution;
uniform float time;
uniform float waveSpeed;
uniform float waveFrequency;
uniform float waveAmplitude;
uniform vec3 waveColor;
uniform vec2 mousePos;
uniform int enableMouseInteraction;
uniform float mouseRadius;
varying vec2 vUv;

vec4 mod289(vec4 x) {
  return x - floor(x * (1.0/289.0)) * 289.0;
}

vec4 permute(vec4 x) {
  return mod289(((x * 34.0) + 1.0) * x);
}

vec4 taylorInvSqrt(vec4 r) {
  return 1.79284291400159 - 0.85373472095314 * r;
}

vec2 fade(vec2 t) {
  return t*t*t*(t*(t*6.0-15.0)+10.0);
}

float cnoise(vec2 P) {
  vec4 Pi = floor(P.xyxy) + vec4(0.0,0.0,1.0,1.0);
  vec4 Pf = fract(P.xyxy) - vec4(0.0,0.0,1.0,1.0);
  Pi = mod289(Pi);
  vec4 ix = Pi.xzxz;
  vec4 iy = Pi.yyww;
  vec4 fx = Pf.xzxz;
  vec4 fy = Pf.yyww;
  vec4 i = permute(permute(ix) + iy);
  vec4 gx = fract(i * (1.0/41.0)) * 2.0 - 1.0;
  vec4 gy = abs(gx) - 0.5;
  vec4 tx = floor(gx + 0.5);
  gx = gx - tx;
  vec2 g00 = vec2(gx.x, gy.x);
  vec2 g10 = vec2(gx.y, gy.y);
  vec2 g01 = vec2(gx.z, gy.z);
  vec2 g11 = vec2(gx.w, gy.w);
  vec4 norm = taylorInvSqrt(vec4(dot(g00,g00), dot(g01,g01), dot(g10,g10), dot(g11,g11)));
  g00 *= norm.x;
  g01 *= norm.y;
  g10 *= norm.z;
  g11 *= norm.w;
  float n00 = dot(g00, vec2(fx.x, fy.x));
  float n10 = dot(g10, vec2(fx.y, fy.y));
  float n01 = dot(g01, vec2(fx.z, fy.z));
  float n11 = dot(g11, vec2(fx.w, fy.w));
  vec2 fade_xy = fade(Pf.xy);
  vec2 n_x = mix(vec2(n00, n01), vec2(n10, n11), fade_xy.x);
  return 2.3 * mix(n_x.x, n_x.y, fade_xy.y);
}

float fbm(vec2 p) {
  float value = 0.0;
  float amp = 1.0;
  float freq = waveFrequency;
  
  for (int i = 0; i < 4; i++) {
    value += amp * abs(cnoise(p));
    p *= freq;
    amp *= waveAmplitude;
  }
  
  return value;
}

float pattern(vec2 p) {
  vec2 p2 = p - time * waveSpeed;
  return fbm(p + fbm(p2));
}

void main() {
  vec2 uv = vUv - 0.5;
  uv.x *= resolution.x / resolution.y;
  
  float f = pattern(uv);
  
  if (enableMouseInteraction == 1) {
    vec2 mouseNDC = (mousePos / resolution - 0.5) * vec2(1.0, -1.0);
    mouseNDC.x *= resolution.x / resolution.y;
    float dist = length(uv - mouseNDC);
    float effect = 1.0 - smoothstep(0.0, mouseRadius, dist);
    f -= 0.5 * effect;
  }
  
  vec3 col = mix(vec3(0.0), waveColor, f);
  gl_FragColor = vec4(col, 1.0);
}
`

const ditherFragmentShader = `
uniform float colorNum;
uniform float pixelSize;
uniform sampler2D tDiffuse;
uniform vec2 resolution;
varying vec2 vUv;

const float bayerMatrix8x8[64] = float[64](
  0.0/64.0,  48.0/64.0, 12.0/64.0, 60.0/64.0, 3.0/64.0,  51.0/64.0, 15.0/64.0, 63.0/64.0,
  32.0/64.0, 16.0/64.0, 44.0/64.0, 28.0/64.0, 35.0/64.0, 19.0/64.0, 47.0/64.0, 31.0/64.0,
  8.0/64.0,  56.0/64.0, 4.0/64.0,  52.0/64.0, 11.0/64.0, 59.0/64.0, 7.0/64.0,  55.0/64.0,
  40.0/64.0, 24.0/64.0, 36.0/64.0, 20.0/64.0, 43.0/64.0, 27.0/64.0, 39.0/64.0, 23.0/64.0,
  2.0/64.0,  50.0/64.0, 14.0/64.0, 62.0/64.0, 1.0/64.0,  49.0/64.0, 13.0/64.0, 61.0/64.0,
  34.0/64.0, 18.0/64.0, 46.0/64.0, 30.0/64.0, 33.0/64.0, 17.0/64.0, 45.0/64.0, 29.0/64.0,
  10.0/64.0, 58.0/64.0, 6.0/64.0,  54.0/64.0, 9.0/64.0,  57.0/64.0, 5.0/64.0,  53.0/64.0,
  42.0/64.0, 26.0/64.0, 38.0/64.0, 22.0/64.0, 41.0/64.0, 25.0/64.0, 37.0/64.0, 21.0/64.0
);

vec3 dither(vec2 uv, vec3 color) {
  vec2 scaledCoord = floor(uv * resolution / pixelSize);
  int x = int(mod(scaledCoord.x, 8.0));
  int y = int(mod(scaledCoord.y, 8.0));
  float threshold = bayerMatrix8x8[y * 8 + x] - 0.25;
  float step = 1.0 / (colorNum - 1.0);
  color += threshold * step;
  float bias = 0.2;
  color = clamp(color - bias, 0.0, 1.0);
  return floor(color * (colorNum - 1.0) + 0.5) / (colorNum - 1.0);
}

void main() {
  vec2 normalizedPixelSize = pixelSize / resolution;
  vec2 uvPixel = normalizedPixelSize * floor(vUv / normalizedPixelSize);
  vec4 color = texture2D(tDiffuse, uvPixel);
  color.rgb = dither(vUv, color.rgb);
  gl_FragColor = color;
}
`

const setupScene = () => {
  if (!canvasRef.value) return
  
  // Renderer
  renderer = new THREE.WebGLRenderer({
    canvas: canvasRef.value,
    antialias: true,
    alpha: false
  })
  renderer.setPixelRatio(1)
  renderer.setSize(window.innerWidth, window.innerHeight)
  
  // Scene
  scene = new THREE.Scene()
  
  // Camera
  camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1)
  
  // Wave mesh
  const geometry = new THREE.PlaneGeometry(2, 2)
  const material = new THREE.ShaderMaterial({
    vertexShader: waveVertexShader,
    fragmentShader: waveFragmentShader,
    uniforms: {
      time: { value: 0 },
      resolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) },
      waveSpeed: { value: props.waveSpeed },
      waveFrequency: { value: props.waveFrequency },
      waveAmplitude: { value: props.waveAmplitude },
      waveColor: { value: new THREE.Color(...waveColor.value) },
      mousePos: { value: mousePos.value },
      enableMouseInteraction: { value: props.enableMouseInteraction ? 1 : 0 },
      mouseRadius: { value: props.mouseRadius }
    }
  })
  
  mesh = new THREE.Mesh(geometry, material)
  scene.add(mesh)
  
  // Post-processing
  composer = new EffectComposer(renderer)
  composer.addPass(new RenderPass(scene, camera))
  
  const ditherPass = new ShaderPass({
    uniforms: {
      tDiffuse: { value: null },
      colorNum: { value: props.colorNum },
      pixelSize: { value: props.pixelSize },
      resolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) }
    },
    vertexShader: `
      varying vec2 vUv;
      void main() {
        vUv = uv;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
    `,
    fragmentShader: ditherFragmentShader
  })
  
  composer.addPass(ditherPass)
}

const animate = () => {
  if (!mesh || !composer) return
  
  if (!props.disableAnimation) {
    mesh.material.uniforms.time.value += 0.01
  }
  
  mesh.material.uniforms.waveColor.value.set(...waveColor.value)
  mesh.material.uniforms.enableMouseInteraction.value = props.enableMouseInteraction ? 1 : 0
  
  composer.render()
  animationId = requestAnimationFrame(animate)
}

const handleResize = () => {
  if (!renderer || !composer || !mesh) return
  
  const width = window.innerWidth
  const height = window.innerHeight
  
  renderer.setSize(width, height)
  composer.setSize(width, height)
  
  mesh.material.uniforms.resolution.value.set(width, height)
  
  // Update dither pass resolution
  const ditherPass = composer.passes[1]
  if (ditherPass && ditherPass.uniforms) {
    ditherPass.uniforms.resolution.value.set(width, height)
  }
}

const handleMouseMove = (e) => {
  if (!props.enableMouseInteraction) return
  mousePos.value.set(e.clientX, e.clientY)
  if (mesh) {
    mesh.material.uniforms.mousePos.value = mousePos.value
  }
}

onMounted(() => {
  setupScene()
  animate()
  
  window.addEventListener('resize', handleResize)
  if (props.enableMouseInteraction) {
    window.addEventListener('mousemove', handleMouseMove)
  }
})

onUnmounted(() => {
  if (animationId) {
    cancelAnimationFrame(animationId)
  }
  
  window.removeEventListener('resize', handleResize)
  window.removeEventListener('mousemove', handleMouseMove)
  
  if (renderer) {
    renderer.dispose()
  }
  if (scene) {
    scene.clear()
  }
})

watch(() => isDark.value, () => {
  if (mesh) {
    mesh.material.uniforms.waveColor.value.set(...waveColor.value)
  }
})
</script>

<style scoped>
.dither-container {
  width: 100%;
  height: 100%;
  display: block;
}
</style>
