<template>
  <div class="max-w-4xl mx-auto py-8 px-4">
    <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-2xl overflow-hidden">
      <!-- Header -->
      <div class="bg-gradient-to-r from-cyan-500 via-blue-500 to-purple-600 px-8 py-12 text-white">
        <h1 class="text-4xl font-bold mb-3">📋 Tell us about your needs</h1>
        <p class="text-lg opacity-90">
          Help us personalize your learning experience with AI-powered content adaptation
        </p>
      </div>

      <!-- Form -->
      <form @submit.prevent="submitSurvey" class="px-8 py-10 space-y-8">
        
        <!-- Preferred Reading Level -->
        <div class="space-y-3">
          <label class="block text-lg font-semibold text-gray-800 dark:text-white">
            Preferred Reading Level
          </label>
          <p class="text-sm text-gray-600 dark:text-gray-400">
            We'll simplify all content to match your preferred comprehension level
          </p>
          <select 
            v-model="survey.readingLevel" 
            required
            class="w-full px-5 py-4 text-lg rounded-xl border-2 border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-4 focus:ring-blue-500/50 focus:border-blue-500 transition-all"
          >
            <option value="">Select reading level...</option>
            <option value="very-simple">Very Simple (5th grade level) - Easiest to understand</option>
            <option value="simple">Simple (8th grade level) - Clear and straightforward</option>
            <option value="medium">Medium (10th grade level) - Standard comprehension</option>
          </select>
        </div>

        <!-- Accessibility Features -->
        <div class="space-y-3">
          <label class="block text-lg font-semibold text-gray-800 dark:text-white">
            Accessibility Features (Select all that apply)
          </label>
          <p class="text-sm text-gray-600 dark:text-gray-400">
            Choose features that will help you learn better
          </p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <label class="flex items-center gap-4 p-5 rounded-xl border-2 border-gray-200 dark:border-gray-700 hover:border-blue-500 dark:hover:border-blue-500 cursor-pointer transition-all"
              :class="{'border-blue-500 bg-blue-50 dark:bg-blue-900/20': survey.features.textToSpeech}">
              <input 
                type="checkbox" 
                v-model="survey.features.textToSpeech" 
                class="w-6 h-6 rounded text-blue-500 focus:ring-blue-500"
              >
              <div>
                <span class="text-3xl">🔊</span>
                <p class="font-semibold text-gray-800 dark:text-white">Text-to-Speech</p>
                <p class="text-sm text-gray-600 dark:text-gray-400">Listen to content read aloud</p>
              </div>
            </label>

            <label class="flex items-center gap-4 p-5 rounded-xl border-2 border-gray-200 dark:border-gray-700 hover:border-blue-500 dark:hover:border-blue-500 cursor-pointer transition-all"
              :class="{'border-blue-500 bg-blue-50 dark:bg-blue-900/20': survey.features.dyslexiaFont}">
              <input 
                type="checkbox" 
                v-model="survey.features.dyslexiaFont" 
                class="w-6 h-6 rounded text-blue-500 focus:ring-blue-500"
              >
              <div>
                <span class="text-3xl">📖</span>
                <p class="font-semibold text-gray-800 dark:text-white">Dyslexia-Friendly Font</p>
                <p class="text-sm text-gray-600 dark:text-gray-400">Easier to read text</p>
              </div>
            </label>

            <label class="flex items-center gap-4 p-5 rounded-xl border-2 border-gray-200 dark:border-gray-700 hover:border-blue-500 dark:hover:border-blue-500 cursor-pointer transition-all"
              :class="{'border-blue-500 bg-blue-50 dark:bg-blue-900/20': survey.features.highContrast}">
              <input 
                type="checkbox" 
                v-model="survey.features.highContrast" 
                class="w-6 h-6 rounded text-blue-500 focus:ring-blue-500"
              >
              <div>
                <span class="text-3xl">🎨</span>
                <p class="font-semibold text-gray-800 dark:text-white">High Contrast Mode</p>
                <p class="text-sm text-gray-600 dark:text-gray-400">Better visibility</p>
              </div>
            </label>

            <label class="flex items-center gap-4 p-5 rounded-xl border-2 border-gray-200 dark:border-gray-700 hover:border-blue-500 dark:hover:border-blue-500 cursor-pointer transition-all"
              :class="{'border-blue-500 bg-blue-50 dark:bg-blue-900/20': survey.features.imageDescriptions}">
              <input 
                type="checkbox" 
                v-model="survey.features.imageDescriptions" 
                class="w-6 h-6 rounded text-blue-500 focus:ring-blue-500"
              >
              <div>
                <span class="text-3xl">🖼️</span>
                <p class="font-semibold text-gray-800 dark:text-white">Image Descriptions</p>
                <p class="text-sm text-gray-600 dark:text-gray-400">AI-generated alt text</p>
              </div>
            </label>
          </div>
        </div>

        <!-- Content Type -->
        <div class="space-y-3">
          <label class="block text-lg font-semibold text-gray-800 dark:text-white">
            What type of content are you processing?
          </label>
          <p class="text-sm text-gray-600 dark:text-gray-400">
            This helps us optimize processing for your specific needs
          </p>
          <select 
            v-model="survey.contentType" 
            required
            class="w-full px-5 py-4 text-lg rounded-xl border-2 border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-4 focus:ring-blue-500/50 focus:border-blue-500 transition-all"
          >
            <option value="">Select content type...</option>
            <option value="educational">📚 Educational Material (Textbooks, lessons)</option>
            <option value="article">📰 Article/Blog Post (News, online articles)</option>
            <option value="research">🔬 Research Paper (Academic, scientific)</option>
            <option value="book">📕 Book Chapter (Fiction or non-fiction)</option>
            <option value="technical">⚙️ Technical Documentation (Manuals, guides)</option>
            <option value="other">📄 Other</option>
          </select>
        </div>

        <!-- Learning Goals -->
        <div class="space-y-3">
          <label class="block text-lg font-semibold text-gray-800 dark:text-white">
            What's your learning goal?
          </label>
          <p class="text-sm text-gray-600 dark:text-gray-400">
            Tell us what you want to achieve - we'll generate flashcards, notes, and summaries tailored to your goal
          </p>
          <textarea
            v-model="survey.learningGoal"
            rows="4"
            required
            maxlength="500"
            placeholder="Example: I want to understand the main concepts for my biology exam next week, focusing on cell structure and photosynthesis..."
            class="w-full px-5 py-4 text-lg rounded-xl border-2 border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white placeholder-gray-400 focus:ring-4 focus:ring-blue-500/50 focus:border-blue-500 transition-all resize-none"
          ></textarea>
          <p class="text-xs text-gray-500 dark:text-gray-500">
            {{ survey.learningGoal.length }} / 500 characters
          </p>
        </div>

        <!-- Learning Style (Optional) -->
        <div class="space-y-3">
          <label class="block text-lg font-semibold text-gray-800 dark:text-white">
            How do you learn best? (Optional)
          </label>
          <p class="text-sm text-gray-600 dark:text-gray-400">
            We'll adapt content format to match your learning style
          </p>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <label class="flex flex-col items-center gap-3 p-5 rounded-xl border-2 border-gray-200 dark:border-gray-700 hover:border-blue-500 dark:hover:border-blue-500 cursor-pointer transition-all"
              :class="{'border-blue-500 bg-blue-50 dark:bg-blue-900/20': survey.learningStyle === 'visual'}">
              <input 
                type="radio" 
                v-model="survey.learningStyle" 
                value="visual"
                class="w-5 h-5 text-blue-500 focus:ring-blue-500"
              >
              <span class="text-4xl">👁️</span>
              <p class="font-semibold text-center text-gray-800 dark:text-white">Visual</p>
              <p class="text-xs text-center text-gray-600 dark:text-gray-400">Diagrams, charts, images</p>
            </label>

            <label class="flex flex-col items-center gap-3 p-5 rounded-xl border-2 border-gray-200 dark:border-gray-700 hover:border-blue-500 dark:hover:border-blue-500 cursor-pointer transition-all"
              :class="{'border-blue-500 bg-blue-50 dark:bg-blue-900/20': survey.learningStyle === 'reading'}">
              <input 
                type="radio" 
                v-model="survey.learningStyle" 
                value="reading"
                class="w-5 h-5 text-blue-500 focus:ring-blue-500"
              >
              <span class="text-4xl">📚</span>
              <p class="font-semibold text-center text-gray-800 dark:text-white">Reading/Writing</p>
              <p class="text-xs text-center text-gray-600 dark:text-gray-400">Text-based, notes</p>
            </label>

            <label class="flex flex-col items-center gap-3 p-5 rounded-xl border-2 border-gray-200 dark:border-gray-700 hover:border-blue-500 dark:hover:border-blue-500 cursor-pointer transition-all"
              :class="{'border-blue-500 bg-blue-50 dark:bg-blue-900/20': survey.learningStyle === 'kinesthetic'}">
              <input 
                type="radio" 
                v-model="survey.learningStyle" 
                value="kinesthetic"
                class="w-5 h-5 text-blue-500 focus:ring-blue-500"
              >
              <span class="text-4xl">✋</span>
              <p class="font-semibold text-center text-gray-800 dark:text-white">Kinesthetic</p>
              <p class="text-xs text-center text-gray-600 dark:text-gray-400">Hands-on, examples</p>
            </label>
          </div>
        </div>

        <!-- Error Message -->
        <div v-if="error" class="p-4 bg-red-100 dark:bg-red-900/30 border-2 border-red-500 rounded-xl">
          <p class="text-red-700 dark:text-red-300">{{ error }}</p>
        </div>

        <!-- Submit Button -->
        <div class="flex gap-4 pt-6">
          <button
            type="submit"
            :disabled="saving"
            class="flex-1 px-8 py-5 bg-gradient-to-r from-cyan-500 via-blue-500 to-purple-600 text-white text-xl font-bold rounded-xl shadow-lg hover:shadow-xl transform hover:scale-[1.02] transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-3"
          >
            <svg v-if="saving" class="w-6 h-6 animate-spin" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <span v-if="saving">Saving Preferences...</span>
            <span v-else>Save & Continue to Upload →</span>
          </button>
        </div>

        <p class="text-sm text-center text-gray-500 dark:text-gray-400">
          You can update these preferences anytime in Settings
        </p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import databaseService from '../services/database.service';

const router = useRouter();
const authStore = useAuthStore();

const saving = ref(false);
const error = ref('');

const survey = reactive({
  readingLevel: '',
  features: {
    textToSpeech: false,
    dyslexiaFont: false,
    highContrast: false,
    imageDescriptions: false
  },
  contentType: '',
  learningGoal: '',
  learningStyle: ''
});

onMounted(async () => {
  // Check if user already completed survey
  if (authStore.user?.surveyData) {
    Object.assign(survey, authStore.user.surveyData);
  }
});

const submitSurvey = async () => {
  try {
    error.value = '';
    
    // Validate
    if (!survey.readingLevel) {
      error.value = 'Please select a reading level';
      return;
    }
    
    if (!survey.contentType) {
      error.value = 'Please select a content type';
      return;
    }
    
    if (!survey.learningGoal || survey.learningGoal.trim().length < 10) {
      error.value = 'Please provide a detailed learning goal (at least 10 characters)';
      return;
    }
    
    saving.value = true;
    
    // Save survey data to user profile
    await databaseService.updateUserSurvey(authStore.user.uid, {
      ...survey,
      completedAt: new Date().toISOString()
    });
    
    // Update auth store
    authStore.user.surveyData = survey;
    authStore.user.surveyCompleted = true;
    
    // Success!
    alert('✅ Preferences saved! You can now upload and process files.');
    router.push('/dashboard/upload');
    
  } catch (err) {
    console.error('Survey save error:', err);
    error.value = 'Failed to save preferences. Please try again.';
  } finally {
    saving.value = false;
  }
};
</script>

<style scoped>
/* Add custom checkbox/radio styling if needed */
</style>
