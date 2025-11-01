<template>
  <section class="relative py-24 px-6 lg:px-12 overflow-hidden">
    <div class="max-w-5xl mx-auto">
      <!-- Title -->
      <BlurText
        text="LOVED BY LEARNERS"
        :delay="100"
        animateBy="words"
        direction="top"
        as="h2"
        className="font-sora font-extrabold text-4xl md:text-5xl lg:text-6xl text-center mb-4 uppercase tracking-wide transition-colors duration-500"
        :style="{ color: textColor }"
      />

      <BlurText
        text="See what our community has to say about transforming their learning experience"
        :delay="80"
        animateBy="words"
        direction="top"
        as="p"
        className="text-center mb-16 max-w-2xl mx-auto transition-colors duration-500"
        :style="{ color: secondaryTextColor }"
      />

      <!-- Carousel -->
      <div class="relative h-80 flex items-center justify-center">
        <TransitionGroup name="slide">
          <div
            v-show="index === currentIndex"
            :key="testimonial.id"
            class="absolute w-full max-w-3xl"
            v-for="(testimonial, index) in testimonials"
          >
            <div
              class="rounded-3xl p-8 md:p-12 shadow-2xl transition-all duration-500"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(255, 255, 255, 0.5)',
                backdropFilter: 'blur(20px)',
                border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.15)'}`
              }"
            >
              <!-- Quote -->
              <p class="text-lg md:text-xl leading-relaxed mb-8 italic transition-colors duration-500" :style="{ color: textColor }">
                "{{ testimonial.quote }}"
              </p>

              <!-- Author -->
              <div class="flex items-center gap-4">
                <!-- Avatar -->
                <div class="w-14 h-14 rounded-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center text-white font-bold text-lg">
                  {{ testimonial.avatar }}
                </div>
                
                <!-- Info -->
                <div>
                  <div class="font-semibold text-lg transition-colors duration-500" :style="{ color: textColor }">
                    {{ testimonial.name }}
                  </div>
                  <div class="text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
                    {{ testimonial.role }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </TransitionGroup>

        <!-- Navigation Arrows -->
        <button
          @click="paginate(-1)"
          class="absolute left-0 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full backdrop-blur-sm flex items-center justify-center hover:bg-white/20 transition-all z-10"
          :style="{ 
            background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(255, 255, 255, 0.5)', 
            border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.15)'}`,
            color: textColor
          }"
        >
          ←
        </button>
        <button
          @click="paginate(1)"
          class="absolute right-0 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full backdrop-blur-sm flex items-center justify-center hover:bg-white/20 transition-all z-10"
          :style="{ 
            background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(255, 255, 255, 0.5)', 
            border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.15)'}`,
            color: textColor
          }"
        >
          →
        </button>
      </div>

      <!-- Dots Indicator -->
      <div class="flex justify-center gap-2 mt-8">
        <button
          v-for="(_, index) in testimonials"
          :key="index"
          @click="goToSlide(index)"
          class="h-2 rounded-full transition-all"
          :style="{ 
            background: index === currentIndex 
              ? textColor 
              : (isDark ? 'rgba(255, 255, 255, 0.3)' : 'rgba(0, 0, 0, 0.3)'),
            width: index === currentIndex ? '32px' : '8px'
          }"
        />
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useDark } from '@vueuse/core'
import BlurText from './BlurText.vue'

const isDark = useDark()
const textColor = computed(() => isDark.value ? '#ffffff' : '#000000')
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)')

const testimonials = [
  {
    id: 1,
    name: "Sarah Chen",
    role: "Graduate Student",
    quote: "SkillSet AI transformed my research papers into digestible summaries. I can finally keep up with my reading list!",
    avatar: "SC"
  },
  {
    id: 2,
    name: "Marcus Johnson",
    role: "High School Teacher",
    quote: "My students with dyslexia can now access the same materials as everyone else. This is truly inclusive education.",
    avatar: "MJ"
  },
  {
    id: 3,
    name: "Dr. Emily Rodriguez",
    role: "Accessibility Researcher",
    quote: "The accuracy is impressive. It simplifies without losing the essential meaning—exactly what we need.",
    avatar: "ER"
  },
  {
    id: 4,
    name: "Alex Thompson",
    role: "Software Engineer",
    quote: "I use it for technical documentation. It makes complex concepts clear without dumbing them down.",
    avatar: "AT"
  }
]

const currentIndex = ref(0)
let intervalId = null

const paginate = (direction) => {
  let next = currentIndex.value + direction
  if (next < 0) next = testimonials.length - 1
  if (next >= testimonials.length) next = 0
  currentIndex.value = next
}

const goToSlide = (index) => {
  currentIndex.value = index
}

onMounted(() => {
  intervalId = setInterval(() => {
    paginate(1)
  }, 5000)
})

onUnmounted(() => {
  if (intervalId) {
    clearInterval(intervalId)
  }
})
</script>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: all 0.5s ease;
}

.slide-enter-from {
  opacity: 0;
  transform: translateX(100px) scale(0.8);
  filter: blur(10px);
}

.slide-leave-to {
  opacity: 0;
  transform: translateX(-100px) scale(0.8);
  filter: blur(10px);
}
</style>
