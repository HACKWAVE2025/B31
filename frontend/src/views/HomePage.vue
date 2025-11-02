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
          <div 
            class="gradient-title-wrapper font-sora font-black leading-tight uppercase transition-colors duration-500"
            :class="{ 'light-mode-gradient': !isDark }"
            :style="{ 
              fontSize: 'clamp(72px, 12vw, 140px)',
              lineHeight: '1.05',
              letterSpacing: '-0.03em',
              fontWeight: '900'
            }"
          >
            <h1 
              class="gradient-title-content"
              :style="{ 
                color: isDark ? textColor : 'inherit'
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
          </div>

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
          <div ref="heroButtonGroup" class="flex flex-col sm:flex-row gap-4 justify-center mt-8 relative">
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
          
          <!-- Sticky Bottom Get Started Button (appears on scroll) -->
          <Transition name="slide-up">
            <div
              v-if="showStickyButton"
              class="fixed bottom-8 left-1/2 transform -translate-x-1/2 z-50"
            >
              <button
                @click="showAuthModal = true"
                class="px-10 py-5 rounded-full font-inter font-bold shadow-2xl transition-all duration-300 hover:scale-105 backdrop-blur-sm"
                :style="{
                  backgroundColor: isDark ? '#ffffff' : '#000000',
                  color: isDark ? '#000000' : '#ffffff',
                  boxShadow: isDark ? '0 20px 60px rgba(255, 255, 255, 0.3)' : '0 20px 60px rgba(0, 0, 0, 0.5)'
                }"
              >
                Get Started
              </button>
            </div>
          </Transition>
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
              :containerWidth="800"
              :containerHeight="400"
              :animationDelay="0.5"
              :animationStagger="0.06"
              easeType="elastic.out(1, 0.8)"
              :transformStyles="whySkillsetTransforms"
              :enableHover="true"
            />
          </div>
        </div>
      </section>

      <!-- Extra Features Section -->
      <ExtraFeatures @openModal="showAuthModal = true" />

      <!-- Powerful Features Section -->
      <section class="relative py-24 px-6 lg:px-12">
        <div class="max-w-7xl mx-auto">
          <!-- Section Title -->
          <div class="text-center mb-16">
            <BlurText
              text="POWERFUL FEATURES"
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
              :items="powerfulFeatures"
              :containerWidth="1000"
              :containerHeight="400"
              :animationDelay="0.7"
              :animationStagger="0.08"
              easeType="elastic.out(1, 0.8)"
              :transformStyles="powerfulFeaturesTransforms"
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
      <Footer />
    </div>

    <!-- Auth Modal -->
    <AuthModal v-model="showAuthModal" @close="showAuthModal = false" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useDark } from '@vueuse/core'
import DitherBackground from '../components/DitherBackground.vue'
import Iridescence from '../components/Iridescence.vue'
import DecryptedText from '../components/DecryptedText.vue'
import BlurText from '../components/BlurText.vue'
import BounceCards from '../components/BounceCards.vue'
import AuthModal from '../components/AuthModal.vue'
import ExtraFeatures from '../components/ExtraFeatures.vue'
import AdvancedGrid from '../components/AdvancedGrid.vue'
import TestimonialsCarousel from '../components/TestimonialsCarousel.vue'
import CTABand from '../components/CTABand.vue'
import Footer from '../components/Footer.vue'

const router = useRouter()
const isDark = useDark()
const toggleTheme = () => {
  isDark.value = !isDark.value
  console.log('Theme toggled, isDark:', isDark.value)
}
const showAuthModal = ref(false)

// Sticky button logic
const showStickyButton = ref(false)
const heroButtonGroup = ref(null)

const handleScroll = () => {
  if (heroButtonGroup.value) {
    const rect = heroButtonGroup.value.getBoundingClientRect()
    // Show sticky button when hero buttons are scrolled out of view
    showStickyButton.value = rect.bottom < 0
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  handleScroll() // Check initial state
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

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

const whySkillsetTransforms = [
  'rotate(5deg) translate(-150px)',
  'rotate(-3deg)',
  'rotate(5deg) translate(150px)'
]

const powerfulFeatures = [
  {
    title: 'AI-Powered Analysis',
    description: 'Advanced machine learning algorithms analyze your skills and provide personalized insights.',
    icon: '●'
  },
  {
    title: 'Smart Roadmaps',
    description: 'Get custom learning paths designed specifically for your career goals and skill gaps.',
    icon: '■'
  },
  {
    title: 'Real-time Analytics',
    description: 'Track your progress with comprehensive dashboards and performance metrics.',
    icon: '▼'
  },
  {
    title: 'Expert Resources',
    description: 'Access curated content from industry experts and top learning platforms.',
    icon: '◆'
  },
  {
    title: 'Career Insights',
    description: 'Discover trending skills and opportunities aligned with your professional journey.',
    icon: '★'
  }
]

const powerfulFeaturesTransforms = [
  'rotate(10deg) translate(-220px)',
  'rotate(5deg) translate(-110px)',
  'rotate(-3deg)',
  'rotate(-10deg) translate(110px)',
  'rotate(2deg) translate(220px)'
]
</script>

<style scoped>
/* Gradient wrapper applies the animated gradient background */
.gradient-title-wrapper {
  display: inline-block;
  position: relative;
}

.light-mode-gradient {
  background: linear-gradient(90deg, #000000, #ffffff, #d3d3d3, #0066ff, #87ceeb, #000000);
  background-size: 300% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  animation: gradientMove 6s linear infinite;
}

/* Make the content and all children transparent to show the gradient */
.light-mode-gradient .gradient-title-content,
.light-mode-gradient :deep(*) {
  color: transparent !important;
  -webkit-text-fill-color: transparent !important;
}

/* Sticky button slide-up animation */
.slide-up-enter-active {
  transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.slide-up-leave-active {
  transition: all 0.3s ease-out;
}

.slide-up-enter-from {
  opacity: 0;
  transform: translate(-50%, 100px);
}

.slide-up-leave-to {
  opacity: 0;
  transform: translate(-50%, 100px);
}

.slide-up-enter-to,
.slide-up-leave-from {
  opacity: 1;
  transform: translate(-50%, 0);
}

@keyframes gradientMove {
  0% {
    background-position: 300% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

@keyframes rgbGradient {
  0% {
    background-position: 0% 50%;
  }
  100% {
    background-position: 200% 50%;
  }
}
</style>
