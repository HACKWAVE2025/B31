<template>
  <div class="space-y-6">
    <!-- Welcome Section -->
    <div class="bg-gradient-to-r from-primary-500 to-accent-500 rounded-2xl p-8 text-white shadow-lg">
      <h1 class="text-3xl font-bold mb-2">
        Welcome back, {{ authStore.user?.displayName || 'there' }}! 👋
      </h1>
      <p class="text-white/90 text-lg">
        {{ greetingMessage }}
      </p>
      <div class="mt-6 flex flex-wrap gap-4">
        <router-link
          to="/dashboard/upload"
          class="bg-white text-primary-600 px-6 py-3 rounded-lg font-semibold hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-200 flex items-center space-x-2"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
          </svg>
          <span>Upload New Material</span>
        </router-link>
        <router-link
          v-if="!authStore.user?.surveyCompleted"
          to="/dashboard/survey"
          class="bg-white/20 backdrop-blur-sm text-white border-2 border-white px-6 py-3 rounded-lg font-semibold hover:bg-white/30 transition-all duration-200"
        >
          Complete Your Profile Survey
        </router-link>
      </div>
    </div>

    <!-- Stats Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md border border-gray-100 dark:border-gray-700">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600 dark:text-gray-400 mb-1">Total Uploads</p>
            <p class="text-3xl font-bold text-gray-900 dark:text-white">{{ stats.uploads }}</p>
          </div>
          <div class="w-12 h-12 bg-blue-100 dark:bg-blue-900 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md border border-gray-100 dark:border-gray-700">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600 dark:text-gray-400 mb-1">Processed Files</p>
            <p class="text-3xl font-bold text-gray-900 dark:text-white">{{ stats.processed }}</p>
          </div>
          <div class="w-12 h-12 bg-green-100 dark:bg-green-900 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-green-600 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
      </div>

      <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md border border-gray-100 dark:border-gray-700">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm text-gray-600 dark:text-gray-400 mb-1">Saved Items</p>
            <p class="text-3xl font-bold text-gray-900 dark:text-white">{{ stats.saved }}</p>
          </div>
          <div class="w-12 h-12 bg-purple-100 dark:bg-purple-900 rounded-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-purple-600 dark:text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Recent Activity -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <!-- Recent Uploads -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700">
        <div class="p-6 border-b border-gray-200 dark:border-gray-700">
          <div class="flex items-center justify-between">
            <h2 class="text-xl font-bold text-gray-900 dark:text-white">Recent Uploads</h2>
            <router-link
              to="/dashboard/history"
              class="text-sm text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 font-medium"
            >
              View all →
            </router-link>
          </div>
        </div>
        <div class="p-6">
          <div v-if="contentStore.recentUploads.length === 0" class="text-center py-8">
            <svg class="w-16 h-16 text-gray-300 dark:text-gray-600 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
            </svg>
            <p class="text-gray-500 dark:text-gray-400">No uploads yet</p>
            <router-link to="/dashboard/upload" class="text-primary-600 dark:text-primary-400 hover:underline mt-2 inline-block">
              Upload your first file
            </router-link>
          </div>
          <div v-else class="space-y-3">
            <div
              v-for="upload in contentStore.recentUploads"
              :key="upload.id"
              class="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-600 transition-colors"
            >
              <div class="flex items-center space-x-3 flex-1 min-w-0">
                <div class="flex-shrink-0 w-10 h-10 bg-blue-100 dark:bg-blue-900 rounded-lg flex items-center justify-center">
                  <svg class="w-5 h-5 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                  </svg>
                </div>
                <div class="flex-1 min-w-0">
                  <p class="text-sm font-medium text-gray-900 dark:text-white truncate">{{ upload.fileName }}</p>
                  <p class="text-xs text-gray-500 dark:text-gray-400">{{ formatDate(upload.createdAt) }}</p>
                </div>
              </div>
              <span class="px-3 py-1 bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 text-xs font-medium rounded-full">
                {{ upload.status }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Saved Content -->
      <div class="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700">
        <div class="p-6 border-b border-gray-200 dark:border-gray-700">
          <div class="flex items-center justify-between">
            <h2 class="text-xl font-bold text-gray-900 dark:text-white">Saved Content</h2>
            <router-link
              to="/dashboard/saved"
              class="text-sm text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 font-medium"
            >
              View all →
            </router-link>
          </div>
        </div>
        <div class="p-6">
          <div v-if="contentStore.savedContent.length === 0" class="text-center py-8">
            <svg class="w-16 h-16 text-gray-300 dark:text-gray-600 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
            </svg>
            <p class="text-gray-500 dark:text-gray-400">No saved content yet</p>
          </div>
          <div v-else class="space-y-3">
            <div
              v-for="saved in contentStore.savedContent.slice(0, 5)"
              :key="saved.id"
              class="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-600 transition-colors cursor-pointer"
            >
              <div class="flex items-center space-x-3 flex-1 min-w-0">
                <div class="flex-shrink-0 w-10 h-10 bg-purple-100 dark:bg-purple-900 rounded-lg flex items-center justify-center">
                  <svg class="w-5 h-5 text-purple-600 dark:text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                </div>
                <div class="flex-1 min-w-0">
                  <p class="text-sm font-medium text-gray-900 dark:text-white truncate">Processed Content</p>
                  <p class="text-xs text-gray-500 dark:text-gray-400">{{ formatDate(saved.savedAt) }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Quick Actions -->
    <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-md border border-gray-100 dark:border-gray-700">
      <h2 class="text-xl font-bold text-gray-900 dark:text-white mb-4">Quick Actions</h2>
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <router-link
          to="/dashboard/upload"
          class="flex flex-col items-center justify-center p-6 bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900/20 dark:to-blue-800/20 rounded-xl hover:shadow-lg transform hover:-translate-y-1 transition-all duration-200 group"
        >
          <div class="w-12 h-12 bg-blue-500 rounded-lg flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
            </svg>
          </div>
          <span class="text-sm font-semibold text-gray-900 dark:text-white">Upload File</span>
        </router-link>

        <router-link
          to="/dashboard/history"
          class="flex flex-col items-center justify-center p-6 bg-gradient-to-br from-green-50 to-green-100 dark:from-green-900/20 dark:to-green-800/20 rounded-xl hover:shadow-lg transform hover:-translate-y-1 transition-all duration-200 group"
        >
          <div class="w-12 h-12 bg-green-500 rounded-lg flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <span class="text-sm font-semibold text-gray-900 dark:text-white">View History</span>
        </router-link>

        <router-link
          to="/dashboard/saved"
          class="flex flex-col items-center justify-center p-6 bg-gradient-to-br from-purple-50 to-purple-100 dark:from-purple-900/20 dark:to-purple-800/20 rounded-xl hover:shadow-lg transform hover:-translate-y-1 transition-all duration-200 group"
        >
          <div class="w-12 h-12 bg-purple-500 rounded-lg flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
            </svg>
          </div>
          <span class="text-sm font-semibold text-gray-900 dark:text-white">Saved Content</span>
        </router-link>

        <router-link
          to="/dashboard/settings"
          class="flex flex-col items-center justify-center p-6 bg-gradient-to-br from-orange-50 to-orange-100 dark:from-orange-900/20 dark:to-orange-800/20 rounded-xl hover:shadow-lg transform hover:-translate-y-1 transition-all duration-200 group"
        >
          <div class="w-12 h-12 bg-orange-500 rounded-lg flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
          </div>
          <span class="text-sm font-semibold text-gray-900 dark:text-white">Settings</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useContentStore } from '../stores/content';

const authStore = useAuthStore();
const contentStore = useContentStore();

const stats = ref({
  uploads: 0,
  processed: 0,
  saved: 0,
});

const greetingMessage = computed(() => {
  const hour = new Date().getHours();
  if (hour < 12) return 'Good morning! Ready to make learning accessible?';
  if (hour < 18) return 'Good afternoon! Let\'s transform some content today.';
  return 'Good evening! Keep making education accessible for everyone.';
});

const formatDate = (dateString) => {
  const date = new Date(dateString);
  const now = new Date();
  const diffMs = now - date;
  const diffMins = Math.floor(diffMs / 60000);
  const diffHours = Math.floor(diffMs / 3600000);
  const diffDays = Math.floor(diffMs / 86400000);

  if (diffMins < 1) return 'Just now';
  if (diffMins < 60) return `${diffMins} min${diffMins > 1 ? 's' : ''} ago`;
  if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`;
  if (diffDays < 7) return `${diffDays} day${diffDays > 1 ? 's' : ''} ago`;
  return date.toLocaleDateString();
};

onMounted(async () => {
  if (authStore.user) {
    await contentStore.fetchUserContent(authStore.user.uid);
    stats.value = {
      uploads: contentStore.uploads.length,
      processed: contentStore.processedContent.length,
      saved: contentStore.savedContent.length,
    };
  }
});
</script>
