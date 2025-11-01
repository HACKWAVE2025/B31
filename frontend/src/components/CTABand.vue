<template>
  <section class="relative py-32 px-6 lg:px-12 overflow-hidden">
    <!-- Aurora Glow Background -->
    <div class="absolute inset-0 overflow-hidden">
      <div
        class="absolute inset-0 aurora-glow"
        :class="{ 'aurora-glow-animate': true }"
      />
    </div>

    <div class="max-w-4xl mx-auto text-center relative z-10">
      <!-- Glass Overlay Card -->
      <div
        class="rounded-3xl p-12 md:p-16 shadow-2xl relative overflow-hidden transition-all duration-500"
        :style="{
          background: isDark ? 'rgba(255, 255, 255, 0.03)' : 'rgba(255, 255, 255, 0.5)',
          backdropFilter: 'blur(20px)',
          border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.15)'}`
        }"
      >
        <!-- Heading -->
        <BlurText
          text="READY TO MAKE EVERY RESOURCE ACCESSIBLE?"
          :delay="80"
          animateBy="words"
          direction="top"
          as="h2"
          className="font-sora font-extrabold text-3xl md:text-4xl lg:text-5xl mb-8 leading-tight uppercase tracking-wide transition-colors duration-500"
          :style="{ color: textColor }"
        />

        <!-- Buttons -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
          <!-- Primary Button -->
          <button
            @click="$emit('openModal')"
            class="px-10 py-4 rounded-full font-inter font-bold text-black bg-white shadow-lg transition-all relative overflow-hidden group hover:scale-105"
          >
            <span class="relative z-10">Get Started</span>
            <div
              class="absolute inset-0 bg-gradient-to-r from-blue-400 to-purple-500 opacity-0 group-hover:opacity-20 transition-opacity"
            />
          </button>

          <!-- Secondary Button -->
          <button
            class="px-10 py-4 rounded-full font-inter font-bold border-2 transition-all relative overflow-hidden group hover:scale-105"
            :style="{
              color: textColor,
              background: 'transparent',
              borderColor: isDark ? 'rgba(6, 182, 212, 0.5)' : 'rgba(168, 85, 247, 0.5)'
            }"
          >
            <span class="relative z-10">Request Demo</span>
            <div
              class="absolute inset-0 bg-gradient-to-r from-blue-400/10 to-purple-500/10 opacity-0 group-hover:opacity-100 transition-opacity"
            />
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useDark } from '@vueuse/core'
import BlurText from './BlurText.vue'

defineEmits(['openModal'])

const isDark = useDark()
const textColor = computed(() => isDark.value ? '#ffffff' : '#000000')
</script>

<style scoped>
@keyframes aurora {
  0% {
    background: radial-gradient(circle at 20% 50%, rgba(6, 182, 212, 0.15) 0%, transparent 50%);
  }
  33% {
    background: radial-gradient(circle at 80% 50%, rgba(168, 85, 247, 0.15) 0%, transparent 50%);
  }
  66% {
    background: radial-gradient(circle at 50% 80%, rgba(6, 182, 212, 0.15) 0%, transparent 50%);
  }
  100% {
    background: radial-gradient(circle at 20% 50%, rgba(6, 182, 212, 0.15) 0%, transparent 50%);
  }
}

.aurora-glow-animate {
  animation: aurora 10s linear infinite;
}
</style>
