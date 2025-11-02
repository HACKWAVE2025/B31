<template>
  <Teleport to="body">
    <Transition name="modal">
      <div v-if="modelValue" class="fixed inset-0 z-[100] flex items-center justify-center p-4" @click.self="closeModal">
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-black/70 backdrop-blur-sm"></div>

        <!-- Modal Content -->
        <div class="relative bg-gradient-to-br from-gray-900 to-gray-800 border border-white/20 rounded-2xl shadow-2xl max-w-md w-full p-8 animate-modal-enter">
          <!-- Close Button -->
          <button 
            @click="closeModal"
            class="absolute top-4 right-4 text-gray-400 hover:text-white transition-colors"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>

          <!-- Header -->
          <div class="text-center mb-8">
            <h2 class="text-3xl font-bold text-white mb-2">
              {{ isLogin ? 'Welcome Back' : 'Create Account' }}
            </h2>
            <p class="text-gray-400">
              {{ isLogin ? 'Sign in to continue learning' : 'Join thousands of learners today' }}
            </p>
          </div>

          <!-- Form -->
          <form @submit.prevent="handleSubmit" class="space-y-4">
            <!-- Name (Sign Up Only) -->
            <div v-if="!isLogin">
              <label class="block text-sm font-medium text-gray-300 mb-2">Full Name</label>
              <input
                v-model="formData.name"
                type="text"
                placeholder="John Doe"
                class="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                :class="{ 'border-red-500': errors.name }"
              />
              <p v-if="errors.name" class="text-red-400 text-sm mt-1">{{ errors.name }}</p>
            </div>

            <!-- Email -->
            <div>
              <label class="block text-sm font-medium text-gray-300 mb-2">Email</label>
              <input
                v-model="formData.email"
                type="email"
                placeholder="you@example.com"
                class="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                :class="{ 'border-red-500': errors.email }"
              />
              <p v-if="errors.email" class="text-red-400 text-sm mt-1">{{ errors.email }}</p>
            </div>

            <!-- Password -->
            <div>
              <label class="block text-sm font-medium text-gray-300 mb-2">Password</label>
              <input
                v-model="formData.password"
                type="password"
                placeholder="••••••••"
                class="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                :class="{ 'border-red-500': errors.password }"
              />
              <p v-if="errors.password" class="text-red-400 text-sm mt-1">{{ errors.password }}</p>
            </div>

            <!-- Confirm Password (Sign Up Only) -->
            <div v-if="!isLogin">
              <label class="block text-sm font-medium text-gray-300 mb-2">Confirm Password</label>
              <input
                v-model="formData.confirmPassword"
                type="password"
                placeholder="••••••••"
                class="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-lg text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                :class="{ 'border-red-500': errors.confirmPassword }"
              />
              <p v-if="errors.confirmPassword" class="text-red-400 text-sm mt-1">{{ errors.confirmPassword }}</p>
            </div>

            <!-- Forgot Password (Sign In Only) -->
            <div v-if="isLogin" class="text-right">
              <button type="button" class="text-sm text-blue-400 hover:text-blue-300 transition-colors">
                Forgot Password?
              </button>
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              :disabled="isLoading"
              class="w-full py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold rounded-lg hover:shadow-lg hover:shadow-purple-500/50 transition-all transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
            >
              <span v-if="isLoading" class="flex items-center justify-center">
                <svg class="animate-spin -ml-1 mr-2 h-5 w-5" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Processing...
              </span>
              <span v-else>
                {{ isLogin ? 'Sign In' : 'Create Account' }}
              </span>
            </button>

            <!-- Divider -->
            <div class="relative my-6">
              <div class="absolute inset-0 flex items-center">
                <div class="w-full border-t border-white/10"></div>
              </div>
              <div class="relative flex justify-center text-sm">
                <span class="px-2 bg-gray-900 text-gray-400">Or continue with</span>
              </div>
            </div>

            <!-- Google Sign In -->
            <button
              type="button"
              @click="handleGoogleSignIn"
              :disabled="isLoading"
              class="w-full py-3 bg-white/10 border border-white/20 text-white font-semibold rounded-lg hover:bg-white/20 transition-all flex items-center justify-center gap-3"
            >
              <svg class="w-5 h-5" viewBox="0 0 24 24">
                <path fill="currentColor" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                <path fill="currentColor" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                <path fill="currentColor" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                <path fill="currentColor" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
              </svg>
              Sign in with Google
            </button>
          </form>

          <!-- Toggle Auth Mode -->
          <p class="text-center text-gray-400 mt-6">
            {{ isLogin ? "Don't have an account?" : "Already have an account?" }}
            <button 
              @click="toggleAuthMode"
              class="text-blue-400 hover:text-blue-300 font-semibold transition-colors ml-1"
            >
              {{ isLogin ? 'Sign Up' : 'Sign In' }}
            </button>
          </p>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { useFirebaseAuth } from '../composables/useFirebaseAuth';

const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false
  }
});

const emit = defineEmits(['close', 'update:modelValue']);
const router = useRouter();

const { signUp, signIn, signInWithGoogle, validateEmail, validatePassword, getPasswordErrors } = useFirebaseAuth();

const isLogin = ref(true);
const isLoading = ref(false);

const formData = reactive({
  name: '',
  email: '',
  password: '',
  confirmPassword: ''
});

const errors = reactive({
  name: '',
  email: '',
  password: '',
  confirmPassword: ''
});

const validateForm = () => {
  // Reset errors
  Object.keys(errors).forEach(key => errors[key] = '');
  
  let isValid = true;

  // Name validation (sign up only)
  if (!isLogin.value && !formData.name.trim()) {
    errors.name = 'Name is required';
    isValid = false;
  }

  // Email validation
  if (!formData.email.trim()) {
    errors.email = 'Email is required';
    isValid = false;
  } else if (!validateEmail(formData.email)) {
    errors.email = 'Please enter a valid email address';
    isValid = false;
  }

  // Password validation
  if (!formData.password) {
    errors.password = 'Password is required';
    isValid = false;
  } else if (!isLogin.value && !validatePassword(formData.password)) {
    const passwordErrors = getPasswordErrors(formData.password);
    errors.password = passwordErrors.join(', ');
    isValid = false;
  }

  // Confirm password validation (sign up only)
  if (!isLogin.value) {
    if (!formData.confirmPassword) {
      errors.confirmPassword = 'Please confirm your password';
      isValid = false;
    } else if (formData.password !== formData.confirmPassword) {
      errors.confirmPassword = 'Passwords do not match';
      isValid = false;
    }
  }

  return isValid;
};

const handleSubmit = async () => {
  if (!validateForm()) return;

  isLoading.value = true;

  try {
    let result;
    if (isLogin.value) {
      result = await signIn(formData.email, formData.password);
    } else {
      result = await signUp(formData.name, formData.email, formData.password);
    }

    if (result.success) {
      console.log('✅ Authentication successful:', result.user);
      closeModal();
      // Redirect to dashboard
      router.push('/dashboard');
    } else {
      errors.email = result.error;
    }
  } catch (error) {
    console.error('❌ Authentication error:', error);
    errors.email = 'An unexpected error occurred. Please try again.';
  } finally {
    isLoading.value = false;
  }
};

const handleGoogleSignIn = async () => {
  isLoading.value = true;

  try {
    const result = await signInWithGoogle();

    if (result.success) {
      console.log('✅ Google sign-in successful:', result.user);
      closeModal();
      // Redirect to dashboard
      router.push('/dashboard');
    } else {
      errors.email = result.error;
    }
  } catch (error) {
    console.error('❌ Google sign-in error:', error);
    errors.email = 'Failed to sign in with Google. Please try again.';
  } finally {
    isLoading.value = false;
  }
};

const toggleAuthMode = () => {
  isLogin.value = !isLogin.value;
  // Reset form
  Object.keys(formData).forEach(key => formData[key] = '');
  Object.keys(errors).forEach(key => errors[key] = '');
};

const closeModal = () => {
  emit('update:modelValue', false);
  emit('close');
};
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

@keyframes modal-enter {
  from {
    opacity: 0;
    transform: scale(0.9) translateY(20px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

.animate-modal-enter {
  animation: modal-enter 0.3s ease-out;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>
