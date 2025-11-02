<template>
  <div class="relative w-full min-h-screen overflow-x-hidden">
    <!-- Background Effects -->
    <DitherBackground v-if="isDark" />
    <div v-else class="fixed top-0 left-0 w-full h-full z-0">
      <Iridescence
        :color="[1, 1, 1]"
        :mouseReact="true"
        :amplitude="0.1"
        :speed="1.0"
      />
    </div>

    <!-- Content -->
    <div class="relative z-10">
      <!-- Navbar -->
      <div class="fixed top-0 left-0 right-0 z-20 flex justify-center pt-6 px-6">
        <nav class="w-full max-w-7xl">
          <div 
            class="backdrop-blur-2xl rounded-full px-8 py-4 flex items-center justify-between shadow-xl transition-colors duration-500"
            :style="{
              background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
              borderColor: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.15)',
              border: '1px solid'
            }"
          >
            <router-link to="/" class="font-sora font-bold text-lg flex items-center gap-2" :style="{ color: textColor }">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                <path d="M12 2L2 7L12 12L22 7L12 2Z" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M2 17L12 22L22 17" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M2 12L12 17L22 12" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
              SkillSet AI
            </router-link>
          </div>
        </nav>
      </div>

      <!-- Main Content -->
      <main class="pt-32 pb-20 px-6 lg:px-12">
        <div class="max-w-4xl mx-auto">
          <div class="rounded-3xl p-10 lg:p-14 shadow-2xl transition-all duration-500"
            :style="{
              background: isDark 
                ? 'rgba(0, 0, 0, 0.6)'
                : 'rgba(255, 255, 255, 0.7)',
              backdropFilter: 'blur(20px)',
              border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
            }">
            
            <h1 class="font-sora font-extrabold text-4xl lg:text-5xl mb-6 transition-colors duration-500" :style="{ color: textColor }">
              Privacy Policy
            </h1>
            
            <p class="font-inter text-sm mb-8 transition-colors duration-500" :style="{ color: secondaryTextColor }">
              Last updated: November 2, 2025
            </p>

            <div class="space-y-8 font-inter" :style="{ color: textColor }">
              <section>
                <h2 class="font-sora font-bold text-2xl mb-4">1. Introduction</h2>
                <p class="leading-relaxed" :style="{ color: secondaryTextColor }">
                  At SkillSet AI, we are committed to protecting your privacy and ensuring the security of your personal information. 
                  This Privacy Policy explains how we collect, use, and safeguard your data when you use our platform.
                </p>
              </section>

              <section>
                <h2 class="font-sora font-bold text-2xl mb-4">2. Information We Collect</h2>
                <ul class="list-disc list-inside space-y-2 leading-relaxed" :style="{ color: secondaryTextColor }">
                  <li>Account information (name, email address)</li>
                  <li>Content you upload for processing</li>
                  <li>Usage data and analytics</li>
                  <li>Device and browser information</li>
                </ul>
              </section>

              <section>
                <h2 class="font-sora font-bold text-2xl mb-4">3. How We Use Your Information</h2>
                <p class="leading-relaxed" :style="{ color: secondaryTextColor }">
                  We use your information to provide and improve our services, process your requests, communicate with you, 
                  and ensure the security of our platform.
                </p>
              </section>

              <section>
                <h2 class="font-sora font-bold text-2xl mb-4">4. Data Security</h2>
                <p class="leading-relaxed" :style="{ color: secondaryTextColor }">
                  We implement industry-standard security measures to protect your data from unauthorized access, 
                  alteration, disclosure, or destruction.
                </p>
              </section>

              <section>
                <h2 class="font-sora font-bold text-2xl mb-4">5. Contact Us</h2>
                <p class="leading-relaxed" :style="{ color: secondaryTextColor }">
                  If you have any questions about this Privacy Policy, please contact us at 
                  <a href="mailto:skillsetai.cw@gmail.com" class="underline hover:opacity-70">skillsetai.cw@gmail.com</a>
                </p>
              </section>
            </div>
          </div>
        </div>
      </main>

      <!-- Footer -->
      <Footer />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useDark } from '@vueuse/core'
import DitherBackground from '../components/DitherBackground.vue'
import Iridescence from '../components/Iridescence.vue'
import Footer from '../components/Footer.vue'

const isDark = useDark()
const textColor = computed(() => isDark.value ? '#ffffff' : '#000000')
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)')
</script>
