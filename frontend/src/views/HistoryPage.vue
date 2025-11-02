<template>
  <div class="max-w-7xl mx-auto px-6 py-12">
    <!-- Header -->
    <div class="mb-12">
      <h1 class="font-sora font-bold text-4xl mb-3 transition-colors duration-500" :style="{ color: textColor }">Upload History</h1>
      <p class="font-inter text-lg transition-colors duration-500" :style="{ color: secondaryTextColor }">View and manage all your uploaded files</p>
    </div>

    <!-- Filters & Search -->
    <div class="rounded-3xl shadow-xl p-6 mb-8 transition-all duration-500"
      :style="{
        background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
        backdropFilter: 'blur(20px)',
        border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
      }">
      <div class="flex flex-col md:flex-row gap-4">
        <!-- Search -->
        <div class="flex-1">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search files..."
            class="w-full px-5 py-3 rounded-xl font-inter text-sm transition-all duration-300"
            :style="{
              background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
              border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)',
              color: textColor
            }"
          />
        </div>

        <!-- Status Filter -->
        <select
          v-model="filterStatus"
          class="px-5 py-3 rounded-xl font-inter text-sm transition-all duration-300"
          :style="{
            background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
            border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)',
            color: textColor
          }"
        >
          <option value="all">All Status</option>
          <option value="completed">Completed</option>
          <option value="processing">Processing</option>
          <option value="failed">Failed</option>
        </select>

        <!-- Sort -->
        <select
          v-model="sortBy"
          class="px-5 py-3 rounded-xl font-inter text-sm transition-all duration-300"
          :style="{
            background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
            border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)',
            color: textColor
          }"
        >
          <option value="newest">Newest First</option>
          <option value="oldest">Oldest First</option>
          <option value="name">Name (A-Z)</option>
          <option value="size">Size</option>
        </select>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="filteredUploads.length === 0" class="rounded-3xl shadow-xl p-16 text-center transition-all duration-500"
      :style="{
        background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
        backdropFilter: 'blur(20px)',
        border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
      }">
      <svg class="w-20 h-20 mx-auto mb-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" :style="{ color: secondaryTextColor }">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
      </svg>
      <h2 class="font-sora font-bold text-3xl mb-3 transition-colors duration-500" :style="{ color: textColor }">No uploads found</h2>
      <p class="font-inter text-lg mb-8 transition-colors duration-500" :style="{ color: secondaryTextColor }">
        {{ searchQuery ? 'Try a different search term' : 'Upload your first file to get started!' }}
      </p>
      <router-link
        v-if="!searchQuery"
        to="/dashboard/upload"
        class="inline-block px-8 py-4 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-105"
        :style="{
          background: isDark ? '#ffffff' : '#000000',
          color: isDark ? '#000000' : '#ffffff'
        }"
      >
        Upload a File
      </router-link>
    </div>

    <!-- Upload History List -->
    <div v-else class="space-y-4">
      <div
        v-for="upload in filteredUploads"
        :key="upload.id"
        class="rounded-3xl shadow-xl p-6 transition-all duration-300 cursor-pointer hover:scale-[1.01]"
        :style="{
          background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
          backdropFilter: 'blur(20px)',
          border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
        }"
        @click="viewUpload(upload)"
      >
        <div class="flex items-center justify-between gap-4">
          <!-- File Icon & Info -->
          <div class="flex items-center gap-4 flex-1 min-w-0">
            <div class="w-14 h-14 rounded-xl flex items-center justify-center flex-shrink-0 transition-all duration-300"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
              }">
              <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24" :style="{ color: textColor }">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="getFileIcon(upload.fileType)" />
              </svg>
            </div>
            
            <div class="flex-1 min-w-0">
              <h3 class="font-sora font-bold text-lg mb-1 truncate transition-colors duration-500" :style="{ color: textColor }">
                {{ upload.filename }}
              </h3>
              <div class="flex items-center gap-3 flex-wrap">
                <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                  {{ formatDate(upload.uploadedAt) }}
                </p>
                <span class="text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">•</span>
                <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                  {{ formatFileSize(upload.fileSize) }}
                </p>
                <span class="text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">•</span>
                <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                  {{ upload.fileType || 'Unknown' }}
                </p>
              </div>
            </div>
          </div>

          <!-- Status & Actions -->
          <div class="flex items-center gap-4">
            <span class="px-4 py-2 rounded-full text-xs font-inter font-semibold whitespace-nowrap"
              :style="{
                background: getStatusColor(upload.status).bg,
                color: getStatusColor(upload.status).text
              }">
              {{ upload.status }}
            </span>
            
            <button
              @click.stop="deleteUpload(upload.id)"
              class="p-2 rounded-lg transition-all duration-300 hover:scale-110"
              :style="{
                background: isDark ? 'rgba(255, 100, 100, 0.1)' : 'rgba(255, 100, 100, 0.1)',
                color: isDark ? 'rgba(255, 150, 150, 1)' : 'rgba(200, 50, 50, 1)'
              }"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Pagination -->
    <div v-if="totalPages > 1" class="flex justify-center items-center gap-2 mt-8">
      <button
        @click="currentPage--"
        :disabled="currentPage === 1"
        class="px-4 py-2 rounded-xl font-inter font-semibold text-sm transition-all duration-300 hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed"
        :style="{
          background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
          color: textColor
        }"
      >
        Previous
      </button>
      
      <span class="px-4 py-2 font-inter text-sm transition-colors duration-500" :style="{ color: textColor }">
        Page {{ currentPage }} of {{ totalPages }}
      </span>
      
      <button
        @click="currentPage++"
        :disabled="currentPage === totalPages"
        class="px-4 py-2 rounded-xl font-inter font-semibold text-sm transition-all duration-300 hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed"
        :style="{
          background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
          color: textColor
        }"
      >
        Next
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useDark } from '@vueuse/core';
import { useAuthStore } from '../stores/auth';
import { useContentStore } from '../stores/content';
import { useRouter } from 'vue-router';

const router = useRouter();
const authStore = useAuthStore();
const contentStore = useContentStore();
const isDark = useDark();

const textColor = computed(() => isDark.value ? '#ffffff' : '#000000');
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)');

const searchQuery = ref('');
const filterStatus = ref('all');
const sortBy = ref('newest');
const currentPage = ref(1);
const itemsPerPage = 10;

const uploads = computed(() => contentStore.uploads || []);

const filteredUploads = computed(() => {
  let result = [...uploads.value];

  // Search filter
  if (searchQuery.value) {
    result = result.filter(upload =>
      upload.filename?.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
  }

  // Status filter
  if (filterStatus.value !== 'all') {
    result = result.filter(upload => upload.status === filterStatus.value);
  }

  // Sort
  switch (sortBy.value) {
    case 'newest':
      result.sort((a, b) => new Date(b.uploadedAt) - new Date(a.uploadedAt));
      break;
    case 'oldest':
      result.sort((a, b) => new Date(a.uploadedAt) - new Date(b.uploadedAt));
      break;
    case 'name':
      result.sort((a, b) => a.filename.localeCompare(b.filename));
      break;
    case 'size':
      result.sort((a, b) => (b.fileSize || 0) - (a.fileSize || 0));
      break;
  }

  // Pagination
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return result.slice(start, end);
});

const totalPages = computed(() => Math.ceil((uploads.value?.length || 0) / itemsPerPage));

const formatDate = (dateString) => {
  if (!dateString) return 'Unknown date';
  const date = new Date(dateString);
  if (isNaN(date.getTime())) return 'Invalid date';
  
  const now = new Date();
  const diffMs = now - date;
  const diffMins = Math.floor(diffMs / 60000);
  const diffHours = Math.floor(diffMs / 3600000);
  const diffDays = Math.floor(diffMs / 86400000);

  if (diffMins < 1) return 'Just now';
  if (diffMins < 60) return `${diffMins} min ago`;
  if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;
  if (diffDays < 7) return `${diffDays} day${diffDays > 1 ? 's' : ''} ago`;
  
  return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
};

const formatFileSize = (bytes) => {
  if (!bytes) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i];
};

const getFileIcon = (type) => {
  const icons = {
    pdf: 'M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z',
    docx: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z',
    txt: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z',
    url: 'M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1'
  };
  return icons[type] || icons.pdf;
};

const getStatusColor = (status) => {
  const colors = {
    completed: {
      bg: isDark.value ? 'rgba(100, 255, 100, 0.15)' : 'rgba(100, 255, 100, 0.2)',
      text: isDark.value ? 'rgba(150, 255, 150, 1)' : 'rgba(0, 150, 0, 1)'
    },
    processing: {
      bg: isDark.value ? 'rgba(255, 200, 100, 0.15)' : 'rgba(255, 200, 100, 0.2)',
      text: isDark.value ? 'rgba(255, 220, 150, 1)' : 'rgba(180, 100, 0, 1)'
    },
    failed: {
      bg: isDark.value ? 'rgba(255, 100, 100, 0.15)' : 'rgba(255, 100, 100, 0.2)',
      text: isDark.value ? 'rgba(255, 150, 150, 1)' : 'rgba(200, 50, 50, 1)'
    }
  };
  return colors[status] || colors.completed;
};

const viewUpload = (upload) => {
  if (upload.status === 'completed') {
    router.push(`/dashboard/process/${upload.id}`);
  }
};

const deleteUpload = async (id) => {
  if (confirm('Are you sure you want to delete this upload?')) {
    await contentStore.deleteUpload(id);
  }
};

onMounted(async () => {
  if (authStore.user) {
    await contentStore.fetchUserContent(authStore.user.uid);
  }
});
</script>
