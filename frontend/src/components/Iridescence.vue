<template>
  <div ref="containerRef" class="iridescence-container" :style="containerStyle"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'

const props = defineProps({
  color: {
    type: Array,
    default: () => [1, 1, 1]
  },
  speed: {
    type: Number,
    default: 1.0
  },
  amplitude: {
    type: Number,
    default: 0.1
  },
  mouseReact: {
    type: Boolean,
    default: true
  }
})

const containerRef = ref(null)
const mousePos = ref({ x: 0.5, y: 0.5 })
let canvas = null
let ctx = null
let animationId = null
let startTime = Date.now()

const containerStyle = ref({
  width: '100%',
  height: '100%',
  position: 'relative'
})

const drawIridescence = () => {
  if (!canvas || !ctx) return
  
  const width = canvas.width
  const height = canvas.height
  const time = (Date.now() - startTime) * 0.001 * props.speed
  
  // Create gradient
  const imageData = ctx.createImageData(width, height)
  const data = imageData.data
  
  // Get mouse influence
  const mx = mousePos.value.x
  const my = mousePos.value.y
  
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const idx = (y * width + x) * 4
      
      // Normalize coordinates
      const nx = (x / width - 0.5) * 2
      const ny = (y / height - 0.5) * 2
      
      // Add mouse influence
      const mxOffset = (mx - 0.5) * props.amplitude * 2
      const myOffset = (my - 0.5) * props.amplitude * 2
      
      // Calculate waves
      let wave = 0
      const d = -time * 0.5
      let a = 0
      
      for (let i = 0; i < 8; i++) {
        a += Math.cos(i - d - a * (nx + mxOffset))
        wave += Math.sin((ny + myOffset) * i + a)
      }
      
      // Create color from waves
      const r = Math.cos(nx * Math.cos(d + wave)) * 0.6 + 0.4
      const g = Math.cos(ny * Math.cos(a + wave)) * 0.6 + 0.4
      const b = Math.cos((a + d) * 0.5 + 0.5) * 0.6 + 0.4
      
      // Apply color multiplier
      data[idx] = Math.floor(r * props.color[0] * 255)
      data[idx + 1] = Math.floor(g * props.color[1] * 255)
      data[idx + 2] = Math.floor(b * props.color[2] * 255)
      data[idx + 3] = 255
    }
  }
  
  ctx.putImageData(imageData, 0, 0)
  animationId = requestAnimationFrame(drawIridescence)
}

const resize = () => {
  if (!canvas || !containerRef.value) return
  
  const scale = 0.5 // Lower resolution for better performance
  canvas.width = containerRef.value.offsetWidth * scale
  canvas.height = containerRef.value.offsetHeight * scale
  canvas.style.width = '100%'
  canvas.style.height = '100%'
}

const handleMouseMove = (e) => {
  if (!props.mouseReact || !containerRef.value) return
  
  const rect = containerRef.value.getBoundingClientRect()
  mousePos.value.x = (e.clientX - rect.left) / rect.width
  mousePos.value.y = 1.0 - (e.clientY - rect.top) / rect.height
}

onMounted(() => {
  if (!containerRef.value) return
  
  // Create canvas
  canvas = document.createElement('canvas')
  canvas.style.width = '100%'
  canvas.style.height = '100%'
  canvas.style.display = 'block'
  
  ctx = canvas.getContext('2d', { willReadFrequently: true })
  
  containerRef.value.appendChild(canvas)
  
  // Setup
  resize()
  window.addEventListener('resize', resize)
  
  if (props.mouseReact) {
    containerRef.value.addEventListener('mousemove', handleMouseMove)
  }
  
  // Start animation
  drawIridescence()
})

onUnmounted(() => {
  if (animationId) {
    cancelAnimationFrame(animationId)
  }
  
  window.removeEventListener('resize', resize)
  
  if (containerRef.value && props.mouseReact) {
    containerRef.value.removeEventListener('mousemove', handleMouseMove)
  }
  
  if (canvas && containerRef.value && containerRef.value.contains(canvas)) {
    containerRef.value.removeChild(canvas)
  }
})

watch(() => [props.color, props.speed, props.amplitude, props.mouseReact], () => {
  // Animation will pick up new values automatically
}, { deep: true })
</script>

<style scoped>
.iridescence-container {
  width: 100%;
  height: 100%;
  position: relative;
}
</style>
