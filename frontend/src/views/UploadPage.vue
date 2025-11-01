<template>
  <div class="max-w-4xl mx-auto">
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900 dark:text-white mb-2">Upload Learning Material</h1>
      <p class="text-gray-600 dark:text-gray-400">Upload documents or provide a URL to make content accessible</p>
    </div>

    <!-- Upload Tabs -->
    <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 overflow-hidden">
      <!-- Tab Headers -->
      <div class="flex border-b border-gray-200 dark:border-gray-700">
        <button
          @click="activeTab = 'file'"
          :class="[
            'flex-1 px-6 py-4 text-sm font-semibold transition-all',
            activeTab === 'file'
              ? 'bg-primary-50 dark:bg-primary-900/20 text-primary-600 dark:text-primary-400 border-b-2 border-primary-600'
              : 'text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700'
          ]"
        >
          <div class="flex items-center justify-center space-x-2">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
            </svg>
            <span>Upload File</span>
          </div>
        </button>
        <button
          @click="activeTab = 'url'"
          :class="[
            'flex-1 px-6 py-4 text-sm font-semibold transition-all',
            activeTab === 'url'
              ? 'bg-primary-50 dark:bg-primary-900/20 text-primary-600 dark:text-primary-400 border-b-2 border-primary-600'
              : 'text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700'
          ]"
        >
          <div class="flex items-center justify-center space-x-2">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" />
            </svg>
            <span>From URL</span>
          </div>
        </button>
      </div>

      <!-- Tab Content -->
      <div class="p-8">
        <!-- File Upload Tab -->
        <div v-show="activeTab === 'file'">
          <div
            @dragover.prevent="isDragging = true"
            @dragleave.prevent="isDragging = false"
            @drop.prevent="handleDrop"
            :class="[
              'border-2 border-dashed rounded-xl p-12 text-center transition-all cursor-pointer',
              isDragging
                ? 'border-primary-500 bg-primary-50 dark:bg-primary-900/20'
                : 'border-gray-300 dark:border-gray-600 hover:border-primary-400 dark:hover:border-primary-500'
            ]"
            @click="$refs.fileInput.click()"
          >
            <input
              ref="fileInput"
              type="file"
              @change="handleFileSelect"
              accept=".pdf,.docx,.doc,.txt,.pptx,.png,.jpg,.jpeg,.gif"
              class="hidden"
            />

            <div v-if="!selectedFile">
              <svg class="w-16 h-16 text-gray-400 dark:text-gray-500 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                Drop your file here or click to browse
              </h3>
              <p class="text-sm text-gray-500 dark:text-gray-400 mb-4">
                Supports PDF, DOCX, TXT, PPTX, and images (max 50MB)
              </p>
              <div class="flex flex-wrap justify-center gap-2 mt-4">
                <span class="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 text-xs font-medium rounded-full">.pdf</span>
                <span class="px-3 py-1 bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 text-xs font-medium rounded-full">.docx</span>
                <span class="px-3 py-1 bg-purple-100 dark:bg-purple-900 text-purple-800 dark:text-purple-200 text-xs font-medium rounded-full">.txt</span>
                <span class="px-3 py-1 bg-orange-100 dark:bg-orange-900 text-orange-800 dark:text-orange-200 text-xs font-medium rounded-full">.pptx</span>
                <span class="px-3 py-1 bg-pink-100 dark:bg-pink-900 text-pink-800 dark:text-pink-200 text-xs font-medium rounded-full">.jpg/.png</span>
              </div>
            </div>

            <!-- Selected File Preview -->
            <div v-else class="flex items-center justify-between bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
              <div class="flex items-center space-x-4">
                <div class="w-12 h-12 bg-blue-100 dark:bg-blue-900 rounded-lg flex items-center justify-center">
                  <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                  </svg>
                </div>
                <div class="text-left">
                  <p class="text-sm font-medium text-gray-900 dark:text-white">{{ selectedFile.name }}</p>
                  <p class="text-xs text-gray-500 dark:text-gray-400">{{ formatFileSize(selectedFile.size) }}</p>
                </div>
              </div>
              <button
                @click.stop="clearFile"
                class="text-red-600 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- URL Tab -->
        <div v-show="activeTab === 'url'" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              Enter URL
            </label>
            <input
              v-model="urlInput"
              type="url"
              placeholder="https://example.com/article"
              class="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
            />
          </div>
          <p class="text-sm text-gray-500 dark:text-gray-400">
            <svg class="w-4 h-4 inline mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            We'll extract and process the content from the webpage
          </p>
        </div>

        <!-- Error Message -->
        <div v-if="error" class="mt-4 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 text-red-800 dark:text-red-200 px-4 py-3 rounded-lg">
          <p class="text-sm">{{ error }}</p>
        </div>

        <!-- Upload Button -->
        <div class="mt-6 flex justify-end space-x-4">
          <button
            v-if="selectedFile || urlInput"
            @click="clearAll"
            class="px-6 py-3 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-all"
          >
            Cancel
          </button>
          <button
            @click="handleUpload"
            :disabled="(!selectedFile && !urlInput) || uploading"
            class="px-6 py-3 bg-gradient-to-r from-primary-600 to-accent-600 text-white rounded-lg font-semibold hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
          >
            <span v-if="uploading" class="flex items-center">
              <svg class="animate-spin -ml-1 mr-2 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Uploading...
            </span>
            <span v-else>Upload & Process</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Upload Progress -->
    <div v-if="uploading" class="mt-6 bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md border border-gray-100 dark:border-gray-700">
      <div class="flex items-center space-x-4">
        <div class="flex-1">
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-medium text-gray-700 dark:text-gray-300">Uploading...</span>
            <span class="text-sm text-gray-500 dark:text-gray-400">{{ uploadProgress }}%</span>
          </div>
          <div class="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
            <div
              class="bg-gradient-to-r from-primary-600 to-accent-600 h-2 rounded-full transition-all duration-300"
              :style="{ width: uploadProgress + '%' }"
            ></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';
import { useContentStore } from '../stores/content';
import { apiService } from '../services/api.service';

const router = useRouter();
const authStore = useAuthStore();
const contentStore = useContentStore();

const activeTab = ref('file');
const isDragging = ref(false);
const selectedFile = ref(null);
const urlInput = ref('');
const uploading = ref(false);
const uploadProgress = ref(0);
const error = ref(null);

const handleFileSelect = (event) => {
  const file = event.target.files[0];
  if (file) {
    if (file.size > 50 * 1024 * 1024) {
      error.value = 'File size must be less than 50MB';
      return;
    }
    selectedFile.value = file;
    error.value = null;
  }
};

const handleDrop = (event) => {
  isDragging.value = false;
  const file = event.dataTransfer.files[0];
  if (file) {
    if (file.size > 50 * 1024 * 1024) {
      error.value = 'File size must be less than 50MB';
      return;
    }
    selectedFile.value = file;
    error.value = null;
  }
};

const clearFile = () => {
  selectedFile.value = null;
  error.value = null;
};

const clearAll = () => {
  selectedFile.value = null;
  urlInput.value = '';
  error.value = null;
};

const formatFileSize = (bytes) => {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i];
};

const handleUpload = async () => {
  error.value = null;
  uploading.value = true;
  uploadProgress.value = 0;

  try {
    const userId = authStore.user?.uid;
    let result;

    // Simulate progress
    const progressInterval = setInterval(() => {
      if (uploadProgress.value < 90) {
        uploadProgress.value += 10;
      }
    }, 200);

    if (activeTab.value === 'file' && selectedFile.value) {
      // Upload file
      result = await apiService.uploadDocument(selectedFile.value, userId);
      
      // Save to Firestore
      await contentStore.saveUpload(userId, selectedFile.value, {
        fileId: result.data.fileId,
        uploadedAt: new Date().toISOString(),
      });
    } else if (activeTab.value === 'url' && urlInput.value) {
      // Upload URL
      result = await apiService.uploadURL(urlInput.value, userId);
      
      // Save to Firestore
      await contentStore.saveUpload(userId, { name: urlInput.value, type: 'url', size: 0 }, {
        url: urlInput.value,
        uploadedAt: new Date().toISOString(),
      });
    }

    clearInterval(progressInterval);
    uploadProgress.value = 100;

    // Redirect to process page
    setTimeout(() => {
      router.push({ name: 'Process', params: { id: result.data.fileId || 'url' } });
    }, 500);

  } catch (err) {
    console.error('Upload error:', err);
    error.value = err.response?.data?.error || 'Failed to upload. Please try again.';
    uploading.value = false;
    uploadProgress.value = 0;
  }
};
</script>
