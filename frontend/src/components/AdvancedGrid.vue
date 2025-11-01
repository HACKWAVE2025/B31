<template>
  <section class="relative py-24 px-6 lg:px-12">
    <div class="max-w-7xl mx-auto">
      <!-- Section Title -->
      <h2
        class="font-sora font-extrabold text-4xl md:text-5xl lg:text-6xl text-center mb-16 uppercase tracking-wide transition-colors duration-500"
        :style="{ color: textColor }"
      >
        Powerful Features
      </h2>

      <!-- BounceCards Animation -->
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
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useDark } from '@vueuse/core'
import BounceCards from './BounceCards.vue'

const isDark = useDark()
const textColor = computed(() => isDark.value ? '#ffffff' : '#000000')

const gridItems = [
  { 
    title: 'AI Skill Assessment', 
    icon: '●',
    description: 'Get personalized AI-powered skill evaluations'
  },
  { 
    title: 'Roadmap Generator', 
    icon: '◆',
    description: 'Create custom learning paths tailored to your goals'
  },
  { 
    title: 'Progress Analytics', 
    icon: '■',
    description: 'Track your improvement with detailed insights'
  },
  { 
    title: 'Smart Recommendations', 
    icon: '★',
    description: 'Discover resources that match your learning style'
  },
  { 
    title: 'Skill Gap Detection', 
    icon: '◉',
    description: 'Identify areas where you need to improve'
  }
]

const transformStyles = [
  "rotate(5deg) translate(-260px)",
  "rotate(2deg) translate(-130px)",
  "rotate(-3deg)",
  "rotate(3deg) translate(130px)",
  "rotate(-4deg) translate(260px)"
]
</script>
