<template>
  <div class="max-w-7xl mx-auto px-6 py-12">
    <div class="flex items-center justify-between mb-12">
      <h1 class="font-sora font-bold text-4xl transition-colors duration-500" :style="{ color: textColor }">Saved Content</h1>
      <p class="font-inter text-lg transition-colors duration-500" :style="{ color: secondaryTextColor }">{{ savedContent.length }} saved items</p>
    </div>

    <!-- Empty State -->
    <div v-if="savedContent.length === 0" class="rounded-3xl shadow-xl p-16 text-center transition-all duration-500"
      :style="{
        background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
        backdropFilter: 'blur(20px)',
        border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
      }">
      <div class="w-24 h-24 rounded-full flex items-center justify-center mx-auto mb-6 transition-all duration-300"
        :style="{
          background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
        }">
        <svg class="w-12 h-12" fill="none" stroke="currentColor" viewBox="0 0 24 24" :style="{ color: secondaryTextColor }">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
        </svg>
      </div>
      <h2 class="font-sora font-bold text-3xl mb-3 transition-colors duration-500" :style="{ color: textColor }">No saved content yet</h2>
      <p class="font-inter text-lg mb-8 transition-colors duration-500" :style="{ color: secondaryTextColor }">Process some files and save your favorites!</p>
      <router-link
        to="/dashboard/upload"
        class="inline-block px-8 py-4 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-[1.02]"
        :style="{
          background: isDark ? '#ffffff' : '#000000',
          color: isDark ? '#000000' : '#ffffff'
        }"
      >
        Upload a File
      </router-link>
    </div>

    <!-- Saved Items Grid -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <div
        v-for="item in savedContent"
        :key="item.id"
        class="rounded-3xl shadow-xl p-8 hover:shadow-2xl transition-all duration-300 cursor-pointer hover:scale-[1.02]"
        :style="{
          background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
          backdropFilter: 'blur(20px)',
          border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
        }"
        @click="viewContent(item)"
      >
        <!-- Header -->
        <div class="flex items-start justify-between mb-6">
          <div class="flex-1">
            <h3 class="font-sora font-bold text-xl mb-2 line-clamp-1 transition-colors duration-500" :style="{ color: textColor }">
              {{ item.fileName }}
            </h3>
            <p class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
              {{ formatDate(item.savedAt) }}
            </p>
          </div>
          <button
            @click.stop="deleteItem(item.id)"
            class="transition-colors duration-300 hover:opacity-70"
            :style="{ color: secondaryTextColor }"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
          </button>
        </div>

        <!-- Summary Preview -->
        <div class="mb-6">
          <p class="font-inter text-sm leading-relaxed line-clamp-3 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            {{ item.summary }}
          </p>
        </div>

        <!-- Key Points Badge -->
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-2 font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
            </svg>
            <span>{{ item.keyPoints?.length || 0 }} key points</span>
          </div>
          <button
            @click.stop="viewContent(item)"
            class="font-inter font-semibold text-sm hover:opacity-70 transition-all duration-300"
            :style="{ color: textColor }"
          >
            View →
          </button>
        </div>
      </div>
    </div>

    <!-- Content Modal -->
    <div
      v-if="selectedContent"
      class="fixed inset-0 z-50 flex items-center justify-center p-4"
      :style="{ background: 'rgba(0, 0, 0, 0.7)' }"
      @click="closeModal"
    >
      <div
        class="rounded-3xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto transition-all duration-500"
        :style="{
          background: isDark ? 'rgba(0, 0, 0, 0.95)' : 'rgba(255, 255, 255, 0.95)',
          backdropFilter: 'blur(20px)',
          border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
        }"
        @click.stop
      >
        <!-- Modal Header -->
        <div class="sticky top-0 p-8 transition-colors duration-500"
          :style="{
            background: isDark ? 'rgba(0, 0, 0, 0.9)' : 'rgba(255, 255, 255, 0.9)',
            backdropFilter: 'blur(20px)',
            borderBottom: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
          }">
          <div class="flex items-start justify-between">
            <div>
              <h2 class="font-sora font-bold text-3xl mb-2 transition-colors duration-500" :style="{ color: textColor }">
                {{ selectedContent.fileName }}
              </h2>
              <p class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
                Saved {{ formatDate(selectedContent.savedAt) }}
              </p>
            </div>
            <button
              @click="closeModal"
              class="transition-colors duration-300 hover:opacity-70"
              :style="{ color: secondaryTextColor }"
            >
              <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>

        <!-- Modal Content -->
        <div class="p-8 space-y-8">
          <!-- Simplified Text -->
          <div>
            <h3 class="font-sora font-bold text-xl mb-4 transition-colors duration-500" :style="{ color: textColor }">Simplified Content</h3>
            <div class="rounded-2xl p-6 transition-all duration-300"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
              }">
              <p class="font-inter text-sm leading-relaxed whitespace-pre-wrap transition-colors duration-500" :style="{ color: secondaryTextColor }">{{ selectedContent.simplified }}</p>
            </div>
          </div>

          <!-- Summary -->
          <div>
            <h3 class="font-sora font-bold text-xl mb-4 transition-colors duration-500" :style="{ color: textColor }">Summary</h3>
            <div class="rounded-2xl p-6 transition-all duration-300"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
              }">
              <p class="font-inter text-sm leading-relaxed transition-colors duration-500" :style="{ color: secondaryTextColor }">{{ selectedContent.summary }}</p>
            </div>
          </div>

          <!-- Key Points -->
          <div>
            <h3 class="font-sora font-bold text-xl mb-4 transition-colors duration-500" :style="{ color: textColor }">Key Points</h3>
            <ul class="space-y-3">
              <li
                v-for="(point, index) in selectedContent.keyPoints"
                :key="index"
                class="flex items-start space-x-4 rounded-2xl p-4 transition-all duration-300"
                :style="{
                  background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                }"
              >
                <span class="w-8 h-8 rounded-full flex items-center justify-center font-inter font-bold text-sm flex-shrink-0 transition-all duration-300"
                  :style="{
                    background: isDark ? '#ffffff' : '#000000',
                    color: isDark ? '#000000' : '#ffffff'
                  }">
                  {{ index + 1 }}
                </span>
                <span class="font-inter text-sm leading-relaxed transition-colors duration-500" :style="{ color: secondaryTextColor }">{{ point }}</span>
              </li>
            </ul>
          </div>
        </div>

        <!-- Modal Footer -->
        <div class="sticky bottom-0 p-8 transition-colors duration-500"
          :style="{
            background: isDark ? 'rgba(0, 0, 0, 0.9)' : 'rgba(255, 255, 255, 0.9)',
            backdropFilter: 'blur(20px)',
            borderTop: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
          }">
          <div class="flex space-x-4">
            <button
              @click="copyAllContent"
              class="flex-1 px-8 py-4 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-[1.02]"
              :style="{
                background: isDark ? '#ffffff' : '#000000',
                color: isDark ? '#000000' : '#ffffff'
              }"
            >
              📋 Copy All
            </button>
            <button
              @click="closeModal"
              class="flex-1 px-8 py-4 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-[1.02]"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                color: textColor
              }"
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
import { ref, computed, onMounted } from 'vue';
import { useDark } from '@vueuse/core';
import { useContentStore } from '../stores/content';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';

const contentStore = useContentStore();
const authStore = useAuthStore();
const router = useRouter();
const isDark = useDark();

const textColor = computed(() => isDark.value ? '#ffffff' : '#000000');
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)');

const savedContent = computed(() => contentStore.savedContent);
const selectedContent = ref(null);

// Fetch saved content from database on mount
onMounted(async () => {
  if (authStore.user?.uid) {
    await contentStore.fetchUserContent(authStore.user.uid);
  }
});


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

const viewContent = (item) => {
  selectedContent.value = item;
};

const closeModal = () => {
  selectedContent.value = null;
};

const deleteItem = async (id) => {
  if (confirm('Are you sure you want to delete this saved content?')) {
    await contentStore.deleteContent(id);
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
