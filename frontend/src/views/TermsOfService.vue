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
              Terms of Service
            </h1>
            
            <p class="font-inter text-sm mb-8 transition-colors duration-500" :style="{ color: secondaryTextColor }">
              Last updated: November 2, 2025
            </p>

            <div class="space-y-8 font-inter" :style="{ color: textColor }">
              <section>
                <h2 class="font-sora font-bold text-2xl mb-4">1. Acceptance of Terms</h2>
                <p class="leading-relaxed" :style="{ color: secondaryTextColor }">
                  By accessing and using SkillSet AI, you accept and agree to be bound by these Terms of Service. 
                  If you do not agree to these terms, please do not use our platform.
                </p>
              </section>

              <section>
                <h2 class="font-sora font-bold text-2xl mb-4">2. Use of Service</h2>
                <p class="leading-relaxed mb-3" :style="{ color: secondaryTextColor }">
                  You agree to use SkillSet AI only for lawful purposes and in accordance with these Terms. You agree not to:
                </p>
                <ul class="list-disc list-inside space-y-2 leading-relaxed" :style="{ color: secondaryTextColor }">
                  <li>Use the service in any way that violates any applicable law or regulation</li>
                  <li>Upload malicious content or code</li>
                  <li>Attempt to gain unauthorized access to our systems</li>
                  <li>Interfere with or disrupt the service</li>
                </ul>
              </section>

              <section>
                <h2 class="font-sora font-bold text-2xl mb-4">3. User Content</h2>
                <p class="leading-relaxed" :style="{ color: secondaryTextColor }">
                  You retain all rights to the content you upload. By uploading content, you grant us a license to process, 
                  store, and display your content as necessary to provide our services.
                </p>
              </section>

              <section>
                <h2 class="font-sora font-bold text-2xl mb-4">4. Intellectual Property</h2>
                <p class="leading-relaxed" :style="{ color: secondaryTextColor }">
                  The SkillSet AI platform, including its original content, features, and functionality, is owned by SkillSet AI 
                  and is protected by international copyright, trademark, and other intellectual property laws.
                </p>
              </section>

              <section>
                <h2 class="font-sora font-bold text-2xl mb-4">5. Limitation of Liability</h2>
                <p class="leading-relaxed" :style="{ color: secondaryTextColor }">
                  SkillSet AI shall not be liable for any indirect, incidental, special, consequential, or punitive damages 
                  resulting from your use or inability to use the service.
                </p>
              </section>

              <section>
                <h2 class="font-sora font-bold text-2xl mb-4">6. Contact Us</h2>
                <p class="leading-relaxed" :style="{ color: secondaryTextColor }">
                  If you have any questions about these Terms of Service, please contact us at 
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
