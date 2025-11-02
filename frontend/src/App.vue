<template>
  <div id="app" :class="{ dark: themeStore.isDark }">
    <RouterView />
    <ScrollToTop />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useThemeStore } from './stores/theme';
import { useAuthStore } from './stores/auth';
import ScrollToTop from './components/ScrollToTop.vue';

const themeStore = useThemeStore();
const authStore = useAuthStore();

onMounted(() => {
  themeStore.initialize();
  authStore.initialize();
});
</script>

<style>
#app {
  min-height: 100vh;
  transition: background-color 0.3s ease;
}
</style>
