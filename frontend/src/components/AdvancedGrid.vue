<template>
  <section class="relative py-24 px-6 lg:px-12">
    <div class="max-w-7xl mx-auto">
      <!-- Section Title -->
      <div class="text-center mb-4">
        <h2
          class="font-sora font-extrabold text-4xl md:text-5xl lg:text-6xl mb-4 uppercase tracking-wide transition-colors duration-500"
          :style="{ color: textColor }"
        >
          Extra Features
        </h2>
        <p class="font-inter text-lg mb-16 transition-colors duration-500" :style="{ color: secondaryTextColor }">
          Extra Features to Make It Stand Out
        </p>
      </div>

      <!-- BounceCards Animation - First Row -->
      <div class="flex justify-center mb-12">
        <BounceCards
          :items="gridItems"
          :containerWidth="1400"
          :containerHeight="300"
          :animationDelay="0.6"
          :animationStagger="0.08"
          easeType="elastic.out(1, 0.5)"
          :transformStyles="transformStyles"
          :enableHover="true"
        />
      </div>

      <!-- BounceCards Animation - Second Row -->
      <div class="flex justify-center">
        <BounceCards
          :items="extraGridItems"
          :containerWidth="900"
          :containerHeight="300"
          :animationDelay="0.8"
          :animationStagger="0.08"
          easeType="elastic.out(1, 0.5)"
          :transformStyles="extraTransformStyles"
          :enableHover="true"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useDark } from '@vueuse/core'
import BounceCards from './BounceCards.vue'

const isDark = useDark()
const textColor = computed(() => isDark.value ? '#ffffff' : '#000000')
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)')

const gridItems = [
  { 
    title: 'Multi-Voice Narration', 
    icon: '●',
    description: 'Let users pick narrator type (male/female/neutral tone, accent)'
  },
  { 
    title: 'Real-time Highlighting', 
    icon: '◆',
    description: 'While audio plays, highlight the text word-by-word'
  },
  { 
    title: 'Personal Learning Profile', 
    icon: '■',
    description: 'Remember user preferences (font, voice, colors) using Firebase Auth'
  },
  { 
    title: 'Accessibility Score', 
    icon: '★',
    description: 'Show how accessible a file was originally and how much your system improved it'
  },
  { 
    title: 'Collaborative Mode', 
    icon: '◉',
    description: 'Teachers can annotate simplified versions to add teaching notes or audio explanations'
  }
]

const extraGridItems = [
  { 
    title: 'Multi-language Support', 
    icon: '▲',
    description: 'Use translation + TTS to support non-English content'
  },
  { 
    title: 'Chrome Extension', 
    icon: '▼',
    description: 'A simple plugin to convert any webpage into an accessible format with one click'
  },
  { 
    title: 'AI Chat Assistant', 
    icon: '◈',
    description: 'Let users ask questions about the uploaded material and get AI-driven explanations'
  }
]

const transformStyles = [
  "rotate(5deg) translate(-260px)",
  "rotate(2deg) translate(-130px)",
  "rotate(-3deg)",
  "rotate(3deg) translate(130px)",
  "rotate(-4deg) translate(260px)"
]

const extraTransformStyles = [
  "rotate(5deg) translate(-150px)",
  "rotate(-3deg)",
  "rotate(5deg) translate(150px)"
]
</script>
