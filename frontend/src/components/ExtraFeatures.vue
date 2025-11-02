<template>
  <section class="extra-features-section relative py-24 px-6 lg:px-12">
    <div class="max-w-7xl mx-auto">
      
      <!-- Section Title -->
      <div class="text-center mb-20">
        <BlurText
          text="INNOVATIVE FEATURES"
          :delay="100"
          animateBy="words"
          direction="top"
          as="h2"
          className="font-sora font-extrabold text-4xl md:text-5xl lg:text-6xl mb-4 uppercase tracking-wide transition-colors duration-500"
          :style="{ color: textColor }"
        />
        <div class="w-24 h-1 mx-auto rounded-full transition-colors duration-500" :style="{ background: textColor }" />
        <p class="font-inter text-base md:text-lg mt-6 max-w-3xl mx-auto transition-colors duration-500" :style="{ color: secondaryTextColor }">
          Discover cutting-edge accessibility features designed to make learning inclusive, personalized, and effective for everyone.
        </p>
      </div>

      <!-- Features Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <!-- Feature 1: Multi-Voice Narration -->
        <div 
          class="feature-card backdrop-blur-xl rounded-3xl p-8 transition-all duration-500 hover:scale-105 cursor-pointer"
          :style="{
            background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.03)',
            border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'}`
          }"
        >
          <div class="flex items-center gap-3 mb-4">
            <div 
              class="w-12 h-12 rounded-full flex items-center justify-center text-xl"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
              }"
            >
              🎙️
            </div>
            <h3 class="font-sora font-bold text-xl transition-colors duration-500" :style="{ color: textColor }">
              Multi-Voice Narration
            </h3>
          </div>
          <p class="font-inter text-sm leading-relaxed mb-3 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Choose from multiple narrator voices and accents (male, female, neutral) with support for British, American, Indian, and more regional variations.
          </p>
          <p class="font-inter text-xs font-semibold transition-colors duration-500" :style="{ color: textColor, opacity: 0.6 }">
            📍 Dashboard + Reader View
          </p>
        </div>

        <!-- Feature 2: Real-time Highlighting -->
        <div 
          class="feature-card backdrop-blur-xl rounded-3xl p-8 transition-all duration-500 hover:scale-105 cursor-pointer"
          :style="{
            background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.03)',
            border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'}`
          }"
        >
          <div class="flex items-center gap-3 mb-4">
            <div 
              class="w-12 h-12 rounded-full flex items-center justify-center text-xl"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
              }"
            >
              ✨
            </div>
            <h3 class="font-sora font-bold text-xl transition-colors duration-500" :style="{ color: textColor }">
              Real-time Highlighting
            </h3>
          </div>
          <p class="font-inter text-sm leading-relaxed mb-3 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Each word is highlighted in sync with narration, improving focus and comprehension. Control playback speed, skip sections, and customize highlight colors.
          </p>
          <p class="font-inter text-xs font-semibold transition-colors duration-500" :style="{ color: textColor, opacity: 0.6 }">
            📍 Reader View
          </p>
        </div>

        <!-- Feature 3: Personal Learning Profile -->
        <div 
          class="feature-card backdrop-blur-xl rounded-3xl p-8 transition-all duration-500 hover:scale-105 cursor-pointer"
          :style="{
            background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.03)',
            border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'}`
          }"
        >
          <div class="flex items-center gap-3 mb-4">
            <div 
              class="w-12 h-12 rounded-full flex items-center justify-center text-xl"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
              }"
            >
              👤
            </div>
            <h3 class="font-sora font-bold text-xl transition-colors duration-500" :style="{ color: textColor }">
              Personal Profile
            </h3>
          </div>
          <p class="font-inter text-sm leading-relaxed mb-3 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Your preferences (fonts, voice, speed, colors) are saved via Firebase and automatically applied across all devices for a consistent experience.
          </p>
          <p class="font-inter text-xs font-semibold transition-colors duration-500" :style="{ color: textColor, opacity: 0.6 }">
            📍 User Settings (Global)
          </p>
        </div>

        <!-- Feature 4: Accessibility Score -->
        <div 
          class="feature-card backdrop-blur-xl rounded-3xl p-8 transition-all duration-500 hover:scale-105 cursor-pointer"
          :style="{
            background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.03)',
            border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'}`
          }"
        >
          <div class="flex items-center gap-3 mb-4">
            <div 
              class="w-12 h-12 rounded-full flex items-center justify-center text-xl"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
              }"
            >
              📊
            </div>
            <h3 class="font-sora font-bold text-xl transition-colors duration-500" :style="{ color: textColor }">
              Accessibility Score
            </h3>
          </div>
          <p class="font-inter text-sm leading-relaxed mb-3 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Rate content before and after processing. See metrics for readability, alt text, color contrast, and clarity. Example: 52% → 92% improvement.
          </p>
          <p class="font-inter text-xs font-semibold transition-colors duration-500" :style="{ color: textColor, opacity: 0.6 }">
            📍 Dashboard + File Summary
          </p>
        </div>

        <!-- Feature 5: Collaborative Mode -->
        <div 
          class="feature-card backdrop-blur-xl rounded-3xl p-8 transition-all duration-500 hover:scale-105 cursor-pointer"
          :style="{
            background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.03)',
            border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'}`
          }"
        >
          <div class="flex items-center gap-3 mb-4">
            <div 
              class="w-12 h-12 rounded-full flex items-center justify-center text-xl"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
              }"
            >
              👥
            </div>
            <h3 class="font-sora font-bold text-xl transition-colors duration-500" :style="{ color: textColor }">
              Collaborative Mode
            </h3>
          </div>
          <p class="font-inter text-sm leading-relaxed mb-3 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Teachers can annotate simplified versions, add teaching notes, or record audio explanations. Share materials with students and groups easily.
          </p>
          <p class="font-inter text-xs font-semibold transition-colors duration-500" :style="{ color: textColor, opacity: 0.6 }">
            📍 Teacher / Group Dashboard
          </p>
        </div>

        <!-- Feature 6: Multi-language Support -->
        <div 
          class="feature-card backdrop-blur-xl rounded-3xl p-8 transition-all duration-500 hover:scale-105 cursor-pointer"
          :style="{
            background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.03)',
            border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'}`
          }"
        >
          <div class="flex items-center gap-3 mb-4">
            <div 
              class="w-12 h-12 rounded-full flex items-center justify-center text-xl"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
              }"
            >
              🌍
            </div>
            <h3 class="font-sora font-bold text-xl transition-colors duration-500" :style="{ color: textColor }">
              Multi-language Support
            </h3>
          </div>
          <p class="font-inter text-sm leading-relaxed mb-3 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Auto-detect document language and translate to 60+ languages. TTS narration available in target languages with native speaker quality.
          </p>
          <p class="font-inter text-xs font-semibold transition-colors duration-500" :style="{ color: textColor, opacity: 0.6 }">
            📍 Global Feature (All Pages)
          </p>
        </div>

        <!-- Feature 7: Chrome Extension -->
        <div 
          class="feature-card backdrop-blur-xl rounded-3xl p-8 transition-all duration-500 hover:scale-105 cursor-pointer"
          :style="{
            background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.03)',
            border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'}`
          }"
        >
          <div class="flex items-center gap-3 mb-4">
            <div 
              class="w-12 h-12 rounded-full flex items-center justify-center text-xl"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
              }"
            >
              🔌
            </div>
            <h3 class="font-sora font-bold text-xl transition-colors duration-500" :style="{ color: textColor }">
              Chrome Extension
            </h3>
          </div>
          <p class="font-inter text-sm leading-relaxed mb-3 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Install our browser tool to convert any webpage into an accessible version instantly. One-click simplification, TTS, and sync with your profile.
          </p>
          <p class="font-inter text-xs font-semibold transition-colors duration-500" :style="{ color: textColor, opacity: 0.6 }">
            📍 External Tool (Connects to Platform)
          </p>
        </div>

        <!-- Feature 8: AI Chat Assistant -->
        <div 
          class="feature-card backdrop-blur-xl rounded-3xl p-8 transition-all duration-500 hover:scale-105 cursor-pointer"
          :style="{
            background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.03)',
            border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'}`
          }"
        >
          <div class="flex items-center gap-3 mb-4">
            <div 
              class="w-12 h-12 rounded-full flex items-center justify-center text-xl"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
              }"
            >
              💬
            </div>
            <h3 class="font-sora font-bold text-xl transition-colors duration-500" :style="{ color: textColor }">
              AI Chat Assistant
            </h3>
          </div>
          <p class="font-inter text-sm leading-relaxed mb-3 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Ask contextual questions about uploaded material. Get summaries, explanations, and clarifications in accessible language. Example: "Explain this equation."
          </p>
          <p class="font-inter text-xs font-semibold transition-colors duration-500" :style="{ color: textColor, opacity: 0.6 }">
            📍 Reader View + Dashboard
          </p>
        </div>

        <!-- Feature 9: Advanced Processing -->
        <div 
          class="feature-card backdrop-blur-xl rounded-3xl p-8 transition-all duration-500 hover:scale-105 cursor-pointer"
          :style="{
            background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.03)',
            border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'}`
          }"
        >
          <div class="flex items-center gap-3 mb-4">
            <div 
              class="w-12 h-12 rounded-full flex items-center justify-center text-xl"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
              }"
            >
              🤖
            </div>
            <h3 class="font-sora font-bold text-xl transition-colors duration-500" :style="{ color: textColor }">
              AI Processing
            </h3>
          </div>
          <p class="font-inter text-sm leading-relaxed mb-3 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Advanced NLP algorithms simplify complex text, improve readability, and generate alt text for images. Transform PDFs, DOCX, and URLs automatically.
          </p>
          <p class="font-inter text-xs font-semibold transition-colors duration-500" :style="{ color: textColor, opacity: 0.6 }">
            📍 Upload + Processing Engine
          </p>
        </div>

      </div>

      <!-- Call to Action -->
      <div class="text-center mt-16">
        <button
          @click="$emit('openModal')"
          class="px-10 py-5 rounded-full font-inter font-bold shadow-2xl transition-all duration-300 hover:scale-105"
          :style="{
            backgroundColor: isDark ? '#ffffff' : '#000000',
            color: isDark ? '#000000' : '#ffffff'
          }"
        >
          Experience These Features
        </button>
      </div>

    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useDark } from '@vueuse/core'
import BlurText from './BlurText.vue'

const isDark = useDark()

defineEmits(['openModal'])

const textColor = computed(() => isDark.value ? '#ffffff' : '#000000')
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)')
</script>

<style scoped>
.feature-card {
  position: relative;
  overflow: hidden;
}

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, transparent, currentColor, transparent);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.feature-card:hover::before {
  opacity: 0.3;
}
</style>
