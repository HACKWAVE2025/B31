<template>
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold mb-6">Processing Content</h1>

    <!-- Step Indicator -->
    <div class="mb-8">
      <div class="flex items-center justify-between">
        <div v-for="(step, index) in steps" :key="index" class="flex-1">
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
      <!-- Success Banner -->
      <div class="bg-gradient-to-r from-green-500 to-emerald-600 rounded-xl shadow-lg p-6 text-white">
        <div class="flex items-center space-x-4">
          <div class="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
          </div>
          <div>
            <h3 class="text-xl font-bold">Processing Complete!</h3>
            <p class="text-white/90">Your content has been successfully processed and simplified.</p>
          </div>
        </div>
      </div>

      <!-- Simplified Content -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-lg overflow-hidden border border-gray-200 dark:border-gray-700">
        <div class="bg-gradient-to-r from-primary-500 to-accent-500 px-6 py-4 flex items-center justify-between">
          <h2 class="text-xl font-bold text-white flex items-center">
            <span class="mr-2">✨</span> Simplified Content
          </h2>
          <button 
            @click="copyToClipboard(formatText(generatedContent.simplified))" 
            class="px-4 py-2 bg-white/20 hover:bg-white/30 rounded-lg transition-all text-white font-medium text-sm"
          >
            📋 Copy
          </button>
        </div>
        <div class="p-6">
          <div class="prose prose-lg dark:prose-invert max-w-none">
            <div 
              class="text-gray-800 dark:text-gray-200 leading-relaxed space-y-4"
              v-html="formatTextToHTML(generatedContent.simplified)"
            ></div>
          </div>
        </div>
      </div>

      <!-- Summary -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-lg overflow-hidden border border-gray-200 dark:border-gray-700">
        <div class="bg-gradient-to-r from-blue-500 to-indigo-600 px-6 py-4 flex items-center justify-between">
          <h2 class="text-xl font-bold text-white flex items-center">
            <span class="mr-2">📝</span> Key Summary
          </h2>
          <button 
            @click="copyToClipboard(formatText(generatedContent.summary))" 
            class="px-4 py-2 bg-white/20 hover:bg-white/30 rounded-lg transition-all text-white font-medium text-sm"
          >
            📋 Copy
          </button>
        </div>
        <div class="p-6">
          <div class="prose prose-lg dark:prose-invert max-w-none">
            <div 
              class="text-gray-800 dark:text-gray-200 leading-relaxed space-y-4"
              v-html="formatTextToHTML(generatedContent.summary)"
            ></div>
          </div>
        </div>
      </div>

      <!-- Key Points -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-lg overflow-hidden border border-gray-200 dark:border-gray-700">
        <div class="bg-gradient-to-r from-purple-500 to-pink-600 px-6 py-4">
          <h2 class="text-xl font-bold text-white flex items-center">
            <span class="mr-2">🎯</span> Key Points
          </h2>
        </div>
        <div class="p-6">
          <div class="space-y-4">
            <div 
              v-for="(point, index) in formatKeyPoints(generatedContent.keyPoints)" 
              :key="index" 
              class="flex items-start space-x-4 p-4 bg-gray-50 dark:bg-gray-700/50 rounded-lg hover:shadow-md transition-all"
            >
              <div class="w-8 h-8 bg-gradient-to-br from-purple-500 to-pink-600 text-white rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0">
                {{ index + 1 }}
              </div>
              <p class="text-gray-800 dark:text-gray-200 leading-relaxed flex-1 pt-0.5">{{ point }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <button
          @click="saveContent"
          class="px-6 py-4 bg-gradient-to-r from-green-500 to-emerald-600 text-white rounded-xl font-semibold hover:shadow-lg transform hover:scale-105 transition-all flex items-center justify-center space-x-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"></path>
          </svg>
          <span>Save Content</span>
        </button>
        <button
          @click="downloadPDF"
          class="px-6 py-4 bg-gradient-to-r from-red-500 to-rose-600 text-white rounded-xl font-semibold hover:shadow-lg transform hover:scale-105 transition-all flex items-center justify-center space-x-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"></path>
          </svg>
          <span>Download PDF</span>
        </button>
        <button
          @click="startOver"
          class="px-6 py-4 bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-white rounded-xl font-semibold hover:bg-gray-300 dark:hover:bg-gray-600 transform hover:scale-105 transition-all flex items-center justify-center space-x-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
          </svg>
          <span>Process Another</span>
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
    
    // Use the text content extracted during upload
    fileContent.value = lastUpload.textContent || lastUpload.text_content || '';
    
    if (!fileContent.value) {
      console.warn('⚠️ No text content found in upload. File may need reprocessing.');
    } else {
      console.log('✅ Using uploaded file content:', fileContent.value.substring(0, 200) + '...');
      console.log(`📊 Content length: ${fileContent.value.length} characters, ${fileContent.value.split(' ').length} words`);
    }
  } else {
    console.error('❌ No uploads found in store');
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

// Format text by removing API response artifacts
const formatText = (text) => {
  if (!text) return '';
  
  // If it's an object, try to extract the text content
  if (typeof text === 'object') {
    // Handle API response format
    if (text.simplifiedText) return formatText(text.simplifiedText);
    if (text.summary) return formatText(text.summary);
    if (text.text) return formatText(text.text);
    if (text.content) return formatText(text.content);
    
    // Try to stringify and parse
    try {
      const str = JSON.stringify(text);
      return formatText(str);
    } catch (e) {
      return String(text);
    }
  }
  
  // Convert to string if not already
  text = String(text);
  
  // Remove JSON formatting if present
  if (text.includes('"success"') || text.includes('"simplifiedText"')) {
    try {
      const parsed = JSON.parse(text);
      return formatText(parsed); // Recursively format the parsed object
    } catch (e) {
      // Not JSON, continue with text cleanup
    }
  }
  
  // Clean up common artifacts
  return text
    .replace(/^["']|["']$/g, '') // Remove quotes at start/end
    .replace(/\\n/g, '\n') // Convert \n to actual newlines
    .trim();
};

// Format text to HTML with paragraphs
const formatTextToHTML = (text) => {
  const cleaned = formatText(text);
  if (!cleaned) return '<p class="text-gray-500 italic">No content available</p>';
  
  // Split into paragraphs and wrap in p tags
  const paragraphs = cleaned
    .split('\n\n')
    .filter(p => p.trim())
    .map(p => `<p class="mb-4 last:mb-0">${p.trim()}</p>`)
    .join('');
  
  return paragraphs || `<p>${cleaned}</p>`;
};

// Format key points from various response formats
const formatKeyPoints = (keyPoints) => {
  if (!keyPoints) {
    return ['No key points extracted yet.'];
  }
  
  // If it's an object (Gemini response format), extract the keyPoints property
  if (typeof keyPoints === 'object' && !Array.isArray(keyPoints)) {
    // Handle Gemini API response format: { success: true, keyPoints: "..." }
    if (keyPoints.keyPoints) {
      return formatKeyPoints(keyPoints.keyPoints);
    }
    if (keyPoints.points) {
      return formatKeyPoints(keyPoints.points);
    }
    
    // If no keyPoints property, try to get string values
    const values = Object.values(keyPoints).filter(v => typeof v === 'string' && v.length > 10);
    if (values.length > 0) {
      return formatKeyPoints(values[0]); // Take the first substantial string value
    }
  }
  
  // If it's already an array of strings, clean and return
  if (Array.isArray(keyPoints)) {
    if (keyPoints.length === 0) return ['No key points extracted yet.'];
    if (typeof keyPoints[0] === 'string') {
      return keyPoints.map(point => point.trim()).filter(p => p.length > 0);
    }
  }
  
  // If it's a string, parse it into an array
  if (typeof keyPoints === 'string') {
    if (!keyPoints.trim()) return ['No key points extracted yet.'];
    
    // Try to parse as JSON first
    try {
      const parsed = JSON.parse(keyPoints);
      return formatKeyPoints(parsed);
    } catch (e) {
      // Not JSON, split by newlines and extract numbered points
      const lines = keyPoints
        .split(/\n+/)
        .map(line => line.trim())
        .filter(line => line.length > 0)
        .map(line => {
          // Remove leading numbers, asterisks, dashes, etc.
          return line.replace(/^[\d\*\-\•]+[\.):\s]+/, '').trim();
        })
        .filter(line => line.length > 5); // Filter out very short lines
      
      return lines.length > 0 ? lines : ['No key points extracted yet.'];
    }
  }
  
  return ['No key points extracted yet.'];
};

// Download content as PDF
const downloadPDF = () => {
  const content = `
ACCESSIBILITY LEARNING HUB - PROCESSED CONTENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

File: ${fileName.value}
Date: ${new Date().toLocaleDateString()}
Reading Level: ${survey.readingLevel}


✨ SIMPLIFIED CONTENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

${formatText(generatedContent.simplified)}


📝 KEY SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

${formatText(generatedContent.summary)}


🎯 KEY POINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

${formatKeyPoints(generatedContent.keyPoints).map((point, i) => `${i + 1}. ${point}`).join('\n\n')}


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generated by Accessibility Learning Hub
Making education accessible to everyone 🌟
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  `.trim();
  
  // Create blob and download
  const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = `${fileName.value.replace(/\.[^/.]+$/, '')}_processed.txt`;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
  
  // Show success message
  setTimeout(() => {
    alert('✅ Downloaded as TXT file!\n\nNote: For PDF format, you can print this file as PDF from your text editor.');
  }, 100);
};

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
