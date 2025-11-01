<template>
  <div class="relative w-full min-h-screen overflow-x-hidden">
    <!-- Background Effects - Conditional based on theme -->
    <DitherBackground v-if="isDark" />
    <div v-else class="fixed top-0 left-0 w-full h-full z-0">
      <Iridescence
        :color="[1, 1, 1]"
        :mouseReact="true"
        :amplitude="0.1"
        :speed="1.0"
      />
      <!-- Black shade overlay for better text contrast -->
      <div class="absolute inset-0 bg-black opacity-30 pointer-events-none" />
    </div>

    <!-- Main Content -->
    <div class="relative z-10">
      <!-- Navbar -->
      <div class="fixed top-0 left-0 right-0 z-20 flex justify-center pt-6 px-6">
        <nav class="w-full max-w-4xl">
          <div 
            class="backdrop-blur-2xl rounded-full px-8 py-4 flex items-center justify-between shadow-xl transition-colors duration-500"
            :style="{
              background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
              borderColor: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.15)',
              border: '1px solid',
              boxShadow: isDark ? '0 8px 32px rgba(0, 0, 0, 0.3)' : '0 8px 32px rgba(0, 0, 0, 0.1)'
            }"
          >
            <!-- Logo -->
            <div class="font-sora font-bold text-lg flex items-center gap-2 transition-colors duration-500" :style="{ color: textColor }">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2L2 7L12 12L22 7L12 2Z" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M2 17L12 22L22 17" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M2 12L12 17L22 12" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
              SkillSet AI
            </div>

            <!-- Nav Links + Theme Toggle -->
            <div class="flex items-center gap-8">
              <a href="#home" class="font-inter text-sm font-medium transition-all hover:opacity-70" :style="{ color: textColor }">
                Home
              </a>
              <a href="#docs" class="font-inter text-sm font-medium transition-all hover:opacity-70" :style="{ color: textColor }">
                Docs
              </a>
              
              <!-- Theme Toggle Button -->
              <button
                @click="toggleTheme"
                class="p-2 rounded-full transition-all duration-300 hover:scale-110"
                :style="{
                  background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                  border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)'}`
                }"
                aria-label="Toggle theme"
              >
                <!-- Sun icon for light mode -->
                <svg v-if="isDark" width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="12" cy="12" r="5" :stroke="textColor" strokeWidth="2"/>
                  <path d="M12 1V3M12 21V23M23 12H21M3 12H1M20.49 3.51L19.07 4.93M4.93 19.07L3.51 20.49M20.49 20.49L19.07 19.07M4.93 4.93L3.51 3.51" :stroke="textColor" strokeWidth="2" strokeLinecap="round"/>
                </svg>
                <!-- Moon icon for dark mode -->
                <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </button>
            </div>
          </div>
        </nav>
      </div>

      <!-- Hero Section -->
      <section class="relative min-h-screen flex items-center justify-center px-6 lg:px-12 pt-24">
        <div class="max-w-7xl mx-auto w-full text-center">
          <!-- Main Title -->
          <h1 
            class="font-sora font-extrabold leading-tight uppercase transition-colors duration-500"
            :style="{ 
              fontSize: 'clamp(48px, 8vw, 96px)',
              lineHeight: '1.1',
              letterSpacing: '-0.02em',
              ...(isDark 
                ? { color: textColor }
                : {
                    background: 'linear-gradient(90deg, #000000, #ffffff, #cccccc, #0000ff, #000000)',
                    backgroundSize: '200% 100%',
                    WebkitBackgroundClip: 'text',
                    WebkitTextFillColor: 'transparent',
                    backgroundClip: 'text',
                    animation: 'rgbGradient 3s linear infinite'
                  }
              )
            }"
          >
            <DecryptedText
              text="SKILLSET AI"
              :speed="200"
              :maxIterations="20"
              :sequential="true"
              revealDirection="start"
              animateOn="view"
              :loopInterval="8000"
              characters="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
            />
          </h1>

          <BlurText
            text="Unlock your potential with personalized learning."
            :delay="80"
            animateBy="words"
            direction="top"
            as="h2"
            className="font-sora text-lg md:text-xl mt-6 transition-colors duration-500"
            :style="{ color: textColor, opacity: 0.9 }"
          />

          <!-- Subtitle -->
          <BlurText
            text="Discover your strengths, close your skill gaps, and grow with AI-driven recommendations tailored for your career path."
            :delay="50"
            animateBy="words"
            direction="top"
            as="p"
            className="font-inter text-sm md:text-base leading-relaxed max-w-2xl mx-auto mt-4 transition-colors duration-500"
            :style="{ color: secondaryTextColor }"
          />

          <!-- Button Group -->
          <div class="flex flex-col sm:flex-row gap-4 justify-center mt-8 relative">
            <!-- Primary Button -->
            <button
              @click="showAuthModal = true"
              class="px-8 py-4 rounded-full font-inter font-bold shadow-lg transition-all duration-500 hover:scale-105"
              :style="{
                backgroundColor: isDark ? '#ffffff' : '#000000',
                color: isDark ? '#000000' : '#ffffff'
              }"
            >
              Get Started
            </button>

            <!-- Secondary Button -->
            <button
              class="px-8 py-4 rounded-full font-inter font-bold bg-transparent border-2 transition-all duration-500 hover:opacity-80"
              :style="{
                color: textColor,
                borderColor: isDark ? 'rgba(255, 255, 255, 0.3)' : 'rgba(0, 0, 0, 0.3)'
              }"
            >
              See Demo
            </button>
          </div>
        </div>
      </section>

      <!-- Features Section -->
      <section class="relative py-24 px-6 lg:px-12">
        <div class="max-w-7xl mx-auto">
          <!-- Section Title -->
          <div class="text-center mb-16">
            <BlurText
              text="WHY SKILLSET AI"
              :delay="100"
              animateBy="words"
              direction="top"
              as="h2"
              className="font-sora font-extrabold text-4xl md:text-5xl lg:text-6xl mb-4 uppercase tracking-wide transition-colors duration-500"
              :style="{ color: textColor }"
            />
            <div class="w-24 h-1 mx-auto rounded-full transition-colors duration-500" :style="{ background: textColor }" />
          </div>

          <!-- Feature Cards with BounceCards -->
          <div class="flex justify-center">
            <BounceCards
              :items="features"
              :containerWidth="900"
              :containerHeight="400"
              :animationDelay="0.5"
              :animationStagger="0.06"
              easeType="elastic.out(1, 0.8)"
              :enableHover="true"
            />
          </div>
        </div>
      </section>

      <!-- Advanced Grid Section -->
      <AdvancedGrid />

      <!-- Testimonials Carousel -->
      <TestimonialsCarousel />

      <!-- CTA Band -->
      <CTABand @openModal="showAuthModal = true" />

      <!-- Footer -->
      <footer class="relative py-12 px-6 transition-colors duration-500" :style="{ backgroundColor: isDark ? '#000000' : '#1a1a1a' }">
        <div class="max-w-7xl mx-auto text-center">
          <div class="flex items-center justify-center gap-2 mb-4">
            <svg class="w-6 h-6" fill="none" stroke="#ffffff" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 2L2 7L12 12L22 7L12 2Z"></path>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2 17L12 22L22 17"></path>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2 12L12 17L22 12"></path>
            </svg>
            <span class="text-lg font-bold text-white">SkillSet AI</span>
          </div>
          <p class="text-gray-400 text-sm">
            © 2024 SkillSet AI. All rights reserved.
          </p>
        </div>
      </footer>
    </div>

    <!-- Auth Modal -->
    <AuthModal v-if="showAuthModal" @close="showAuthModal = false" />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useDark, useToggle } from '@vueuse/core'
import DitherBackground from '../components/DitherBackground.vue'
import Iridescence from '../components/Iridescence.vue'
import DecryptedText from '../components/DecryptedText.vue'
import BlurText from '../components/BlurText.vue'
import BounceCards from '../components/BounceCards.vue'
import AuthModal from '../components/AuthModal.vue'
import AdvancedGrid from '../components/AdvancedGrid.vue'
import TestimonialsCarousel from '../components/TestimonialsCarousel.vue'
import CTABand from '../components/CTABand.vue'

const router = useRouter()
const isDark = useDark()
const toggleTheme = useToggle(isDark)
const showAuthModal = ref(false)

const textColor = computed(() => isDark.value ? '#ffffff' : '#000000')
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)')

const features = [
  {
    title: 'Analyze',
    description: 'Evaluate your current skill set using AI insights and comprehensive assessments.',
    icon: '◉'
  },
  {
    title: 'Learn',
    description: 'Get curated resources and personalized learning paths tailored to your goals.',
    icon: '◆'
  },
  {
    title: 'Grow',
    description: 'Track performance, measure progress, and reach your career goals faster.',
    icon: '▲'
  }
]
</script>

<style scoped>
@keyframes rgbGradient {
  0% {
    background-position: 0% 50%;
  }
  100% {
    background-position: 200% 50%;
  }
}
</style>
