<template>
  <div class="relative w-full min-h-screen overflow-x-hidden">
    <!-- Background Effects - Same as Landing Page -->
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
      <!-- Navbar - Same as Landing Page -->
      <div class="fixed top-0 left-0 right-0 z-20 flex justify-center pt-6 px-6">
        <nav class="w-full max-w-7xl">
          <div 
            class="backdrop-blur-2xl rounded-full px-8 py-4 flex items-center justify-between shadow-xl transition-colors duration-500"
            :style="{
              background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
              borderColor: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.15)',
              border: '1px solid',
              boxShadow: isDark ? '0 8px 32px rgba(0, 0, 0, 0.3)' : '0 8px 32px rgba(0, 0, 0, 0.1)'
            }"
          >
            <!-- Logo - Same as Landing Page -->
            <router-link to="/dashboard" class="font-sora font-bold text-lg flex items-center gap-2 transition-colors duration-500" :style="{ color: textColor }">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2L2 7L12 12L22 7L12 2Z" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M2 17L12 22L22 17" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M2 12L12 17L22 12" :stroke="textColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
              SkillSet AI
            </router-link>

            <!-- Navigation Links + Actions -->
            <div class="flex items-center gap-6">
              <!-- Horizontal Navigation Links -->
              <router-link
                v-for="item in navigation"
                :key="item.name"
                :to="item.to"
                class="font-inter text-sm font-medium transition-all hover:opacity-70 hidden lg:block"
                :class="{ 'font-bold': route.path === item.to }"
                :style="{ color: textColor }"
              >
                {{ item.name }}
              </router-link>

              <!-- User Menu Dropdown -->
              <div class="relative" ref="userMenuRef">
                <button
                  @click="toggleUserMenu"
                  class="flex items-center gap-2 px-4 py-2 rounded-full transition-all duration-300 hover:scale-105"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                    border: `1px solid ${isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)'}`
                  }"
                >
                  <div class="w-8 h-8 rounded-full flex items-center justify-center font-sora font-bold text-sm"
                    :style="{
                      background: isDark ? '#ffffff' : '#000000',
                      color: isDark ? '#000000' : '#ffffff'
                    }">
                    {{ currentUser?.displayName?.charAt(0) || currentUser?.email?.charAt(0) || 'U' }}
                  </div>
                  <span class="font-inter text-sm font-medium hidden md:block" :style="{ color: textColor }">
                    {{ currentUser?.displayName?.split(' ')[0] || 'User' }}
                  </span>
                </button>

                <!-- Dropdown Menu -->
                <Transition name="fade-scale">
                  <div
                    v-if="userMenuOpen"
                    class="absolute right-0 mt-2 w-64 rounded-2xl shadow-2xl overflow-hidden"
                    :style="{
                      background: isDark ? 'rgba(0, 0, 0, 0.9)' : 'rgba(255, 255, 255, 0.95)',
                      backdropFilter: 'blur(20px)',
                      border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
                    }"
                  >
                    <!-- User Info -->
                    <div class="p-4 border-b" :style="{ borderColor: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)' }">
                      <p class="font-sora font-bold text-sm" :style="{ color: textColor }">
                        {{ currentUser?.displayName || 'Guest User' }}
                      </p>
                      <p class="font-inter text-xs mt-1" :style="{ color: secondaryTextColor }">
                        {{ currentUser?.email || 'demo@example.com' }}
                      </p>
                    </div>

                    <!-- Mobile Navigation Links -->
                    <div class="lg:hidden border-b" :style="{ borderColor: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)' }">
                      <router-link
                        v-for="item in navigation"
                        :key="item.name"
                        :to="item.to"
                        @click="closeUserMenu"
                        class="block px-4 py-3 font-inter text-sm font-medium transition-all hover:opacity-70"
                        :style="{ color: textColor }"
                      >
                        {{ item.name }}
                      </router-link>
                    </div>

                    <!-- Actions -->
                    <div class="p-2">
                      <router-link
                        to="/dashboard/settings"
                        @click="closeUserMenu"
                        class="flex items-center gap-3 px-4 py-3 rounded-lg font-inter text-sm font-medium transition-all hover:opacity-70"
                        :style="{ color: textColor }"
                      >
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <circle cx="12" cy="12" r="3" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                          <path d="M12 1v6m0 6v6M5.64 5.64l4.24 4.24m4.24 4.24l4.24 4.24M1 12h6m6 0h6M5.64 18.36l4.24-4.24m4.24-4.24l4.24-4.24" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        Settings
                      </router-link>
                      <button
                        v-if="currentUser"
                        @click="handleLogout"
                        class="w-full flex items-center gap-3 px-4 py-3 rounded-lg font-inter text-sm font-medium transition-all hover:opacity-70"
                        :style="{ color: textColor }"
                      >
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        Logout
                      </button>
                    </div>
                  </div>
                </Transition>
              </div>

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

      <!-- Page Content -->
      <main class="relative pt-32 pb-8 px-6 min-h-screen flex flex-col">
        <div class="flex-1">
          <router-view />
        </div>
        
        <!-- Footer -->
        <div class="mt-auto pt-16">
          <Footer />
        </div>
      </main>
      
      <!-- Scroll to Top Button -->
      <ScrollToTop />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useDark } from '@vueuse/core'
import { useFirebaseAuth } from '../composables/useFirebaseAuth'
import DitherBackground from '../components/DitherBackground.vue'
import Iridescence from '../components/Iridescence.vue'
import Footer from '../components/Footer.vue'
import ScrollToTop from '../components/ScrollToTop.vue'

const router = useRouter()
const route = useRoute()
const { currentUser, logout } = useFirebaseAuth()

const isDark = useDark()
const userMenuOpen = ref(false)
const userMenuRef = ref(null)

const textColor = computed(() => isDark.value ? '#ffffff' : '#000000')
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)')

const toggleTheme = () => {
  isDark.value = !isDark.value
  console.log('Theme toggled, isDark:', isDark.value)
}

const toggleUserMenu = () => {
  userMenuOpen.value = !userMenuOpen.value
}

const closeUserMenu = () => {
  userMenuOpen.value = false
}

const handleLogout = async () => {
  const result = await logout()
  if (result.success) {
    closeUserMenu()
    router.push('/')
  }
}

// Close user menu when clicking outside
const handleClickOutside = (event) => {
  if (userMenuRef.value && !userMenuRef.value.contains(event.target)) {
    closeUserMenu()
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})

// Navigation items - horizontal
const navigation = [
  { name: 'Dashboard', to: '/dashboard' },
  { name: 'Upload', to: '/dashboard/upload' },
  { name: 'History', to: '/dashboard/history' },
  { name: 'Saved', to: '/dashboard/saved' },
  { name: 'Profile', to: '/dashboard/profile' }
]
</script>

<style scoped>
.fade-scale-enter-active,
.fade-scale-leave-active {
  transition: all 0.2s ease;
}

.fade-scale-enter-from,
.fade-scale-leave-to {
  opacity: 0;
  transform: scale(0.95) translateY(-10px);
}

.fade-scale-enter-to,
.fade-scale-leave-from {
  opacity: 1;
  transform: scale(1) translateY(0);
}
</style>
