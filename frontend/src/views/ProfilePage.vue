<template>
  <div class="max-w-6xl mx-auto px-6 py-12">
    <!-- Header -->
    <div class="mb-12">
      <h1 class="font-sora font-bold text-4xl mb-3 transition-colors duration-500" :style="{ color: textColor }">My Profile</h1>
      <p class="font-inter text-lg transition-colors duration-500" :style="{ color: secondaryTextColor }">Manage your account settings and preferences</p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Profile Card -->
      <div class="lg:col-span-1">
        <div class="rounded-3xl shadow-xl p-8 transition-all duration-500"
          :style="{
            background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
            backdropFilter: 'blur(20px)',
            border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
          }">
          <!-- Avatar -->
          <div class="flex justify-center mb-6">
            <div class="relative">
              <div class="w-32 h-32 rounded-full flex items-center justify-center font-sora font-black text-5xl transition-all duration-300"
                :style="{
                  background: isDark ? '#ffffff' : '#000000',
                  color: isDark ? '#000000' : '#ffffff'
                }">
                {{ userInitial }}
              </div>
              <button
                @click="showEditModal = true"
                class="absolute bottom-0 right-0 w-10 h-10 rounded-full flex items-center justify-center shadow-lg transition-all duration-300 hover:scale-110"
                :style="{
                  background: isDark ? '#ffffff' : '#000000',
                  color: isDark ? '#000000' : '#ffffff'
                }"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                </svg>
              </button>
            </div>
          </div>

          <!-- User Info -->
          <div class="text-center mb-6">
            <h2 class="font-sora font-bold text-2xl mb-2 transition-colors duration-500" :style="{ color: textColor }">
              {{ displayName }}
            </h2>
            <p class="font-inter text-sm mb-4 transition-colors duration-500" :style="{ color: secondaryTextColor }">
              {{ email }}
            </p>
            <div class="inline-block px-4 py-2 rounded-full font-inter text-xs font-semibold transition-all duration-300"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                color: textColor
              }">
              Member since {{ memberSince }}
            </div>
          </div>

          <!-- Quick Stats -->
          <div class="space-y-4 pt-6"
            :style="{ borderTop: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)' }">
            <div class="flex items-center justify-between">
              <span class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">Files Uploaded</span>
              <span class="font-sora font-bold text-lg transition-colors duration-500" :style="{ color: textColor }">{{ userStats.uploads }}</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">Files Processed</span>
              <span class="font-sora font-bold text-lg transition-colors duration-500" :style="{ color: textColor }">{{ userStats.processed }}</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">Saved Items</span>
              <span class="font-sora font-bold text-lg transition-colors duration-500" :style="{ color: textColor }">{{ userStats.saved }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Account Details & Settings -->
      <div class="lg:col-span-2 space-y-8">
        <!-- Account Information -->
        <div class="rounded-3xl shadow-xl p-8 transition-all duration-500"
          :style="{
            background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
            backdropFilter: 'blur(20px)',
            border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
          }">
          <div class="flex items-center justify-between mb-6">
            <h2 class="font-sora font-bold text-2xl transition-colors duration-500" :style="{ color: textColor }">
              Account Information
            </h2>
            <button
              @click="editMode = !editMode"
              class="px-4 py-2 rounded-xl font-inter font-semibold text-sm transition-all duration-300 hover:scale-105"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                color: textColor
              }"
            >
              {{ editMode ? 'Cancel' : 'Edit' }}
            </button>
          </div>

          <div class="space-y-6">
            <!-- Full Name -->
            <div>
              <label class="block font-inter text-sm font-semibold mb-2 transition-colors duration-500" :style="{ color: textColor }">
                Full Name
              </label>
              <input
                v-model="profileData.displayName"
                :disabled="!editMode"
                type="text"
                class="w-full px-5 py-4 rounded-xl font-inter text-sm transition-all duration-300"
                :class="{ 'cursor-not-allowed opacity-60': !editMode }"
                :style="{
                  background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
                  border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)',
                  color: textColor
                }"
              />
            </div>

            <!-- Email -->
            <div>
              <label class="block font-inter text-sm font-semibold mb-2 transition-colors duration-500" :style="{ color: textColor }">
                Email Address
              </label>
              <input
                v-model="profileData.email"
                :disabled="true"
                type="email"
                class="w-full px-5 py-4 rounded-xl font-inter text-sm cursor-not-allowed opacity-60 transition-all duration-300"
                :style="{
                  background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
                  border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)',
                  color: textColor
                }"
              />
              <p class="font-inter text-xs mt-2 transition-colors duration-500" :style="{ color: secondaryTextColor }">
                Email cannot be changed
              </p>
            </div>

            <!-- Bio -->
            <div>
              <label class="block font-inter text-sm font-semibold mb-2 transition-colors duration-500" :style="{ color: textColor }">
                Bio
              </label>
              <textarea
                v-model="profileData.bio"
                :disabled="!editMode"
                rows="4"
                class="w-full px-5 py-4 rounded-xl font-inter text-sm transition-all duration-300 resize-none"
                :class="{ 'cursor-not-allowed opacity-60': !editMode }"
                :style="{
                  background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
                  border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)',
                  color: textColor
                }"
                placeholder="Tell us about yourself..."
              ></textarea>
            </div>

            <!-- Save Button -->
            <div v-if="editMode" class="flex justify-end gap-4">
              <button
                @click="saveProfile"
                class="px-8 py-3 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-105"
                :style="{
                  background: isDark ? '#ffffff' : '#000000',
                  color: isDark ? '#000000' : '#ffffff'
                }"
              >
                Save Changes
              </button>
            </div>
          </div>
        </div>

        <!-- Recent Activity -->
        <div class="rounded-3xl shadow-xl p-8 transition-all duration-500"
          :style="{
            background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
            backdropFilter: 'blur(20px)',
            border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
          }">
          <h2 class="font-sora font-bold text-2xl mb-6 transition-colors duration-500" :style="{ color: textColor }">
            Recent Activity
          </h2>
          
          <div v-if="recentActivity.length === 0" class="text-center py-12">
            <svg class="w-16 h-16 mx-auto mb-4" viewBox="0 0 24 24" fill="none" :style="{ color: secondaryTextColor }">
              <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
            <p class="font-inter transition-colors duration-500" :style="{ color: secondaryTextColor }">
              No recent activity
            </p>
          </div>
          
          <div v-else class="space-y-4">
            <div
              v-for="activity in recentActivity"
              :key="activity.id"
              class="flex items-center gap-4 p-4 rounded-xl transition-all duration-300 hover:scale-[1.01]"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
              }"
            >
              <div class="w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0"
                :style="{
                  background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
                }">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" :style="{ color: textColor }">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="getActivityIcon(activity.type)" />
                </svg>
              </div>
              <div class="flex-1">
                <p class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">
                  {{ activity.title }}
                </p>
                <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                  {{ activity.timestamp }}
                </p>
              </div>
              <span class="px-3 py-1 rounded-full text-xs font-inter font-semibold"
                :style="{
                  background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                  color: textColor
                }">
                {{ activity.status }}
              </span>
            </div>
          </div>
        </div>

        <!-- Danger Zone -->
        <div class="rounded-3xl shadow-xl p-8 transition-all duration-500"
          :style="{
            background: isDark ? 'rgba(100, 0, 0, 0.2)' : 'rgba(255, 200, 200, 0.3)',
            backdropFilter: 'blur(20px)',
            border: isDark ? '1px solid rgba(255, 100, 100, 0.3)' : '1px solid rgba(200, 0, 0, 0.2)'
          }">
          <h2 class="font-sora font-bold text-2xl mb-4 transition-colors duration-500" :style="{ color: textColor }">
            Danger Zone
          </h2>
          <p class="font-inter text-sm mb-6 transition-colors duration-500" :style="{ color: secondaryTextColor }">
            Permanently delete your account and all associated data. This action cannot be undone.
          </p>
          <button
            @click="confirmDelete = true"
            class="px-6 py-3 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-105"
            :style="{
              background: isDark ? 'rgba(255, 100, 100, 0.3)' : 'rgba(255, 100, 100, 0.5)',
              border: isDark ? '1px solid rgba(255, 100, 100, 0.5)' : '1px solid rgba(200, 0, 0, 0.4)',
              color: isDark ? 'rgba(255, 150, 150, 1)' : 'rgba(150, 0, 0, 1)'
            }"
          >
            Delete Account
          </button>
        </div>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div
      v-if="confirmDelete"
      class="fixed inset-0 z-50 flex items-center justify-center p-4"
      :style="{ background: 'rgba(0, 0, 0, 0.7)' }"
      @click="confirmDelete = false"
    >
      <div
        class="rounded-3xl shadow-2xl max-w-md w-full p-8 transition-all duration-500"
        :style="{
          background: isDark ? 'rgba(0, 0, 0, 0.95)' : 'rgba(255, 255, 255, 0.95)',
          backdropFilter: 'blur(20px)',
          border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
        }"
        @click.stop
      >
        <h3 class="font-sora font-bold text-2xl mb-4 transition-colors duration-500" :style="{ color: textColor }">
          Delete Account?
        </h3>
        <p class="font-inter text-sm mb-6 transition-colors duration-500" :style="{ color: secondaryTextColor }">
          This action is permanent and cannot be undone. All your data will be lost forever.
        </p>
        <div class="flex gap-4">
          <button
            @click="confirmDelete = false"
            class="flex-1 px-6 py-3 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-105"
            :style="{
              background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
              color: textColor
            }"
          >
            Cancel
          </button>
          <button
            @click="deleteAccount"
            class="flex-1 px-6 py-3 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-105"
            :style="{
              background: 'rgba(255, 100, 100, 0.5)',
              color: isDark ? 'rgba(255, 150, 150, 1)' : 'rgba(150, 0, 0, 1)'
            }"
          >
            Delete
          </button>
        </div>
      </div>
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

const editMode = ref(false);
const showEditModal = ref(false);
const confirmDelete = ref(false);

const profileData = ref({
  displayName: authStore.user?.displayName || 'User',
  email: authStore.user?.email || 'user@example.com',
  bio: 'Passionate about making education accessible for everyone.'
});

const userInitial = computed(() => {
  return profileData.value.displayName?.charAt(0).toUpperCase() || 'U';
});

const displayName = computed(() => profileData.value.displayName);
const email = computed(() => profileData.value.email);

const memberSince = computed(() => {
  const createdAt = authStore.user?.metadata?.creationTime;
  if (!createdAt) return 'Recently';
  const date = new Date(createdAt);
  return date.toLocaleDateString('en-US', { month: 'short', year: 'numeric' });
});

const userStats = ref({
  uploads: 0,
  processed: 0,
  saved: 0
});

const recentActivity = ref([
  {
    id: 1,
    type: 'upload',
    title: 'Uploaded "Advanced Mathematics.pdf"',
    timestamp: '2 hours ago',
    status: 'Completed'
  },
  {
    id: 2,
    type: 'save',
    title: 'Saved "Physics Chapter 5" to favorites',
    timestamp: '1 day ago',
    status: 'Saved'
  },
  {
    id: 3,
    type: 'process',
    title: 'Processed "Biology Notes.docx"',
    timestamp: '2 days ago',
    status: 'Completed'
  }
]);

const getActivityIcon = (type) => {
  const icons = {
    upload: 'M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12',
    save: 'M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z',
    process: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z'
  };
  return icons[type] || icons.upload;
};

const saveProfile = async () => {
  // Save profile changes
  console.log('Saving profile:', profileData.value);
  editMode.value = false;
  // TODO: Implement actual save to Firebase
};

const deleteAccount = async () => {
  // Delete account
  console.log('Deleting account');
  confirmDelete.value = false;
  // TODO: Implement actual account deletion
  await authStore.logout();
  router.push('/');
};

onMounted(async () => {
  if (authStore.user) {
    await contentStore.fetchUserContent(authStore.user.uid);
    userStats.value = {
      uploads: contentStore.uploads.length,
      processed: contentStore.processedContent.length,
      saved: contentStore.savedContent.length
    };
  }
});
</script>
