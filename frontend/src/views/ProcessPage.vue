<template><template>

  <div class="max-w-7xl mx-auto">  <div class="max-w-4xl mx-auto">

    <h1 class="text-3xl font-bold text-gray-900 dark:text-white mb-8">Process Content</h1>    <h1 class="text-3xl font-bold mb-6">Processing Content</h1>

    <div class="bg-white dark:bg-gray-800 rounded-xl p-8 shadow-md">

    <!-- Step Indicator -->      <p>Processing interface - Coming soon!</p>

    <div class="mb-8">    </div>

      <div class="flex items-center justify-between">  </div>

        <div v-for="(step, index) in steps" :key="index" class="flex-1"></template>

          <div class="flex items-center">
            <div
              :class="[
                'w-10 h-10 rounded-full flex items-center justify-center font-semibold',
                currentStep > index
                  ? 'bg-green-500 text-white'
                  : currentStep === index
                  ? 'bg-gradient-to-r from-primary-500 to-accent-500 text-white'
                  : 'bg-gray-200 dark:bg-gray-700 text-gray-600 dark:text-gray-400'
              ]"
            >
              <span v-if="currentStep > index">✓</span>
              <span v-else>{{ index + 1 }}</span>
            </div>
            <div class="flex-1 h-1 mx-2" v-if="index < steps.length - 1">
              <div
                :class="[
                  'h-full transition-all duration-500',
                  currentStep > index ? 'bg-green-500' : 'bg-gray-200 dark:bg-gray-700'
                ]"
              ></div>
            </div>
          </div>
          <p class="text-xs mt-2 text-center font-medium">{{ step }}</p>
        </div>
      </div>
    </div>

    <!-- Step 1: Survey -->
    <div v-if="currentStep === 0" class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8 animate-fade-in">
      <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">📋 Tell us about your needs</h2>
      
      <div class="space-y-6">
        <!-- Reading Level -->
        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Preferred Reading Level
          </label>
          <select v-model="survey.readingLevel" class="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-primary-500">
            <option value="very-simple">Very Simple (5th grade level)</option>
            <option value="simple">Simple (8th grade level)</option>
            <option value="medium">Medium (10th grade level)</option>
          </select>
        </div>

        <!-- Accessibility Needs -->
        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            Accessibility Features (Select all that apply)
          </label>
          <div class="space-y-2">
            <label class="flex items-center">
              <input type="checkbox" v-model="survey.features.textToSpeech" class="rounded text-primary-500 mr-3">
              <span class="text-gray-700 dark:text-gray-300">🔊 Text-to-Speech</span>
            </label>
            <label class="flex items-center">
              <input type="checkbox" v-model="survey.features.dyslexiaFont" class="rounded text-primary-500 mr-3">
              <span class="text-gray-700 dark:text-gray-300">📖 Dyslexia-Friendly Font</span>
            </label>
            <label class="flex items-center">
              <input type="checkbox" v-model="survey.features.highContrast" class="rounded text-primary-500 mr-3">
              <span class="text-gray-700 dark:text-gray-300">🎨 High Contrast Mode</span>
            </label>
            <label class="flex items-center">
              <input type="checkbox" v-model="survey.features.imageDescriptions" class="rounded text-primary-500 mr-3">
              <span class="text-gray-700 dark:text-gray-300">🖼️ Image Descriptions</span>
            </label>
          </div>
        </div>

        <!-- Content Type -->
        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            What type of content are you processing?
          </label>
          <select v-model="survey.contentType" class="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-primary-500">
            <option value="educational">📚 Educational Material</option>
            <option value="article">📰 Article/Blog Post</option>
            <option value="research">🔬 Research Paper</option>
            <option value="book">📕 Book Chapter</option>
            <option value="other">📄 Other</option>
          </select>
        </div>

        <!-- Learning Goals -->
        <div>
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
            What's your learning goal?
          </label>
          <textarea
            v-model="survey.learningGoal"
            rows="3"
            class="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-primary-500"
            placeholder="e.g., Understand the main concepts for an exam, Learn a new skill, etc."
          ></textarea>
        </div>
      </div>

      <button
        @click="nextStep"
        class="mt-6 w-full px-6 py-3 bg-gradient-to-r from-primary-500 to-accent-500 text-white rounded-lg font-semibold hover:shadow-lg transition-all"
      >
        Continue to AI Processing →
      </button>
    </div>

    <!-- Step 2: AI Processing -->
    <div v-if="currentStep === 1" class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8 animate-fade-in">
      <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-6">🤖 Processing with Gemini AI</h2>
      
      <div class="space-y-4">
        <!-- Processing Steps -->
        <div v-for="(process, index) in processingSteps" :key="index" class="flex items-center space-x-4">
          <div
            :class="[
              'w-8 h-8 rounded-full flex items-center justify-center',
              process.status === 'complete' ? 'bg-green-500' : process.status === 'processing' ? 'bg-blue-500 animate-pulse' : 'bg-gray-300'
            ]"
          >
            <svg v-if="process.status === 'complete'" class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <div v-else-if="process.status === 'processing'" class="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
            <span v-else class="text-white text-xs">{{ index + 1 }}</span>
          </div>
          <div class="flex-1">
            <p class="font-medium text-gray-900 dark:text-white">{{ process.name }}</p>
            <p class="text-sm text-gray-500 dark:text-gray-400">{{ process.description }}</p>
          </div>
        </div>
      </div>

      <div v-if="processingComplete" class="mt-6">
        <button
          @click="nextStep"
          class="w-full px-6 py-3 bg-gradient-to-r from-primary-500 to-accent-500 text-white rounded-lg font-semibold hover:shadow-lg transition-all"
        >
          View Results →
        </button>
      </div>
    </div>

    <!-- Step 3: Generated Content -->
    <div v-if="currentStep === 2" class="space-y-6 animate-fade-in">
      <!-- Simplified Content -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-2xl font-bold text-gray-900 dark:text-white">✨ Simplified Content</h2>
          <button @click="copyToClipboard(generatedContent.simplified)" class="px-4 py-2 bg-gray-100 dark:bg-gray-700 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-600 transition-all">
            📋 Copy
          </button>
        </div>
        <div class="prose dark:prose-invert max-w-none">
          <p class="text-gray-700 dark:text-gray-300 whitespace-pre-wrap">{{ generatedContent.simplified }}</p>
        </div>
      </div>

      <!-- Summary -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-2xl font-bold text-gray-900 dark:text-white">📝 Key Summary</h2>
          <button @click="copyToClipboard(generatedContent.summary)" class="px-4 py-2 bg-gray-100 dark:bg-gray-700 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-600 transition-all">
            📋 Copy
          </button>
        </div>
        <div class="prose dark:prose-invert max-w-none">
          <p class="text-gray-700 dark:text-gray-300 whitespace-pre-wrap">{{ generatedContent.summary }}</p>
        </div>
      </div>

      <!-- Key Points -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">🎯 Key Points</h2>
        <ul class="space-y-2">
          <li v-for="(point, index) in generatedContent.keyPoints" :key="index" class="flex items-start space-x-3">
            <span class="w-6 h-6 bg-gradient-to-r from-primary-500 to-accent-500 text-white rounded-full flex items-center justify-center text-sm flex-shrink-0 mt-0.5">{{ index + 1 }}</span>
            <span class="text-gray-700 dark:text-gray-300">{{ point }}</span>
          </li>
        </ul>
      </div>

      <!-- Action Buttons -->
      <div class="flex space-x-4">
        <button
          @click="saveContent"
          class="flex-1 px-6 py-3 bg-gradient-to-r from-primary-500 to-accent-500 text-white rounded-lg font-semibold hover:shadow-lg transition-all"
        >
          💾 Save Content
        </button>
        <button
          @click="startOver"
          class="flex-1 px-6 py-3 bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg font-semibold hover:bg-gray-300 dark:hover:bg-gray-600 transition-all"
        >
          🔄 Process Another File
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useContentStore } from '../stores/content';
import geminiService from '../services/gemini.service';

const route = useRoute();
const router = useRouter();
const contentStore = useContentStore();

const steps = ['Survey', 'AI Processing', 'Results'];
const currentStep = ref(0);

const survey = reactive({
  readingLevel: 'simple',
  features: {
    textToSpeech: true,
    dyslexiaFont: false,
    highContrast: false,
    imageDescriptions: true
  },
  contentType: 'educational',
  learningGoal: ''
});

const processingSteps = ref([
  { name: 'Reading Document', description: 'Extracting text content...', status: 'pending' },
  { name: 'Simplifying Text', description: 'Using Gemini AI to simplify content...', status: 'pending' },
  { name: 'Generating Summary', description: 'Creating concise summary...', status: 'pending' },
  { name: 'Extracting Key Points', description: 'Identifying main concepts...', status: 'pending' },
  { name: 'Finalizing', description: 'Preparing your content...', status: 'pending' }
]);

const processingComplete = ref(false);

const generatedContent = reactive({
  simplified: '',
  summary: '',
  keyPoints: [],
  original: ''
});

const fileContent = ref('');
const fileName = ref('');

onMounted(async () => {
  const uploads = contentStore.uploads;
  if (uploads.length > 0) {
    const lastUpload = uploads[uploads.length - 1];
    fileName.value = lastUpload.filename;
    fileContent.value = `Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll. Plants use sunlight, water, and carbon dioxide to produce glucose and oxygen. This process occurs in the chloroplasts of plant cells, specifically in structures called thylakoids. The light-dependent reactions take place in the thylakoid membranes, where light energy is converted into chemical energy in the form of ATP and NADPH. The light-independent reactions, also known as the Calvin cycle, occur in the stroma of the chloroplast. During these reactions, carbon dioxide is fixed into organic molecules using the energy from ATP and NADPH. The overall equation for photosynthesis is: 6CO2 + 6H2O + light energy → C6H12O6 + 6O2. This process is crucial for life on Earth as it provides oxygen for respiration and forms the base of most food chains.`;
  }
});

const nextStep = async () => {
  if (currentStep.value === 0) {
    currentStep.value = 1;
    await processWithAI();
  } else if (currentStep.value === 1 && processingComplete.value) {
    currentStep.value = 2;
  }
};

const processWithAI = async () => {
  try {
    processingSteps.value[0].status = 'processing';
    await delay(1000);
    processingSteps.value[0].status = 'complete';

    processingSteps.value[1].status = 'processing';
    const simplified = await geminiService.simplifyText(
      fileContent.value,
      survey.readingLevel
    );
    generatedContent.simplified = simplified;
    processingSteps.value[1].status = 'complete';

    processingSteps.value[2].status = 'processing';
    const summary = await geminiService.generateSummary(fileContent.value, 150);
    generatedContent.summary = summary;
    processingSteps.value[2].status = 'complete';

    processingSteps.value[3].status = 'processing';
    const keyPoints = await geminiService.extractKeyPoints(fileContent.value, 5);
    generatedContent.keyPoints = keyPoints;
    processingSteps.value[3].status = 'complete';

    processingSteps.value[4].status = 'processing';
    await delay(500);
    processingSteps.value[4].status = 'complete';

    processingComplete.value = true;
  } catch (error) {
    console.error('Processing error:', error);
    alert('Error processing content with AI. Please try again.');
  }
};

const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

const copyToClipboard = async (text) => {
  try {
    await navigator.clipboard.writeText(text);
    alert('✅ Copied to clipboard!');
  } catch (error) {
    console.error('Copy failed:', error);
  }
};

const saveContent = () => {
  contentStore.addSavedContent({
    id: Date.now().toString(),
    fileName: fileName.value,
    simplified: generatedContent.simplified,
    summary: generatedContent.summary,
    keyPoints: generatedContent.keyPoints,
    savedAt: new Date().toISOString()
  });
  alert('✅ Content saved successfully!');
  router.push('/dashboard/saved');
};

const startOver = () => {
  router.push('/dashboard/upload');
};
</script>
