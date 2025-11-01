<template>
  <component 
    :is="as" 
    ref="containerRef" 
    :class="className"
    :style="style"
  >
    <span
      v-for="(segment, index) in elements"
      :key="index"
      :style="{
        display: 'inline-block',
        willChange: 'transform, filter, opacity'
      }"
      :class="['inline-block', inView ? 'animate' : '']"
      :data-index="index"
    >
      {{ segment === ' ' ? '\u00A0' : segment }}{{ animateBy === 'words' && index < elements.length - 1 ? '\u00A0' : '' }}
    </span>
  </component>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useMotion } from '@vueuse/motion'

const props = defineProps({
  text: {
    type: String,
    default: ''
  },
  delay: {
    type: Number,
    default: 200
  },
  className: {
    type: String,
    default: ''
  },
  animateBy: {
    type: String,
    default: 'words',
    validator: (value) => ['words', 'characters'].includes(value)
  },
  direction: {
    type: String,
    default: 'top',
    validator: (value) => ['top', 'bottom'].includes(value)
  },
  threshold: {
    type: Number,
    default: 0.1
  },
  rootMargin: {
    type: String,
    default: '0px'
  },
  stepDuration: {
    type: Number,
    default: 0.35
  },
  as: {
    type: String,
    default: 'p'
  },
  style: {
    type: Object,
    default: () => ({})
  }
})

const emit = defineEmits(['animation-complete'])

const containerRef = ref(null)
const inView = ref(false)
let observer = null

const elements = computed(() => {
  return props.animateBy === 'words' ? props.text.split(' ') : props.text.split('')
})

const animationFrom = computed(() => {
  return props.direction === 'top' 
    ? { filter: 'blur(10px)', opacity: 0, y: -50 } 
    : { filter: 'blur(10px)', opacity: 0, y: 50 }
})

const animationTo = computed(() => {
  return [
    {
      filter: 'blur(5px)',
      opacity: 0.5,
      y: props.direction === 'top' ? 5 : -5
    },
    { filter: 'blur(0px)', opacity: 1, y: 0 }
  ]
})

onMounted(() => {
  if (!containerRef.value) return
  
  observer = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting) {
        inView.value = true
        
        // Animate each span
        const spans = containerRef.value.querySelectorAll('span')
        spans.forEach((span, index) => {
          const { variant } = useMotion(span, {
            initial: animationFrom.value,
            enter: {
              ...animationTo.value[1],
              transition: {
                delay: (index * props.delay) / 1000,
                duration: props.stepDuration * 1000
              }
            }
          })
          
          variant.value = 'enter'
          
          // Emit completion for last element
          if (index === spans.length - 1) {
            setTimeout(() => {
              emit('animation-complete')
            }, (index * props.delay) + (props.stepDuration * 1000))
          }
        })
        
        observer?.unobserve(containerRef.value)
      }
    },
    { threshold: props.threshold, rootMargin: props.rootMargin }
  )
  
  observer.observe(containerRef.value)
})

onUnmounted(() => {
  if (observer) {
    observer.disconnect()
  }
})
</script>
