<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 via-white to-purple-50 dark:from-gray-900 dark:via-gray-900 dark:to-purple-900 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <!-- Logo and Title -->
      <div class="text-center">
        <router-link to="/" class="inline-flex items-center justify-center space-x-3 mb-6">
          <div class="w-12 h-12 bg-gradient-to-br from-primary-500 to-accent-500 rounded-lg flex items-center justify-center">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
          </div>
          <span class="text-3xl font-bold bg-gradient-to-r from-primary-600 to-accent-600 bg-clip-text text-transparent">
            AccessiLearn
          </span>
        </router-link>
        <h2 class="text-3xl font-bold text-gray-900 dark:text-white">Create your account</h2>
        <p class="mt-2 text-gray-600 dark:text-gray-400">Start making learning accessible today</p>
      </div>

      <!-- Register Form -->
      <div class="mt-8 bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 border border-gray-100 dark:border-gray-700">
        <form @submit.prevent="handleRegister" class="space-y-6">
          <!-- Error Message -->
          <div v-if="error" class="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 text-red-800 dark:text-red-200 px-4 py-3 rounded-lg">
            <p class="text-sm">{{ error }}</p>
          </div>

          <!-- Name -->
          <div>
            <label for="name" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              Full name
            </label>
            <input
              id="name"
              v-model="form.name"
              type="text"
              required
              autocomplete="name"
              class="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white transition-all"
              placeholder="John Doe"
            />
          </div>

          <!-- Email -->
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              Email address
            </label>
            <input
              id="email"
              v-model="form.email"
              type="email"
              required
              autocomplete="email"
              class="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white transition-all"
              placeholder="you@example.com"
            />
          </div>

          <!-- Password -->
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              Password
            </label>
            <input
              id="password"
              v-model="form.password"
              type="password"
              required
              autocomplete="new-password"
              minlength="6"
              class="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white transition-all"
              placeholder="••••••••"
            />
            <p class="mt-1 text-sm text-gray-500 dark:text-gray-400">Must be at least 6 characters</p>
          </div>

          <!-- Confirm Password -->
          <div>
            <label for="confirm-password" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              Confirm password
            </label>
            <input
              id="confirm-password"
              v-model="form.confirmPassword"
              type="password"
              required
              autocomplete="new-password"
              class="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white transition-all"
              placeholder="••••••••"
            />
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="loading"
            class="w-full bg-gradient-to-r from-primary-600 to-accent-600 text-white px-6 py-3 rounded-lg font-semibold hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
          >
            <span v-if="loading" class="flex items-center justify-center">
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Creating account...
            </span>
            <span v-else>Create account</span>
          </button>
        </form>

        <!-- Divider -->
        <div class="mt-6">
          <div class="relative">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-gray-300 dark:border-gray-600"></div>
            </div>
            <div class="relative flex justify-center text-sm">
              <span class="px-4 bg-white dark:bg-gray-800 text-gray-500 dark:text-gray-400">
                Already have an account?
              </span>
            </div>
          </div>
        </div>

        <!-- Sign In Link -->
        <div class="mt-6 text-center">
          <router-link
            to="/login"
            class="font-medium text-primary-600 dark:text-primary-400 hover:text-primary-500 dark:hover:text-primary-300 transition-colors"
          >
            Sign in instead →
          </router-link>
        </div>
      </div>

      <!-- Back to Home -->
      <div class="text-center">
        <router-link to="/" class="text-sm text-gray-600 dark:text-gray-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors">
          ← Back to home
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const router = useRouter();
const authStore = useAuthStore();

const form = reactive({
  name: '',
  email: '',
  password: '',
  confirmPassword: '',
});

const loading = ref(false);
const error = ref(null);

const handleRegister = async () => {
  // Validate passwords match
  if (form.password !== form.confirmPassword) {
    error.value = 'Passwords do not match';
    return;
  }

  // Validate password length
  if (form.password.length < 6) {
    error.value = 'Password must be at least 6 characters';
    return;
  }

  loading.value = true;
  error.value = null;

  const result = await authStore.register(form.email, form.password, form.name);

  if (result.success) {
    // Redirect to survey page for new users
    router.push('/dashboard/survey');
  } else {
    error.value = result.error || 'Failed to create account. Please try again.';
  }

  loading.value = false;
};
</script>
