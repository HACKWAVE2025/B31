<template>
  <div class="max-w-7xl mx-auto">
    <div class="flex items-center justify-between mb-8">
      <h1 class="text-3xl font-bold text-gray-900 dark:text-white">💾 Saved Content</h1>
      <p class="text-gray-600 dark:text-gray-400">{{ savedContent.length }} saved items</p>
    </div>

    <!-- Empty State -->
    <div v-if="savedContent.length === 0" class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-12 text-center">
      <div class="w-24 h-24 bg-gray-100 dark:bg-gray-700 rounded-full flex items-center justify-center mx-auto mb-4">
        <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
        </svg>
      </div>
      <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-2">No saved content yet</h2>
      <p class="text-gray-600 dark:text-gray-400 mb-6">Process some files and save your favorites!</p>
      <router-link
        to="/dashboard/upload"
        class="inline-block px-6 py-3 bg-gradient-to-r from-primary-500 to-accent-500 text-white rounded-lg font-semibold hover:shadow-lg transition-all"
      >
        Upload a File
      </router-link>
    </div>

    <!-- Saved Items Grid -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div
        v-for="item in savedContent"
        :key="item.id"
        class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 hover:shadow-xl transition-all cursor-pointer"
        @click="viewContent(item)"
      >
        <!-- Header -->
        <div class="flex items-start justify-between mb-4">
          <div class="flex-1">
            <h3 class="font-bold text-gray-900 dark:text-white text-lg mb-1 line-clamp-1">
              {{ item.fileName }}
            </h3>
            <p class="text-sm text-gray-500 dark:text-gray-400">
              {{ formatDate(item.savedAt) }}
            </p>
          </div>
          <button
            @click.stop="deleteItem(item.id)"
            class="text-gray-400 hover:text-red-600 dark:hover:text-red-400 transition-colors"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
          </button>
        </div>

        <!-- Summary Preview -->
        <div class="mb-4">
          <p class="text-sm text-gray-700 dark:text-gray-300 line-clamp-3">
            {{ item.summary }}
          </p>
        </div>

        <!-- Key Points Badge -->
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-2 text-sm text-gray-600 dark:text-gray-400">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
            </svg>
            <span>{{ item.keyPoints?.length || 0 }} key points</span>
          </div>
          <button
            @click.stop="viewContent(item)"
            class="text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 font-medium text-sm"
          >
            View →
          </button>
        </div>
      </div>
    </div>

    <!-- Content Modal -->
    <div
      v-if="selectedContent"
      class="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4"
      @click="closeModal"
    >
      <div
        class="bg-white dark:bg-gray-800 rounded-xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto"
        @click.stop
      >
        <!-- Modal Header -->
        <div class="sticky top-0 bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 p-6">
          <div class="flex items-start justify-between">
            <div>
              <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-1">
                {{ selectedContent.fileName }}
              </h2>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                Saved {{ formatDate(selectedContent.savedAt) }}
              </p>
            </div>
            <button
              @click="closeModal"
              class="text-gray-400 hover:text-gray-600 dark:hover:text-gray-200"
            >
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>

        <!-- Modal Content -->
        <div class="p-6 space-y-6">
          <!-- Simplified Text -->
          <div>
            <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-3">✨ Simplified Content</h3>
            <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-4">
              <p class="text-gray-700 dark:text-gray-300 whitespace-pre-wrap">{{ selectedContent.simplified }}</p>
            </div>
          </div>

          <!-- Summary -->
          <div>
            <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-3">📝 Summary</h3>
            <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-4">
              <p class="text-gray-700 dark:text-gray-300">{{ selectedContent.summary }}</p>
            </div>
          </div>

          <!-- Key Points -->
          <div>
            <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-3">🎯 Key Points</h3>
            <ul class="space-y-2">
              <li
                v-for="(point, index) in selectedContent.keyPoints"
                :key="index"
                class="flex items-start space-x-3 bg-gray-50 dark:bg-gray-900 rounded-lg p-3"
              >
                <span class="w-6 h-6 bg-gradient-to-r from-primary-500 to-accent-500 text-white rounded-full flex items-center justify-center text-sm flex-shrink-0">
                  {{ index + 1 }}
                </span>
                <span class="text-gray-700 dark:text-gray-300">{{ point }}</span>
              </li>
            </ul>
          </div>
        </div>

        <!-- Modal Footer -->
        <div class="sticky bottom-0 bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-700 p-6">
          <div class="flex space-x-4">
            <button
              @click="copyAllContent"
              class="flex-1 px-6 py-3 bg-gradient-to-r from-primary-500 to-accent-500 text-white rounded-lg font-semibold hover:shadow-lg transition-all"
            >
              📋 Copy All
            </button>
            <button
              @click="closeModal"
              class="flex-1 px-6 py-3 bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg font-semibold hover:bg-gray-300 dark:hover:bg-gray-600 transition-all"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useContentStore } from '../stores/content';
import { useRouter } from 'vue-router';

const contentStore = useContentStore();
const router = useRouter();

const savedContent = computed(() => contentStore.savedContent);
const selectedContent = ref(null);

const formatDate = (dateString) => {
  const date = new Date(dateString);
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

const viewContent = (item) => {
  selectedContent.value = item;
};

const closeModal = () => {
  selectedContent.value = null;
};

const deleteItem = (id) => {
  if (confirm('Are you sure you want to delete this saved content?')) {
    contentStore.removeSavedContent(id);
  }
};

const copyAllContent = async () => {
  const text = `
${selectedContent.value.fileName}

SIMPLIFIED CONTENT:
${selectedContent.value.simplified}

SUMMARY:
${selectedContent.value.summary}

KEY POINTS:
${selectedContent.value.keyPoints.map((point, i) => `${i + 1}. ${point}`).join('\n')}
  `.trim();

  try {
    await navigator.clipboard.writeText(text);
    alert('✅ All content copied to clipboard!');
  } catch (error) {
    console.error('Copy failed:', error);
  }
};
</script>
