<template>
  <div class="max-w-4xl mx-auto px-6 py-12">
    <div class="mb-12">
      <h1 class="font-sora font-bold text-4xl mb-3 transition-colors duration-500" :style="{ color: textColor }">Upload Learning Material</h1>
      <p class="font-inter text-lg transition-colors duration-500" :style="{ color: secondaryTextColor }">Upload documents or provide a URL to make content accessible</p>
    </div>

    <!-- Upload Tabs -->
    <div class="rounded-3xl shadow-xl overflow-hidden transition-all duration-500"
      :style="{
        background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
        backdropFilter: 'blur(20px)',
        border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
      }">
      <!-- Tab Headers -->
      <div class="flex transition-colors duration-500"
        :style="{ borderBottom: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)' }">
        <button
          @click="activeTab = 'file'"
          :class="[
            'flex-1 px-6 py-4 text-sm font-inter font-semibold transition-all duration-300',
            activeTab === 'file' && 'border-b-2'
          ]"
          :style="{
            background: activeTab === 'file' 
              ? (isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)')
              : 'transparent',
            color: textColor,
            borderColor: activeTab === 'file' ? textColor : 'transparent'
          }"
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
            'flex-1 px-6 py-4 text-sm font-inter font-semibold transition-all duration-300',
            activeTab === 'url' && 'border-b-2'
          ]"
          :style="{
            background: activeTab === 'url' 
              ? (isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)')
              : 'transparent',
            color: textColor,
            borderColor: activeTab === 'url' ? textColor : 'transparent'
          }"
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
              'border-2 border-dashed rounded-2xl p-12 text-center transition-all cursor-pointer duration-300'
            ]"
            :style="{
              background: isDragging
                ? (isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)')
                : (isDark ? 'rgba(255, 255, 255, 0.03)' : 'rgba(0, 0, 0, 0.03)'),
              borderColor: isDragging
                ? textColor
                : (isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)'),
              backdropFilter: 'blur(10px)'
            }"
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
              <svg class="w-16 h-16 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" :style="{ color: secondaryTextColor }">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
              </svg>
              <h3 class="font-sora font-bold text-xl mb-2 transition-colors duration-500" :style="{ color: textColor }">
                Drop your file here or click to browse
              </h3>
              <p class="font-inter text-sm mb-6 transition-colors duration-500" :style="{ color: secondaryTextColor }">
                Supports PDF, DOCX, TXT, PPTX, and images (max 50MB)
              </p>
              <div class="flex flex-wrap justify-center gap-3 mt-4">
                <span class="px-4 py-2 rounded-full text-xs font-inter font-semibold transition-all duration-300"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                    color: textColor
                  }">.pdf</span>
                <span class="px-4 py-2 rounded-full text-xs font-inter font-semibold transition-all duration-300"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                    color: textColor
                  }">.docx</span>
                <span class="px-4 py-2 rounded-full text-xs font-inter font-semibold transition-all duration-300"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                    color: textColor
                  }">.txt</span>
                <span class="px-4 py-2 rounded-full text-xs font-inter font-semibold transition-all duration-300"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                    color: textColor
                  }">.pptx</span>
                <span class="px-4 py-2 rounded-full text-xs font-inter font-semibold transition-all duration-300"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                    color: textColor
                  }">.jpg/.png</span>
              </div>
            </div>

            <!-- Selected File Preview -->
            <div v-else class="flex items-center justify-between rounded-xl p-6 transition-all duration-300"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.08)' : 'rgba(0, 0, 0, 0.08)'
              }">
              <div class="flex items-center space-x-4">
                <div class="w-14 h-14 rounded-xl flex items-center justify-center transition-all duration-300"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
                  }">
                  <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24" :style="{ color: textColor }">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                  </svg>
                </div>
                <div class="text-left">
                  <p class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">{{ selectedFile.name }}</p>
                  <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">{{ formatFileSize(selectedFile.size) }}</p>
                </div>
              </div>
              <button
                @click.stop="clearFile"
                class="transition-colors duration-300 hover:opacity-70"
                :style="{ color: secondaryTextColor }"
              >
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- URL Tab -->
        <div v-show="activeTab === 'url'" class="space-y-4">
          <div>
            <label class="block font-inter text-sm font-semibold mb-3 transition-colors duration-500" :style="{ color: textColor }">
              Enter URL
            </label>
            <input
              v-model="urlInput"
              type="url"
              placeholder="https://example.com/article"
              class="w-full px-5 py-4 rounded-xl font-inter text-sm transition-all duration-300 focus:ring-2 focus:outline-none"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
                border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)',
                color: textColor
              }"
            />
          </div>
          <p class="font-inter text-sm flex items-center gap-2 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            We'll extract and process the content from the webpage
          </p>
        </div>

        <!-- Error Message -->
        <div v-if="error" class="mt-6 rounded-xl px-5 py-4 transition-all duration-300"
          :style="{
            background: isDark ? 'rgba(255, 100, 100, 0.1)' : 'rgba(255, 100, 100, 0.1)',
            border: isDark ? '1px solid rgba(255, 100, 100, 0.3)' : '1px solid rgba(255, 100, 100, 0.3)',
            color: isDark ? 'rgba(255, 150, 150, 1)' : 'rgba(200, 50, 50, 1)'
          }">
          <p class="font-inter text-sm">{{ error }}</p>
        </div>

        <!-- Upload Button -->
        <div class="mt-8 flex justify-end space-x-4">
          <button
            v-if="selectedFile || urlInput"
            @click="clearAll"
            class="px-6 py-3 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-[1.02]"
            :style="{
              background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
              border: isDark ? '1px solid rgba(255, 255, 255, 0.2)' : '1px solid rgba(0, 0, 0, 0.2)',
              color: textColor
            }"
          >
            Cancel
          </button>
          <button
            @click="handleUpload"
            :disabled="(!selectedFile && !urlInput) || uploading"
            class="px-8 py-3 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-[1.02] disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
            :style="{
              background: isDark ? '#ffffff' : '#000000',
              color: isDark ? '#000000' : '#ffffff'
            }"
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
    <div v-if="uploading" class="mt-8 rounded-3xl p-8 shadow-xl transition-all duration-500"
      :style="{
        background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
        backdropFilter: 'blur(20px)',
        border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
      }">
      <div class="flex items-center space-x-4">
        <div class="flex-1">
          <div class="flex items-center justify-between mb-3">
            <span class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">Uploading...</span>
            <span class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">{{ uploadProgress }}%</span>
          </div>
          <div class="w-full rounded-full h-2 transition-all duration-300"
            :style="{ background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)' }">
            <div
              class="h-2 rounded-full transition-all duration-300"
              :style="{ 
                width: uploadProgress + '%',
                background: isDark ? '#ffffff' : '#000000'
              }"
            ></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useDark } from '@vueuse/core';
import { useAuthStore } from '../stores/auth';
import { useContentStore } from '../stores/content';
import { apiService } from '../services/api.service';

const router = useRouter();
const authStore = useAuthStore();
const contentStore = useContentStore();
const isDark = useDark();

const textColor = computed(() => isDark.value ? '#ffffff' : '#000000');
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)');

const activeTab = ref('file');
const isDragging = ref(false);
const selectedFile = ref(null);
const urlInput = ref('');
const uploading = ref(false);
const uploadProgress = ref(0);
const error = ref(null);

// Check if user has completed survey
onMounted(() => {
  if (authStore.user && !authStore.user.surveyCompleted) {
    alert('📋 Please complete the survey first to personalize your learning experience!');
    router.push('/dashboard/survey');
  }
});

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
      
      console.log('✅ Upload result:', result.data);
      
      // Save to database with extracted text content
      await contentStore.saveUpload(userId, {
        filename: result.data.file.filename,
        fileType: result.data.file.file_type,
        fileSize: result.data.file.file_size,
        filePath: result.data.file.file_path,
        textContent: result.data.file.text_content || '',  // Store extracted text
        uploadType: 'file',
        status: 'completed',
        uploadedAt: new Date().toISOString(),
      });
    } else if (activeTab.value === 'url' && urlInput.value) {
      // Upload URL
      result = await apiService.uploadURL(urlInput.value, userId);
      
      // Save to database with extracted content
      await contentStore.saveUpload(userId, {
        filename: urlInput.value,
        fileType: 'url',
        url: urlInput.value,
        textContent: result.data.content?.text || '',  // Store extracted text from URL
        uploadType: 'url',
        status: 'completed',
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
