<template>
  <footer class="relative py-16 px-6 lg:px-12 transition-colors duration-500"
    :style="{
      background: isDark 
        ? 'linear-gradient(180deg, rgba(0, 0, 0, 0.6) 0%, rgba(0, 0, 0, 0.9) 100%)'
        : 'linear-gradient(180deg, rgba(255, 255, 255, 0.7) 0%, rgba(240, 240, 255, 0.9) 100%)',
      backdropFilter: 'blur(20px)',
      borderTop: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
    }">
    <div class="max-w-7xl mx-auto">
      <!-- Main Footer Content -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-12">
        
        <!-- About Us Section -->
        <div>
          <div class="flex items-center gap-2 mb-4">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2L2 7L12 12L22 7L12 2Z" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M2 17L12 22L22 17" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M2 12L12 17L22 12" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
            <h3 class="font-sora font-bold text-xl transition-colors duration-500" :style="{ color: textColor }">
              SkillSet AI
            </h3>
          </div>
          <p class="font-inter text-sm leading-relaxed transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Transforming education through universal accessibility.
          </p>
          <p class="font-inter text-sm leading-relaxed mt-3 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Making learning accessible for everyone, everywhere.
          </p>
        </div>

        <!-- Quick Links -->
        <nav aria-label="Quick Links">
          <h3 class="font-sora font-bold text-lg mb-4 transition-colors duration-500" :style="{ color: textColor }">
            Quick Links
          </h3>
          <ul class="space-y-3">
            <li v-for="link in quickLinks" :key="link.name">
              <router-link
                :to="link.to"
                class="font-inter text-sm inline-flex items-center gap-2 transition-all duration-300 hover:translate-x-1 focus:outline-none focus:ring-2 focus:ring-offset-2 min-h-[44px] py-2"
                :style="{ color: secondaryTextColor }"
                :aria-label="link.ariaLabel"
                @mouseenter="link.hover = true"
                @mouseleave="link.hover = false"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9 18l6-6-6-6" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                {{ link.name }}
              </router-link>
            </li>
          </ul>
        </nav>

        <!-- Contact Info -->
        <address class="not-italic">
          <h3 class="font-sora font-bold text-lg mb-4 transition-colors duration-500" :style="{ color: textColor }">
            Contact Us
          </h3>
          <div class="space-y-3">
            <a
              href="mailto:skillsetai.cw@gmail.com"
              class="font-inter text-sm flex items-center gap-3 transition-all duration-300 hover:translate-x-1 focus:outline-none focus:ring-2 focus:ring-offset-2 min-h-[44px] py-2"
              :style="{ color: secondaryTextColor }"
              aria-label="Email us at skillsetai.cw@gmail.com"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M22 6l-10 7L2 6" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              skillsetai.cw@gmail.com
            </a>
          </div>
        </address>

        <!-- Legal & Resources -->
        <nav aria-label="Legal and Resources">
          <h3 class="font-sora font-bold text-lg mb-4 transition-colors duration-500" :style="{ color: textColor }">
            Legal & Resources
          </h3>
          <ul class="space-y-3">
            <li v-for="link in legalLinks" :key="link.name">
              <router-link
                :to="link.to"
                class="font-inter text-sm inline-flex items-center gap-2 transition-all duration-300 hover:translate-x-1 focus:outline-none focus:ring-2 focus:ring-offset-2 min-h-[44px] py-2"
                :style="{ color: secondaryTextColor }"
                :aria-label="link.ariaLabel"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9 18l6-6-6-6" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                {{ link.name }}
              </router-link>
            </li>
          </ul>
        </nav>
      </div>

      <!-- Divider -->
      <div class="w-full h-px mb-8 transition-colors duration-500"
        :style="{ background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)' }">
      </div>

      <!-- Copyright & Bottom Section -->
      <div class="flex flex-col md:flex-row justify-between items-center gap-6">
        <p class="font-inter text-sm text-center md:text-left transition-colors duration-500" :style="{ color: secondaryTextColor }">
          © 2025 SkillSet AI. All rights reserved.
        </p>
        
        <!-- Accessibility Statement -->
        <div class="flex items-center gap-2">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="12" cy="12" r="10" :stroke="textColor" stroke-width="2"/>
            <path d="M12 16v-4M12 8h.01" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
          <p class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Built with accessibility in mind
          </p>
        </div>

        <!-- Back to Top -->
        <button
          @click="scrollToTop"
          class="font-inter text-sm flex items-center gap-2 px-4 py-2 rounded-full transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-offset-2"
          :style="{
            background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
            color: textColor
          }"
          aria-label="Scroll back to top of page"
        >
          Back to Top
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M18 15l-6-6-6 6" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue'
import { useDark } from '@vueuse/core'

const isDark = useDark()

const textColor = computed(() => isDark.value ? '#ffffff' : '#000000')
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)')

const quickLinks = [
  { name: 'Home', to: '/', ariaLabel: 'Navigate to home page' },
  { name: 'Features', to: '/#features', ariaLabel: 'View platform features' },
  { name: 'Use Cases', to: '/#use-cases', ariaLabel: 'Explore use cases' },
  { name: 'Contact', to: '/#contact', ariaLabel: 'Contact us' }
]

const legalLinks = [
  { name: 'Privacy Policy', to: '/privacy', ariaLabel: 'Read our privacy policy' },
  { name: 'Terms of Service', to: '/terms', ariaLabel: 'Read our terms of service' },
  { name: 'Accessibility', to: '/accessibility', ariaLabel: 'View accessibility statement' },
  { name: 'Documentation', to: '/docs', ariaLabel: 'View documentation' }
]

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}
</script>

<style scoped>
/* Focus visible styles for accessibility */
a:focus-visible,
button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 4px;
}

/* High contrast mode support */
@media (prefers-contrast: high) {
  a, button {
    text-decoration: underline;
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
</style>
