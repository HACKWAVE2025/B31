<template>
  <div class="relative w-full min-h-screen overflow-x-hidden">
    <!-- Background Effects - Same as Dashboard -->
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
    <div class="relative z-10 max-w-4xl mx-auto py-16 px-4">
      <div class="relative overflow-hidden rounded-3xl shadow-2xl transition-all duration-500"
        :style="{
          background: isDark 
            ? 'rgba(0, 0, 0, 0.6)'
            : 'rgba(255, 255, 255, 0.7)',
          backdropFilter: 'blur(20px)',
          border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
        }">
        
        <!-- Header -->
        <div class="px-8 py-12 border-b transition-colors duration-500"
          :style="{
            borderColor: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
          }">
          <h1 class="text-4xl font-bold mb-3 transition-colors duration-500"
            :style="{ color: textColor }">
            📋 Tell us about your needs
          </h1>
          <p class="text-lg transition-colors duration-500"
            :style="{ color: secondaryTextColor }">
            Help us personalize your learning experience with AI-powered content adaptation
          </p>
        </div>

        <!-- Form -->
        <form @submit.prevent="submitSurvey" class="px-8 py-10 space-y-8">
          
          <!-- Preferred Reading Level -->
          <div class="space-y-3">
            <label class="block text-lg font-semibold transition-colors duration-500"
              :style="{ color: textColor }">
              Preferred Reading Level
            </label>
            <p class="text-sm transition-colors duration-500"
              :style="{ color: secondaryTextColor }">
              We'll simplify all content to match your preferred comprehension level
            </p>
            <select 
              v-model="survey.readingLevel" 
              required
              class="w-full px-5 py-4 text-lg rounded-xl border-2 transition-all duration-500 focus:ring-4 focus:ring-white/20"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
                borderColor: isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)',
                color: textColor
              }"
            >
              <option value="">Select reading level...</option>
              <option value="very-simple">Very Simple (5th grade level) - Easiest to understand</option>
              <option value="simple">Simple (8th grade level) - Clear and straightforward</option>
              <option value="medium">Medium (10th grade level) - Standard comprehension</option>
            </select>
          </div>

          <!-- Accessibility Features -->
          <div class="space-y-3">
            <label class="block text-lg font-semibold transition-colors duration-500"
              :style="{ color: textColor }">
              Accessibility Features (Select all that apply)
            </label>
            <p class="text-sm transition-colors duration-500"
              :style="{ color: secondaryTextColor }">
              Choose features that will help you learn better
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <label class="flex items-center gap-4 p-5 rounded-xl border-2 cursor-pointer transition-all duration-500 hover:scale-105"
                :style="{
                  background: survey.features.textToSpeech ? (isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)') : 'transparent',
                  borderColor: survey.features.textToSpeech ? (isDark ? 'rgba(255, 255, 255, 0.4)' : 'rgba(0, 0, 0, 0.4)') : (isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)')
                }">
                <input 
                  type="checkbox" 
                  v-model="survey.features.textToSpeech" 
                  class="w-6 h-6 rounded focus:ring-white/20"
                >
                <div>
                  <span class="text-3xl">🔊</span>
                  <p class="font-semibold transition-colors duration-500"
                    :style="{ color: textColor }">Text-to-Speech</p>
                  <p class="text-sm transition-colors duration-500"
                    :style="{ color: secondaryTextColor }">Listen to content read aloud</p>
                </div>
              </label>

              <label class="flex items-center gap-4 p-5 rounded-xl border-2 cursor-pointer transition-all duration-500 hover:scale-105"
                :style="{
                  background: survey.features.dyslexiaFont ? (isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)') : 'transparent',
                  borderColor: survey.features.dyslexiaFont ? (isDark ? 'rgba(255, 255, 255, 0.4)' : 'rgba(0, 0, 0, 0.4)') : (isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)')
                }">
                <input 
                  type="checkbox" 
                  v-model="survey.features.dyslexiaFont" 
                  class="w-6 h-6 rounded focus:ring-white/20"
                >
                <div>
                  <span class="text-3xl">📖</span>
                  <p class="font-semibold transition-colors duration-500"
                    :style="{ color: textColor }">Dyslexia-Friendly Font</p>
                  <p class="text-sm transition-colors duration-500"
                    :style="{ color: secondaryTextColor }">Easier to read text</p>
                </div>
              </label>

              <label class="flex items-center gap-4 p-5 rounded-xl border-2 cursor-pointer transition-all duration-500 hover:scale-105"
                :style="{
                  background: survey.features.highContrast ? (isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)') : 'transparent',
                  borderColor: survey.features.highContrast ? (isDark ? 'rgba(255, 255, 255, 0.4)' : 'rgba(0, 0, 0, 0.4)') : (isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)')
                }">
                <input 
                  type="checkbox" 
                  v-model="survey.features.highContrast" 
                  class="w-6 h-6 rounded focus:ring-white/20"
                >
                <div>
                  <span class="text-3xl">🎨</span>
                  <p class="font-semibold transition-colors duration-500"
                    :style="{ color: textColor }">High Contrast Mode</p>
                  <p class="text-sm transition-colors duration-500"
                    :style="{ color: secondaryTextColor }">Better visibility</p>
                </div>
              </label>

              <label class="flex items-center gap-4 p-5 rounded-xl border-2 cursor-pointer transition-all duration-500 hover:scale-105"
                :style="{
                  background: survey.features.imageDescriptions ? (isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)') : 'transparent',
                  borderColor: survey.features.imageDescriptions ? (isDark ? 'rgba(255, 255, 255, 0.4)' : 'rgba(0, 0, 0, 0.4)') : (isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)')
                }">
                <input 
                  type="checkbox" 
                  v-model="survey.features.imageDescriptions" 
                  class="w-6 h-6 rounded focus:ring-white/20"
                >
                <div>
                  <span class="text-3xl">🖼️</span>
                  <p class="font-semibold transition-colors duration-500"
                    :style="{ color: textColor }">Image Descriptions</p>
                  <p class="text-sm transition-colors duration-500"
                    :style="{ color: secondaryTextColor }">AI-generated alt text</p>
                </div>
              </label>
            </div>
          </div>

        <!-- Content Type -->
        <div class="space-y-3">
          <label class="block text-lg font-semibold transition-colors duration-500"
            :style="{ color: textColor }">
            What type of content are you processing?
          </label>
          <p class="text-sm transition-colors duration-500"
            :style="{ color: secondaryTextColor }">
            This helps us optimize processing for your specific needs
          </p>
          <select 
            v-model="survey.contentType" 
            required
            class="w-full px-5 py-4 text-lg rounded-xl border-2 transition-all duration-500 focus:ring-4 focus:ring-white/20"
            :style="{
              background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
              borderColor: isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)',
              color: textColor
            }"
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
          <label class="block text-lg font-semibold transition-colors duration-500"
            :style="{ color: textColor }">
            What's your learning goal?
          </label>
          <p class="text-sm transition-colors duration-500"
            :style="{ color: secondaryTextColor }">
            Tell us what you want to achieve - we'll generate flashcards, notes, and summaries tailored to your goal
          </p>
          <textarea
            v-model="survey.learningGoal"
            rows="4"
            required
            maxlength="500"
            placeholder="Example: I want to understand the main concepts for my biology exam next week, focusing on cell structure and photosynthesis..."
            class="w-full px-5 py-4 text-lg rounded-xl border-2 transition-all duration-500 focus:ring-4 focus:ring-white/20 resize-none"
            :style="{
              background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
              borderColor: isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)',
              color: textColor
            }"
          ></textarea>
          <p class="text-xs transition-colors duration-500"
            :style="{ color: secondaryTextColor }">
            {{ survey.learningGoal.length }} / 500 characters
          </p>
        </div>

        <!-- Learning Style (Optional) -->
        <div class="space-y-3">
          <label class="block text-lg font-semibold transition-colors duration-500"
            :style="{ color: textColor }">
            How do you learn best? (Optional)
          </label>
          <p class="text-sm transition-colors duration-500"
            :style="{ color: secondaryTextColor }">
            We'll adapt content format to match your learning style
          </p>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <label class="flex flex-col items-center gap-3 p-5 rounded-xl border-2 cursor-pointer transition-all duration-500"
              :style="{
                borderColor: survey.learningStyle === 'visual' 
                  ? (isDark ? 'rgba(255, 255, 255, 0.8)' : 'rgba(0, 0, 0, 0.8)')
                  : (isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)'),
                background: survey.learningStyle === 'visual' 
                  ? (isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)')
                  : 'transparent'
              }">
              <input 
                type="radio" 
                v-model="survey.learningStyle" 
                value="visual"
                class="w-5 h-5 focus:ring-white/20"
              >
              <span class="text-4xl">👁️</span>
              <p class="font-semibold text-center transition-colors duration-500" :style="{ color: textColor }">Visual</p>
              <p class="text-xs text-center transition-colors duration-500" :style="{ color: secondaryTextColor }">Diagrams, charts, images</p>
            </label>

            <label class="flex flex-col items-center gap-3 p-5 rounded-xl border-2 cursor-pointer transition-all duration-500"
              :style="{
                borderColor: survey.learningStyle === 'reading' 
                  ? (isDark ? 'rgba(255, 255, 255, 0.8)' : 'rgba(0, 0, 0, 0.8)')
                  : (isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)'),
                background: survey.learningStyle === 'reading' 
                  ? (isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)')
                  : 'transparent'
              }">
              <input 
                type="radio" 
                v-model="survey.learningStyle" 
                value="reading"
                class="w-5 h-5 focus:ring-white/20"
              >
              <span class="text-4xl">📚</span>
              <p class="font-semibold text-center transition-colors duration-500" :style="{ color: textColor }">Reading/Writing</p>
              <p class="text-xs text-center transition-colors duration-500" :style="{ color: secondaryTextColor }">Text-based, notes</p>
            </label>

            <label class="flex flex-col items-center gap-3 p-5 rounded-xl border-2 cursor-pointer transition-all duration-500"
              :style="{
                borderColor: survey.learningStyle === 'kinesthetic' 
                  ? (isDark ? 'rgba(255, 255, 255, 0.8)' : 'rgba(0, 0, 0, 0.8)')
                  : (isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)'),
                background: survey.learningStyle === 'kinesthetic' 
                  ? (isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)')
                  : 'transparent'
              }">
              <input 
                type="radio" 
                v-model="survey.learningStyle" 
                value="kinesthetic"
                class="w-5 h-5 focus:ring-white/20"
              >
              <span class="text-4xl">✋</span>
              <p class="font-semibold text-center transition-colors duration-500" :style="{ color: textColor }">Kinesthetic</p>
              <p class="text-xs text-center transition-colors duration-500" :style="{ color: secondaryTextColor }">Hands-on, examples</p>
            </label>
          </div>
        </div>

        <!-- Error Message -->
        <div v-if="error" class="p-4 rounded-xl border-2 border-red-500"
          :style="{
            background: isDark ? 'rgba(239, 68, 68, 0.1)' : 'rgba(239, 68, 68, 0.1)',
            backdropFilter: 'blur(10px)'
          }">
          <p class="text-red-500 font-semibold">{{ error }}</p>
        </div>

        <!-- Submit Button -->
        <div class="flex gap-4 pt-6">
          <button
            type="submit"
            :disabled="saving"
            class="flex-1 px-8 py-5 text-white text-xl font-bold rounded-xl shadow-lg hover:shadow-xl transform hover:scale-[1.02] transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-3"
            :style="{
              background: isDark 
                ? 'linear-gradient(135deg, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0.05) 100%)'
                : 'linear-gradient(135deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.6) 100%)',
              backdropFilter: 'blur(20px)',
              border: isDark ? '2px solid rgba(255,255,255,0.3)' : '2px solid rgba(0,0,0,0.3)'
            }"
          >
            <svg v-if="saving" class="w-6 h-6 animate-spin" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <span v-if="saving">Saving Preferences...</span>
            <span v-else>Save & Continue to Upload →</span>
          </button>
        </div>

        <p class="text-sm text-center transition-colors duration-500"
          :style="{ color: secondaryTextColor }">
          You can update these preferences anytime in Settings
        </p>
      </form>
    </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useDark } from '@vueuse/core';
import { useAuthStore } from '../stores/auth';
import databaseService from '../services/database.service';
import DitherBackground from '../components/DitherBackground.vue';
import Iridescence from '../components/Iridescence.vue';

const router = useRouter();
const authStore = useAuthStore();
const isDark = useDark();

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

// Computed properties for colors
const textColor = computed(() => isDark.value ? '#ffffff' : '#000000');
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)');

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
