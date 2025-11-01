<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50 dark:from-gray-900 dark:via-gray-900 dark:to-purple-900">
    <!-- Navigation -->
    <nav class="fixed top-0 left-0 right-0 z-50 bg-white/80 dark:bg-gray-900/80 backdrop-blur-lg border-b border-gray-200 dark:border-gray-800">
      <div class="container mx-auto px-6 py-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
                        <div class="h-10 w-10 rounded-full bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center text-white font-bold">
              S
            </div>
            <span class="text-xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
              SkillSet AI
            </span>
          </div>
          <div class="flex items-center space-x-4">
            <router-link to="/login" class="text-gray-700 dark:text-gray-300 hover:text-primary-600 dark:hover:text-primary-400 transition-colors font-medium">
              Sign In
            </router-link>
            <router-link to="/register" class="bg-gradient-to-r from-primary-600 to-accent-600 text-white px-6 py-2.5 rounded-lg hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200 font-medium">
              Get Started
            </router-link>
          </div>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="pt-32 pb-20 px-6">
      <div class="container mx-auto max-w-6xl">
        <div class="text-center animate-fade-in">
          <h1 class="text-5xl md:text-7xl font-bold mb-6 bg-gradient-to-r from-primary-600 via-accent-600 to-primary-600 bg-clip-text text-transparent leading-tight">
            Transform Learning Materials
            <br />
            <span class="text-4xl md:text-6xl">For Everyone</span>
          </h1>
          <p class="text-xl md:text-2xl text-gray-600 dark:text-gray-300 mb-10 max-w-3xl mx-auto leading-relaxed">
            Make any study material truly accessible with AI-powered simplification, text-to-speech, dyslexia-friendly fonts, and more.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <router-link to="/register" class="group bg-gradient-to-r from-primary-600 to-accent-600 text-white px-8 py-4 rounded-xl text-lg font-semibold hover:shadow-2xl transform hover:-translate-y-1 transition-all duration-200 flex items-center space-x-2">
              <span>Start Free Today</span>
              <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </router-link>
            <button @click="scrollToFeatures" class="bg-white dark:bg-gray-800 text-gray-800 dark:text-gray-200 px-8 py-4 rounded-xl text-lg font-semibold border-2 border-gray-200 dark:border-gray-700 hover:border-primary-500 transition-all duration-200">
              Learn More
            </button>
          </div>
        </div>

        <!-- Feature Cards Preview -->
        <div class="mt-20 grid md:grid-cols-3 gap-6 animate-slide-up">
          <div class="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 border border-gray-100 dark:border-gray-700">
            <div class="w-12 h-12 bg-blue-100 dark:bg-blue-900 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-7 h-7 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-2 text-gray-900 dark:text-white">AI Text Simplification</h3>
            <p class="text-gray-600 dark:text-gray-300">Complex text transformed to any reading level while preserving meaning</p>
          </div>

          <div class="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 border border-gray-100 dark:border-gray-700">
            <div class="w-12 h-12 bg-purple-100 dark:bg-purple-900 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-7 h-7 text-purple-600 dark:text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15.536a5 5 0 001.414 1.414m2.828-9.9a9 9 0 000 12.728" />
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-2 text-gray-900 dark:text-white">Text-to-Speech</h3>
            <p class="text-gray-600 dark:text-gray-300">Natural-sounding audio narration with adjustable speed and voice</p>
          </div>

          <div class="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300 border border-gray-100 dark:border-gray-700">
            <div class="w-12 h-12 bg-green-100 dark:bg-green-900 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-7 h-7 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-2 text-gray-900 dark:text-white">Image Descriptions</h3>
            <p class="text-gray-600 dark:text-gray-300">Automatic alt-text generation for all images and diagrams</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section ref="featuresSection" class="py-20 bg-white dark:bg-gray-800">
      <div class="container mx-auto px-6 max-w-6xl">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-bold mb-4 text-gray-900 dark:text-white">Powerful Accessibility Features</h2>
          <p class="text-xl text-gray-600 dark:text-gray-300">Everything you need to make learning materials truly inclusive</p>
        </div>

        <div class="grid md:grid-cols-2 gap-8">
          <div class="flex items-start space-x-4 p-6 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors">
            <div class="flex-shrink-0 w-10 h-10 bg-indigo-100 dark:bg-indigo-900 rounded-lg flex items-center justify-center">
              <svg class="w-6 h-6 text-indigo-600 dark:text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
            </div>
            <div>
              <h3 class="text-xl font-semibold mb-2 text-gray-900 dark:text-white">Drag & Drop Upload</h3>
              <p class="text-gray-600 dark:text-gray-300">Upload PDFs, Word docs, PowerPoint, or paste URLs—we handle the rest</p>
            </div>
          </div>

          <div class="flex items-start space-x-4 p-6 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors">
            <div class="flex-shrink-0 w-10 h-10 bg-pink-100 dark:bg-pink-900 rounded-lg flex items-center justify-center">
              <svg class="w-6 h-6 text-pink-600 dark:text-pink-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
              </svg>
            </div>
            <div>
              <h3 class="text-xl font-semibold mb-2 text-gray-900 dark:text-white">Dyslexia-Friendly Fonts</h3>
              <p class="text-gray-600 dark:text-gray-300">Switch to OpenDyslexic font with optimized spacing instantly</p>
            </div>
          </div>

          <div class="flex items-start space-x-4 p-6 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors">
            <div class="flex-shrink-0 w-10 h-10 bg-yellow-100 dark:bg-yellow-900 rounded-lg flex items-center justify-center">
              <svg class="w-6 h-6 text-yellow-600 dark:text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
            </div>
            <div>
              <h3 class="text-xl font-semibold mb-2 text-gray-900 dark:text-white">Adaptive Contrast</h3>
              <p class="text-gray-600 dark:text-gray-300">Automatic color adjustments for low-vision users meeting WCAG standards</p>
            </div>
          </div>

          <div class="flex items-start space-x-4 p-6 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors">
            <div class="flex-shrink-0 w-10 h-10 bg-red-100 dark:bg-red-900 rounded-lg flex items-center justify-center">
              <svg class="w-6 h-6 text-red-600 dark:text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
            </div>
            <div>
              <h3 class="text-xl font-semibold mb-2 text-gray-900 dark:text-white">Math Equation Simplification</h3>
              <p class="text-gray-600 dark:text-gray-300">LaTeX equations explained step-by-step in plain language with audio</p>
            </div>
          </div>

          <div class="flex items-start space-x-4 p-6 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors">
            <div class="flex-shrink-0 w-10 h-10 bg-teal-100 dark:bg-teal-900 rounded-lg flex items-center justify-center">
              <svg class="w-6 h-6 text-teal-600 dark:text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <div>
              <h3 class="text-xl font-semibold mb-2 text-gray-900 dark:text-white">Diagram Descriptions</h3>
              <p class="text-gray-600 dark:text-gray-300">Flowcharts and chemistry diagrams converted to text summaries</p>
            </div>
          </div>

          <div class="flex items-start space-x-4 p-6 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors">
            <div class="flex-shrink-0 w-10 h-10 bg-orange-100 dark:bg-orange-900 rounded-lg flex items-center justify-center">
              <svg class="w-6 h-6 text-orange-600 dark:text-orange-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
              </svg>
            </div>
            <div>
              <h3 class="text-xl font-semibold mb-2 text-gray-900 dark:text-white">AI-Powered Everything</h3>
              <p class="text-gray-600 dark:text-gray-300">Gemini AI ensures high-quality, contextual adaptations</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 bg-gradient-to-r from-primary-600 to-accent-600">
      <div class="container mx-auto px-6 text-center">
        <h2 class="text-4xl md:text-5xl font-bold text-white mb-6">Ready to Transform Your Learning?</h2>
        <p class="text-xl text-white/90 mb-8 max-w-2xl mx-auto">Join thousands making education accessible for everyone</p>
        <router-link to="/register" class="inline-block bg-white text-primary-600 px-8 py-4 rounded-xl text-lg font-semibold hover:shadow-2xl transform hover:-translate-y-1 transition-all duration-200">
          Get Started Free
        </router-link>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-12">
      <div class="container mx-auto px-6 text-center">
        <div class="flex items-center justify-center space-x-3 mb-4">
          <div class="w-10 h-10 bg-gradient-to-br from-primary-500 to-accent-500 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
          </div>
          <span class="text-2xl font-bold">AccessiLearn</span>
        </div>
        <p class="text-gray-400">Making education accessible for everyone, everywhere</p>
        <p class="text-gray-500 mt-4">&copy; 2025 AccessiLearn. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const featuresSection = ref(null);

const scrollToFeatures = () => {
  featuresSection.value?.scrollIntoView({ behavior: 'smooth' });
};
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fadeIn 0.8s ease-out;
}

.animate-slide-up {
  animation: fadeIn 1s ease-out 0.2s both;
}
</style>
