<template>
  <span 
    ref="containerRef" 
    :class="parentClassName" 
    :style="wrapperStyle"
    @mouseenter="handleMouseEnter"
    @mouseleave="handleMouseLeave"
  >
    <!-- Screen reader text -->
    <span :style="srOnlyStyle">{{ text }}</span>
    
    <!-- Animated text -->
    <span aria-hidden="true">
      <span 
        v-for="(char, index) in displayText.split('')" 
        :key="index"
        :class="(revealedIndices.has(index) || !isScrambling || !isHovering) ? className : encryptedClassName"
      >
        {{ char }}
      </span>
    </span>
  </span>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  text: {
    type: String,
    required: true
  },
  speed: {
    type: Number,
    default: 50
  },
  maxIterations: {
    type: Number,
    default: 10
  },
  sequential: {
    type: Boolean,
    default: false
  },
  revealDirection: {
    type: String,
    default: 'start',
    validator: (value) => ['start', 'end', 'center'].includes(value)
  },
  useOriginalCharsOnly: {
    type: Boolean,
    default: false
  },
  characters: {
    type: String,
    default: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+'
  },
  className: {
    type: String,
    default: ''
  },
  parentClassName: {
    type: String,
    default: ''
  },
  encryptedClassName: {
    type: String,
    default: ''
  },
  animateOn: {
    type: String,
    default: 'hover',
    validator: (value) => ['hover', 'view', 'both'].includes(value)
  },
  loopInterval: {
    type: Number,
    default: 0
  }
})

const displayText = ref(props.text)
const isHovering = ref(false)
const isScrambling = ref(false)
const revealedIndices = ref(new Set())
const hasAnimated = ref(false)
const containerRef = ref(null)

let interval = null
let loopTimeout = null
let observer = null
let currentIteration = 0

const wrapperStyle = computed(() => ({
  display: 'inline-block',
  whiteSpace: 'pre-wrap'
}))

const srOnlyStyle = computed(() => ({
  position: 'absolute',
  width: '1px',
  height: '1px',
  padding: 0,
  margin: '-1px',
  overflow: 'hidden',
  clip: 'rect(0,0,0,0)',
  border: 0
}))

const getNextIndex = (revealedSet) => {
  const textLength = props.text.length
  switch (props.revealDirection) {
    case 'start':
      return revealedSet.size
    case 'end':
      return textLength - 1 - revealedSet.size
    case 'center': {
      const middle = Math.floor(textLength / 2)
      const offset = Math.floor(revealedSet.size / 2)
      const nextIndex = revealedSet.size % 2 === 0 ? middle + offset : middle - offset - 1

      if (nextIndex >= 0 && nextIndex < textLength && !revealedSet.has(nextIndex)) {
        return nextIndex
      }

      for (let i = 0; i < textLength; i++) {
        if (!revealedSet.has(i)) return i
      }
      return 0
    }
    default:
      return revealedSet.size
  }
}

const availableChars = computed(() => {
  return props.useOriginalCharsOnly
    ? Array.from(new Set(props.text.split(''))).filter(char => char !== ' ')
    : props.characters.split('')
})

const shuffleText = (originalText, currentRevealed) => {
  if (props.useOriginalCharsOnly) {
    const positions = originalText.split('').map((char, i) => ({
      char,
      isSpace: char === ' ',
      index: i,
      isRevealed: currentRevealed.has(i)
    }))

    const nonSpaceChars = positions.filter(p => !p.isSpace && !p.isRevealed).map(p => p.char)

    for (let i = nonSpaceChars.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1))
      ;[nonSpaceChars[i], nonSpaceChars[j]] = [nonSpaceChars[j], nonSpaceChars[i]]
    }

    let charIndex = 0
    return positions
      .map(p => {
        if (p.isSpace) return ' '
        if (p.isRevealed) return originalText[p.index]
        return nonSpaceChars[charIndex++]
      })
      .join('')
  } else {
    return originalText
      .split('')
      .map((char, i) => {
        if (char === ' ') return ' '
        if (currentRevealed.has(i)) return originalText[i]
        return availableChars.value[Math.floor(Math.random() * availableChars.value.length)]
      })
      .join('')
  }
}

const startAnimation = () => {
  isScrambling.value = true
  currentIteration = 0
  
  interval = setInterval(() => {
    if (props.sequential) {
      if (revealedIndices.value.size < props.text.length) {
        const nextIndex = getNextIndex(revealedIndices.value)
        const newRevealed = new Set(revealedIndices.value)
        newRevealed.add(nextIndex)
        displayText.value = shuffleText(props.text, newRevealed)
        revealedIndices.value = newRevealed
      } else {
        clearInterval(interval)
        interval = null
        isScrambling.value = false
      }
    } else {
      displayText.value = shuffleText(props.text, revealedIndices.value)
      currentIteration++
      if (currentIteration >= props.maxIterations) {
        clearInterval(interval)
        interval = null
        isScrambling.value = false
        displayText.value = props.text
      }
    }
  }, props.speed)
}

const stopAnimation = () => {
  if (interval) {
    clearInterval(interval)
    interval = null
  }
  displayText.value = props.text
  revealedIndices.value = new Set()
  isScrambling.value = false
}

watch(() => isHovering.value, (newVal) => {
  if (newVal) {
    startAnimation()
  } else {
    stopAnimation()
  }
})

const handleMouseEnter = () => {
  if (props.animateOn === 'hover' || props.animateOn === 'both') {
    isHovering.value = true
  }
}

const handleMouseLeave = () => {
  if (props.animateOn === 'hover' || props.animateOn === 'both') {
    isHovering.value = false
  }
}

const startLoop = () => {
  loopTimeout = setTimeout(() => {
    isHovering.value = false
    revealedIndices.value = new Set()
    
    setTimeout(() => {
      isHovering.value = true
      startLoop()
    }, 100)
  }, props.loopInterval)
}

onMounted(() => {
  if (props.animateOn === 'view' || props.animateOn === 'both') {
    const observerCallback = (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !hasAnimated.value) {
          isHovering.value = true
          hasAnimated.value = true
          
          if (props.loopInterval > 0) {
            setTimeout(startLoop, props.loopInterval)
          }
        }
      })
    }

    observer = new IntersectionObserver(observerCallback, {
      root: null,
      rootMargin: '0px',
      threshold: 0.1
    })

    if (containerRef.value) {
      observer.observe(containerRef.value)
    }
  }
})

onUnmounted(() => {
  if (interval) clearInterval(interval)
  if (loopTimeout) clearTimeout(loopTimeout)
  if (observer) observer.disconnect()
})
</script>
