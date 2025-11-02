<template>
  <div
    ref="containerRef"
    :class="['bounceCardsContainer', className]"
    :style="{
      position: 'relative',
      width: containerWidth + 'px',
      height: containerHeight + 'px'
    }"
  >
    <div
      v-for="(item, idx) in items"
      :key="idx"
      :class="['bounce-card', `bounce-card-${idx}`, 'transition-colors', 'duration-500', { 'has-image': item.image }]"
      :style="{
        borderColor: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.2)',
        background: item.image ? 'transparent' : (isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(255, 255, 255, 0.5)'),
        boxShadow: isDark ? '0 10px 30px rgba(128, 128, 128, 0.1)' : '0 10px 30px rgba(0, 0, 0, 0.15)'
      }"
      @mouseenter="() => pushSiblings(idx)"
      @mouseleave="resetSiblings"
    >
      <!-- Image Card (if image provided) -->
      <img 
        v-if="item.image" 
        :src="item.image" 
        :alt="item.title || `card-${idx}`"
        class="bounce-card-image"
      />
      
      <!-- Text Card (if no image) -->
      <template v-else>
        <!-- Icon -->
        <div class="bounce-card-icon transition-colors duration-500" :style="{ color: isDark ? '#ffffff' : '#000000' }">
          <component :is="item.icon" v-if="typeof item.icon === 'object'" />
          <span v-else v-html="item.icon"></span>
        </div>
        
        <!-- Title -->
        <h3 class="bounce-card-title transition-colors duration-500" :style="{ color: isDark ? '#ffffff' : '#000000' }">
          {{ item.title }}
        </h3>
        
        <!-- Description -->
        <p v-if="item.description" class="bounce-card-description transition-colors duration-500" :style="{ color: isDark ? 'rgba(255, 255, 255, 0.8)' : 'rgba(0, 0, 0, 0.8)' }">
          {{ item.description }}
        </p>
      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { gsap } from 'gsap'
import { useDark } from '@vueuse/core'

const props = defineProps({
  className: {
    type: String,
    default: ''
  },
  items: {
    type: Array,
    default: () => []
  },
  containerWidth: {
    type: Number,
    default: 400
  },
  containerHeight: {
    type: Number,
    default: 400
  },
  animationDelay: {
    type: Number,
    default: 0.5
  },
  animationStagger: {
    type: Number,
    default: 0.06
  },
  easeType: {
    type: String,
    default: 'elastic.out(1, 0.8)'
  },
  transformStyles: {
    type: Array,
    default: () => [
      'rotate(10deg) translate(-170px)',
      'rotate(5deg) translate(-85px)',
      'rotate(-3deg)',
      'rotate(-10deg) translate(85px)',
      'rotate(2deg) translate(170px)'
    ]
  },
  enableHover: {
    type: Boolean,
    default: true
  }
})

const containerRef = ref(null)
const isDark = useDark()

const getNoRotationTransform = (transformStr) => {
  const hasRotate = /rotate\([\s\S]*?\)/.test(transformStr)
  if (hasRotate) {
    return transformStr.replace(/rotate\([\s\S]*?\)/, 'rotate(0deg)')
  } else if (transformStr === 'none') {
    return 'rotate(0deg)'
  } else {
    return `${transformStr} rotate(0deg)`
  }
}

const getPushedTransform = (baseTransform, offsetX) => {
  const translateRegex = /translate\(([-0-9.]+)px\)/
  const match = baseTransform.match(translateRegex)
  if (match) {
    const currentX = parseFloat(match[1])
    const newX = currentX + offsetX
    return baseTransform.replace(translateRegex, `translate(${newX}px)`)
  } else {
    return baseTransform === 'none' ? `translate(${offsetX}px)` : `${baseTransform} translate(${offsetX}px)`
  }
}

const pushSiblings = (hoveredIdx) => {
  if (!props.enableHover || !containerRef.value) return
  
  props.items.forEach((_, i) => {
    const card = containerRef.value.querySelector(`.bounce-card-${i}`)
    if (!card) return
    
    gsap.killTweensOf(card)

    const baseTransform = props.transformStyles[i] || 'none'

    if (i === hoveredIdx) {
      const noRotationTransform = getNoRotationTransform(baseTransform)
      gsap.to(card, {
        transform: noRotationTransform,
        duration: 0.4,
        ease: 'back.out(1.4)',
        overwrite: 'auto'
      })
    } else {
      const offsetX = i < hoveredIdx ? -160 : 160
      const pushedTransform = getPushedTransform(baseTransform, offsetX)

      const distance = Math.abs(hoveredIdx - i)
      const delay = distance * 0.05

      gsap.to(card, {
        transform: pushedTransform,
        duration: 0.4,
        ease: 'back.out(1.4)',
        delay,
        overwrite: 'auto'
      })
    }
  })
}

const resetSiblings = () => {
  if (!props.enableHover || !containerRef.value) return
  
  props.items.forEach((_, i) => {
    const card = containerRef.value.querySelector(`.bounce-card-${i}`)
    if (!card) return
    
    gsap.killTweensOf(card)
    const baseTransform = props.transformStyles[i] || 'none'
    gsap.to(card, {
      transform: baseTransform,
      duration: 0.4,
      ease: 'back.out(1.4)',
      overwrite: 'auto'
    })
  })
}

onMounted(() => {
  if (!containerRef.value) return
  
  const cards = containerRef.value.querySelectorAll('.bounce-card')
  if (cards.length === 0) return
  
  // Set initial transforms
  cards.forEach((card, idx) => {
    const baseTransform = props.transformStyles[idx] || 'none'
    gsap.set(card, { transform: baseTransform })
  })
  
  // Animate in
  gsap.fromTo(
    cards,
    { scale: 0 },
    {
      scale: 1,
      stagger: props.animationStagger,
      ease: props.easeType,
      delay: props.animationDelay
    }
  )
})
</script>

<style scoped>
.bounceCardsContainer {
  margin: 0 auto;
}

.bounce-card {
  position: absolute;
  width: 280px;
  height: 360px;
  padding: 2rem;
  border-radius: 24px;
  border: 1px solid;
  backdrop-filter: blur(10px);
  top: 50%;
  left: 50%;
  margin-left: -140px;
  margin-top: -180px;
  transform-origin: center;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  /* GSAP handles transform animations */
}

.bounce-card-icon {
  font-size: 3.5rem;
  margin-bottom: 1.5rem;
}

.bounce-card-title {
  font-family: 'Sora', sans-serif;
  font-weight: 700;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.bounce-card-description {
  font-family: 'Inter', sans-serif;
  font-size: 0.95rem;
  line-height: 1.6;
}

.bounce-card.has-image {
  padding: 0;
  overflow: hidden;
  width: 200px;
  height: 200px;
  margin-left: -100px;
  margin-top: -100px;
  border-width: 5px;
}

.bounce-card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
