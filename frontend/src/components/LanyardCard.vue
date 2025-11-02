<template>
  <div class="lanyard-wrapper">
    <canvas ref="canvasRef" class="lanyard-canvas"></canvas>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useDark } from '@vueuse/core'
import * as THREE from 'three'

const authStore = useAuthStore()
const isDark = useDark()
const canvasRef = ref(null)

const displayName = computed(() => {
  const name = authStore.user?.displayName || authStore.user?.email?.split('@')[0] || 'USER'
  return name.toUpperCase()
})

let scene, camera, renderer, card, strap, clip, animationId
let mouseX = 0, mouseY = 0
let targetRotationX = 0, targetRotationY = 0

const createLanyard = () => {
  // Scene setup
  scene = new THREE.Scene()
  scene.background = null
  
  camera = new THREE.PerspectiveCamera(35, canvasRef.value.clientWidth / canvasRef.value.clientHeight, 0.1, 1000)
  camera.position.set(0, 0, 15)
  
  renderer = new THREE.WebGLRenderer({ 
    canvas: canvasRef.value, 
    alpha: true,
    antialias: true 
  })
  renderer.setSize(canvasRef.value.clientWidth, canvasRef.value.clientHeight)
  renderer.setPixelRatio(window.devicePixelRatio)
  
  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 1.8)
  scene.add(ambientLight)
  
  const directionalLight1 = new THREE.DirectionalLight(0xffffff, 1.2)
  directionalLight1.position.set(5, 5, 5)
  scene.add(directionalLight1)
  
  const directionalLight2 = new THREE.DirectionalLight(0xffffff, 0.6)
  directionalLight2.position.set(-5, -5, 5)
  scene.add(directionalLight2)
  
  // Strap (black fabric-like)
  const strapGeometry = new THREE.BoxGeometry(0.25, 6, 0.08)
  const strapMaterial = new THREE.MeshStandardMaterial({ 
    color: 0x0a0a0a,
    roughness: 0.9,
    metalness: 0.05
  })
  strap = new THREE.Mesh(strapGeometry, strapMaterial)
  strap.position.y = 5.5
  scene.add(strap)
  
  // Add strap pattern (white atom icons)
  const createStrapPattern = () => {
    for (let i = 0; i < 5; i++) {
      // Create atom-like pattern
      const atomGroup = new THREE.Group()
      
      // Center circle
      const centerGeometry = new THREE.CircleGeometry(0.05, 16)
      const centerMaterial = new THREE.MeshBasicMaterial({ 
        color: 0xffffff,
        transparent: true,
        opacity: 0.9
      })
      const center = new THREE.Mesh(centerGeometry, centerMaterial)
      atomGroup.add(center)
      
      // Orbits
      for (let j = 0; j < 3; j++) {
        const angle = (j * Math.PI * 2) / 3
        const orbitGeometry = new THREE.TorusGeometry(0.08, 0.01, 8, 16)
        const orbitMaterial = new THREE.MeshBasicMaterial({ 
          color: 0xffffff,
          transparent: true,
          opacity: 0.6
        })
        const orbit = new THREE.Mesh(orbitGeometry, orbitMaterial)
        orbit.rotation.y = angle
        orbit.rotation.x = Math.PI / 2 + angle * 0.3
        atomGroup.add(orbit)
      }
      
      atomGroup.position.set(0, 7.2 - i * 1.4, 0.05)
      scene.add(atomGroup)
    }
  }
  createStrapPattern()
  
  // Metal clip/ring (darker, more realistic)
  const clipGeometry = new THREE.TorusGeometry(0.5, 0.1, 16, 32)
  const clipMaterial = new THREE.MeshStandardMaterial({ 
    color: 0x2a2a2a,
    metalness: 0.95,
    roughness: 0.15
  })
  clip = new THREE.Mesh(clipGeometry, clipMaterial)
  clip.position.y = 2.8
  clip.rotation.x = Math.PI / 2
  scene.add(clip)
  
  // Card (white with rounded corners)
  const cardShape = new THREE.Shape()
  const width = 5.5, height = 3.5, radius = 0.3
  
  cardShape.moveTo(-width/2 + radius, -height/2)
  cardShape.lineTo(width/2 - radius, -height/2)
  cardShape.quadraticCurveTo(width/2, -height/2, width/2, -height/2 + radius)
  cardShape.lineTo(width/2, height/2 - radius)
  cardShape.quadraticCurveTo(width/2, height/2, width/2 - radius, height/2)
  cardShape.lineTo(-width/2 + radius, height/2)
  cardShape.quadraticCurveTo(-width/2, height/2, -width/2, height/2 - radius)
  cardShape.lineTo(-width/2, -height/2 + radius)
  cardShape.quadraticCurveTo(-width/2, -height/2, -width/2 + radius, -height/2)
  
  const extrudeSettings = { depth: 0.1, bevelEnabled: true, bevelThickness: 0.02, bevelSize: 0.02, bevelSegments: 3 }
  const cardGeometry = new THREE.ExtrudeGeometry(cardShape, extrudeSettings)
  
  const cardMaterial = new THREE.MeshStandardMaterial({ 
    color: 0xfafafa,
    roughness: 0.2,
    metalness: 0.05
  })
  
  card = new THREE.Mesh(cardGeometry, cardMaterial)
  card.position.y = 0
  scene.add(card)
  
  // Create atom logo (black lines like in reference)
  const createAtomLogo = () => {
    const atomGroup = new THREE.Group()
    
    // Center nucleus
    const nucleusGeometry = new THREE.SphereGeometry(0.08, 16, 16)
    const nucleusMaterial = new THREE.MeshBasicMaterial({ color: 0x000000 })
    const nucleus = new THREE.Mesh(nucleusGeometry, nucleusMaterial)
    atomGroup.add(nucleus)
    
    // Create electron orbits (3 elliptical paths)
    const createOrbit = (rotationX, rotationY, rotationZ) => {
      const curve = new THREE.EllipseCurve(
        0, 0,
        0.45, 0.45,
        0, 2 * Math.PI,
        false,
        0
      )
      const points = curve.getPoints(50)
      const geometry = new THREE.BufferGeometry().setFromPoints(points)
      const material = new THREE.LineBasicMaterial({ 
        color: 0x000000,
        linewidth: 3
      })
      const orbit = new THREE.Line(geometry, material)
      orbit.rotation.x = rotationX
      orbit.rotation.y = rotationY
      orbit.rotation.z = rotationZ
      return orbit
    }
    
    // Three orbital rings at different angles
    const orbit1 = createOrbit(Math.PI / 2, 0, 0)
    const orbit2 = createOrbit(Math.PI / 2, Math.PI / 3, Math.PI / 6)
    const orbit3 = createOrbit(Math.PI / 2, -Math.PI / 3, -Math.PI / 6)
    
    atomGroup.add(orbit1)
    atomGroup.add(orbit2)
    atomGroup.add(orbit3)
    
    // Add electrons (small spheres)
    const electronGeometry = new THREE.SphereGeometry(0.06, 12, 12)
    const electronMaterial = new THREE.MeshBasicMaterial({ color: 0x000000 })
    
    const electron1 = new THREE.Mesh(electronGeometry, electronMaterial)
    electron1.position.set(0.45, 0, 0)
    atomGroup.add(electron1)
    
    const electron2 = new THREE.Mesh(electronGeometry, electronMaterial)
    electron2.position.set(-0.45, 0, 0)
    atomGroup.add(electron2)
    
    atomGroup.position.set(0, 0.3, 0.12)
    atomGroup.scale.set(1.2, 1.2, 1.2)
    
    return atomGroup
  }
  
  const atomLogo = createAtomLogo()
  card.add(atomLogo)
  
  // Add text to card using canvas texture - SIMPLIFIED
  const canvas = document.createElement('canvas')
  canvas.width = 1024
  canvas.height = 640
  const ctx = canvas.getContext('2d')
  
  // Clear canvas with white background
  ctx.fillStyle = '#ffffff'
  ctx.fillRect(0, 0, canvas.width, canvas.height)
  
  // User name setup
  const userName = displayName.value
  let fontSize = 90
  
  // Handle long names with smaller font
  if (userName.length > 12) {
    fontSize = 70
  }
  if (userName.length > 16) {
    fontSize = 55
  }
  
  // Set font before measuring
  ctx.font = `bold ${fontSize}px Arial, sans-serif`
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'
  
  // Measure text for background box
  const textMetrics = ctx.measureText(userName)
  const textWidth = textMetrics.width
  const paddingH = 50
  const paddingV = 25
  const centerY = 480
  
  // Draw purple background box (simple rectangle with rounded corners)
  const boxX = (canvas.width - textWidth - paddingH * 2) / 2
  const boxY = centerY - fontSize / 2 - paddingV
  const boxW = textWidth + paddingH * 2
  const boxH = fontSize + paddingV * 2
  const borderRadius = 20
  
  ctx.fillStyle = '#6366f1'
  ctx.beginPath()
  ctx.moveTo(boxX + borderRadius, boxY)
  ctx.lineTo(boxX + boxW - borderRadius, boxY)
  ctx.arcTo(boxX + boxW, boxY, boxX + boxW, boxY + borderRadius, borderRadius)
  ctx.lineTo(boxX + boxW, boxY + boxH - borderRadius)
  ctx.arcTo(boxX + boxW, boxY + boxH, boxX + boxW - borderRadius, boxY + boxH, borderRadius)
  ctx.lineTo(boxX + borderRadius, boxY + boxH)
  ctx.arcTo(boxX, boxY + boxH, boxX, boxY + boxH - borderRadius, borderRadius)
  ctx.lineTo(boxX, boxY + borderRadius)
  ctx.arcTo(boxX, boxY, boxX + borderRadius, boxY, borderRadius)
  ctx.closePath()
  ctx.fill()
  
  // Draw white text on top of purple box
  ctx.fillStyle = '#ffffff'
  ctx.font = `bold ${fontSize}px Arial, sans-serif`
  ctx.fillText(userName, canvas.width / 2, centerY)
  
  // Add "HELLO," text above
  ctx.fillStyle = '#666666'
  ctx.font = 'bold 40px Arial, sans-serif'
  ctx.fillText('HELLO,', canvas.width / 2, centerY - fontSize - 40)
  
  const texture = new THREE.CanvasTexture(canvas)
  texture.needsUpdate = true
  
  const textMaterial = new THREE.MeshBasicMaterial({ 
    map: texture,
    transparent: true,
    side: THREE.DoubleSide
  })
  
  const textGeometry = new THREE.PlaneGeometry(5.2, 3.25)
  const textMesh = new THREE.Mesh(textGeometry, textMaterial)
  textMesh.position.set(0, -0.5, 0.11)
  card.add(textMesh)
}

const animate = () => {
  animationId = requestAnimationFrame(animate)
  
  // Smooth rotation based on mouse
  const targetX = mouseY * 0.3
  const targetY = mouseX * 0.3
  
  targetRotationX += (targetX - targetRotationX) * 0.05
  targetRotationY += (targetY - targetRotationY) * 0.05
  
  // Apply physics-like swing
  const time = Date.now() * 0.001
  const swingX = Math.sin(time * 0.5) * 0.1
  const swingY = Math.sin(time * 0.7) * 0.05
  
  if (card) {
    card.rotation.x = targetRotationX + swingX
    card.rotation.y = targetRotationY + swingY
    card.rotation.z = targetRotationY * 0.5 + swingY
  }
  
  if (clip) {
    clip.rotation.y = Math.sin(time * 0.5) * 0.1
  }
  
  renderer.render(scene, camera)
}

const handleMouseMove = (e) => {
  const rect = canvasRef.value?.getBoundingClientRect()
  if (rect) {
    mouseX = ((e.clientX - rect.left) / rect.width) * 2 - 1
    mouseY = -((e.clientY - rect.top) / rect.height) * 2 + 1
  }
}

const handleResize = () => {
  if (!canvasRef.value) return
  
  const width = canvasRef.value.clientWidth
  const height = canvasRef.value.clientHeight
  
  camera.aspect = width / height
  camera.updateProjectionMatrix()
  renderer.setSize(width, height)
}

onMounted(() => {
  createLanyard()
  animate()
  window.addEventListener('mousemove', handleMouseMove)
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('mousemove', handleMouseMove)
  window.removeEventListener('resize', handleResize)
  if (animationId) {
    cancelAnimationFrame(animationId)
  }
  if (renderer) {
    renderer.dispose()
  }
})
</script>

<style scoped>
.lanyard-wrapper {
  position: relative;
  width: 100%;
  height: 450px;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding-top: 0;
  margin-top: -30px;
  margin-bottom: -40px;
}

.lanyard-canvas {
  width: 100%;
  height: 100%;
  max-width: 800px;
  cursor: grab;
}

.lanyard-canvas:active {
  cursor: grabbing;
}

@media (max-width: 768px) {
  .lanyard-wrapper {
    height: 380px;
  }
  
  .lanyard-canvas {
    max-width: 600px;
  }
}

@media (max-width: 480px) {
  .lanyard-wrapper {
    height: 320px;
  }
  
  .lanyard-canvas {
    max-width: 100%;
  }
}
</style>
