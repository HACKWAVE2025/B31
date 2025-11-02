<template>
  <div class="max-w-4xl mx-auto px-6 py-12">
    <!-- Header -->
    <div class="mb-12">
      <h1 class="font-sora font-bold text-4xl mb-3 transition-colors duration-500" :style="{ color: textColor }">Settings</h1>
      <p class="font-inter text-lg transition-colors duration-500" :style="{ color: secondaryTextColor }">Customize your accessibility preferences and experience</p>
    </div>

    <div class="space-y-8">
      <!-- Text-to-Speech Settings -->
      <div class="rounded-3xl shadow-xl p-8 transition-all duration-500"
        :style="{
          background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
          backdropFilter: 'blur(20px)',
          border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
        }">
        <div class="flex items-center gap-3 mb-6">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
            <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z" :stroke="textColor" stroke-width="2"/>
            <path d="M19 10v2a7 7 0 0 1-14 0v-2M12 19v4M8 23h8" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
          <h2 class="font-sora font-bold text-2xl transition-colors duration-500" :style="{ color: textColor }">
            Text-to-Speech
          </h2>
        </div>

        <div class="space-y-6">
          <!-- Voice Selection -->
          <div>
            <label class="block font-inter text-sm font-semibold mb-3 transition-colors duration-500" :style="{ color: textColor }">
              Preferred Voice
            </label>
            <select
              v-model="settings.ttsVoice"
              @change="saveSettings"
              class="w-full px-5 py-4 rounded-xl font-inter text-sm transition-all duration-300"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
                border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)',
                color: textColor
              }"
            >
              <option value="natural-female-us">Natural Female (English US)</option>
              <option value="natural-male-us">Natural Male (English US)</option>
              <option value="natural-female-uk">Natural Female (English UK)</option>
              <option value="natural-male-uk">Natural Male (English UK)</option>
              <option value="natural-female-au">Natural Female (English AU)</option>
              <option value="natural-male-au">Natural Male (English AU)</option>
            </select>
          </div>

          <!-- Speed Control -->
          <div>
            <div class="flex items-center justify-between mb-3">
              <label class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">
                Speaking Speed
              </label>
              <span class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
                {{ settings.ttsSpeed }}x
              </span>
            </div>
            <input
              v-model.number="settings.ttsSpeed"
              @input="saveSettings"
              type="range"
              min="0.5"
              max="2"
              step="0.1"
              class="w-full h-2 rounded-full appearance-none cursor-pointer"
              :style="{
                background: isDark 
                  ? `linear-gradient(to right, #ffffff ${(settings.ttsSpeed - 0.5) / 1.5 * 100}%, rgba(255, 255, 255, 0.1) ${(settings.ttsSpeed - 0.5) / 1.5 * 100}%)`
                  : `linear-gradient(to right, #000000 ${(settings.ttsSpeed - 0.5) / 1.5 * 100}%, rgba(0, 0, 0, 0.1) ${(settings.ttsSpeed - 0.5) / 1.5 * 100}%)`
              }"
            />
          </div>

          <!-- Test Button -->
          <button
            @click="testTTS"
            class="px-6 py-3 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-105"
            :style="{
              background: isDark ? '#ffffff' : '#000000',
              color: isDark ? '#000000' : '#ffffff'
            }"
          >
            🔊 Test Voice
          </button>
        </div>
      </div>

      <!-- Font & Display Settings -->
      <div class="rounded-3xl shadow-xl p-8 transition-all duration-500"
        :style="{
          background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
          backdropFilter: 'blur(20px)',
          border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
        }">
        <div class="flex items-center gap-3 mb-6">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
            <path d="M4 7V4h16v3M9 20h6M12 4v16" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
          <h2 class="font-sora font-bold text-2xl transition-colors duration-500" :style="{ color: textColor }">
            Font & Display
          </h2>
        </div>

        <div class="space-y-6">
          <!-- Font Type -->
          <div>
            <label class="block font-inter text-sm font-semibold mb-3 transition-colors duration-500" :style="{ color: textColor }">
              Font Type
            </label>
            <select
              v-model="settings.fontType"
              @change="saveSettings"
              class="w-full px-5 py-4 rounded-xl font-inter text-sm transition-all duration-300"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
                border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)',
                color: textColor
              }"
            >
              <option value="default">Default (Sora & Inter)</option>
              <option value="opendyslexic">OpenDyslexic (Dyslexia-Friendly)</option>
              <option value="arial">Arial</option>
              <option value="verdana">Verdana</option>
              <option value="georgia">Georgia</option>
            </select>
            <p class="font-inter text-xs mt-2 transition-colors duration-500" :style="{ color: secondaryTextColor }">
              OpenDyslexic is specifically designed for readers with dyslexia
            </p>
          </div>

          <!-- Font Size -->
          <div>
            <div class="flex items-center justify-between mb-3">
              <label class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">
                Base Font Size
              </label>
              <span class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
                {{ settings.fontSize }}px
              </span>
            </div>
            <input
              v-model.number="settings.fontSize"
              @input="saveSettings"
              type="range"
              min="12"
              max="24"
              step="1"
              class="w-full h-2 rounded-full appearance-none cursor-pointer"
              :style="{
                background: isDark 
                  ? `linear-gradient(to right, #ffffff ${(settings.fontSize - 12) / 12 * 100}%, rgba(255, 255, 255, 0.1) ${(settings.fontSize - 12) / 12 * 100}%)`
                  : `linear-gradient(to right, #000000 ${(settings.fontSize - 12) / 12 * 100}%, rgba(0, 0, 0, 0.1) ${(settings.fontSize - 12) / 12 * 100}%)`
              }"
            />
          </div>

          <!-- Line Spacing -->
          <div>
            <div class="flex items-center justify-between mb-3">
              <label class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">
                Line Spacing
              </label>
              <span class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
                {{ settings.lineSpacing }}
              </span>
            </div>
            <input
              v-model.number="settings.lineSpacing"
              @input="saveSettings"
              type="range"
              min="1"
              max="2.5"
              step="0.1"
              class="w-full h-2 rounded-full appearance-none cursor-pointer"
              :style="{
                background: isDark 
                  ? `linear-gradient(to right, #ffffff ${(settings.lineSpacing - 1) / 1.5 * 100}%, rgba(255, 255, 255, 0.1) ${(settings.lineSpacing - 1) / 1.5 * 100}%)`
                  : `linear-gradient(to right, #000000 ${(settings.lineSpacing - 1) / 1.5 * 100}%, rgba(0, 0, 0, 0.1) ${(settings.lineSpacing - 1) / 1.5 * 100}%)`
              }"
            />
          </div>
        </div>
      </div>

      <!-- Color & Contrast Settings -->
      <div class="rounded-3xl shadow-xl p-8 transition-all duration-500"
        :style="{
          background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
          backdropFilter: 'blur(20px)',
          border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
        }">
        <div class="flex items-center gap-3 mb-6">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="10" :stroke="textColor" stroke-width="2"/>
            <path d="M8 12h8M12 8v8" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
          <h2 class="font-sora font-bold text-2xl transition-colors duration-500" :style="{ color: textColor }">
            Color & Contrast
          </h2>
        </div>

        <div class="space-y-6">
          <!-- Color Theme -->
          <div>
            <label class="block font-inter text-sm font-semibold mb-3 transition-colors duration-500" :style="{ color: textColor }">
              Theme Mode
            </label>
            <div class="grid grid-cols-2 gap-4">
              <button
                @click="toggleTheme(false)"
                class="p-4 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-105"
                :style="{
                  background: !isDark ? '#000000' : 'rgba(255, 255, 255, 0.1)',
                  color: !isDark ? '#ffffff' : textColor,
                  border: !isDark ? '2px solid #000000' : `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'}`
                }"
              >
                ☀️ Light Mode
              </button>
              <button
                @click="toggleTheme(true)"
                class="p-4 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-105"
                :style="{
                  background: isDark ? '#ffffff' : 'rgba(0, 0, 0, 0.1)',
                  color: isDark ? '#000000' : textColor,
                  border: isDark ? '2px solid #ffffff' : `1px solid ${isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'}`
                }"
              >
                🌙 Dark Mode
              </button>
            </div>
          </div>

          <!-- Contrast Level -->
          <div>
            <label class="block font-inter text-sm font-semibold mb-3 transition-colors duration-500" :style="{ color: textColor }">
              Contrast Level
            </label>
            <select
              v-model="settings.colorContrast"
              @change="saveSettings"
              class="w-full px-5 py-4 rounded-xl font-inter text-sm transition-all duration-300"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
                border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)',
                color: textColor
              }"
            >
              <option value="normal">Normal Contrast</option>
              <option value="high">High Contrast</option>
              <option value="maximum">Maximum Contrast</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Language Settings -->
      <div class="rounded-3xl shadow-xl p-8 transition-all duration-500"
        :style="{
          background: isDark ? 'rgba(0, 0, 0, 0.4)' : 'rgba(255, 255, 255, 0.6)',
          backdropFilter: 'blur(20px)',
          border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
        }">
        <div class="flex items-center gap-3 mb-6">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="10" :stroke="textColor" stroke-width="2"/>
            <path d="M2 12h20" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" :stroke="textColor" stroke-width="2"/>
          </svg>
          <h2 class="font-sora font-bold text-2xl transition-colors duration-500" :style="{ color: textColor }">
            Language
          </h2>
        </div>

        <div class="space-y-6">
          <!-- Interface Language -->
          <div>
            <label class="block font-inter text-sm font-semibold mb-3 transition-colors duration-500" :style="{ color: textColor }">
              Interface Language
            </label>
            <select
              v-model="settings.language"
              @change="saveSettings"
              class="w-full px-5 py-4 rounded-xl font-inter text-sm transition-all duration-300"
              :style="{
                background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
                border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)',
                color: textColor
              }"
            >
              <option value="en-US">English (US)</option>
              <option value="en-GB">English (UK)</option>
              <option value="es">Español</option>
              <option value="fr">Français</option>
              <option value="de">Deutsch</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Reset Settings -->
      <div class="rounded-3xl shadow-xl p-8 transition-all duration-500"
        :style="{
          background: isDark ? 'rgba(100, 0, 0, 0.2)' : 'rgba(255, 200, 200, 0.3)',
          backdropFilter: 'blur(20px)',
          border: isDark ? '1px solid rgba(255, 100, 100, 0.3)' : '1px solid rgba(200, 0, 0, 0.2)'
        }">
        <h2 class="font-sora font-bold text-2xl mb-4 transition-colors duration-500" :style="{ color: textColor }">
          Reset Settings
        </h2>
        <p class="font-inter text-sm mb-6 transition-colors duration-500" :style="{ color: secondaryTextColor }">
          Restore all settings to their default values
        </p>
        <button
          @click="resetSettings"
          class="px-6 py-3 rounded-xl font-inter font-semibold transition-all duration-300 hover:scale-105"
          :style="{
            background: isDark ? 'rgba(255, 100, 100, 0.3)' : 'rgba(255, 100, 100, 0.5)',
            border: isDark ? '1px solid rgba(255, 100, 100, 0.5)' : '1px solid rgba(200, 0, 0, 0.4)',
            color: isDark ? 'rgba(255, 150, 150, 1)' : 'rgba(150, 0, 0, 1)'
          }"
        >
          Reset to Defaults
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useDark } from '@vueuse/core';

const isDark = useDark();

const textColor = computed(() => isDark.value ? '#ffffff' : '#000000');
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)');

const defaultSettings = {
  ttsVoice: 'natural-female-us',
  ttsSpeed: 1.0,
  fontType: 'default',
  fontSize: 16,
  lineSpacing: 1.5,
  colorContrast: 'normal',
  language: 'en-US'
};

const settings = ref({ ...defaultSettings });

const loadSettings = () => {
  const stored = localStorage.getItem('skillset-settings');
  if (stored) {
    settings.value = { ...defaultSettings, ...JSON.parse(stored) };
  }
};

const saveSettings = () => {
  localStorage.setItem('skillset-settings', JSON.stringify(settings.value));
  console.log('✅ Settings saved:', settings.value);
};

const resetSettings = () => {
  if (confirm('Are you sure you want to reset all settings to defaults?')) {
    settings.value = { ...defaultSettings };
    saveSettings();
  }
};

const toggleTheme = (dark) => {
  isDark.value = dark;
};

const testTTS = () => {
  const utterance = new SpeechSynthesisUtterance('Hello! This is a test of the text-to-speech feature.');
  utterance.rate = settings.value.ttsSpeed;
  speechSynthesis.speak(utterance);
};

onMounted(() => {
  loadSettings();
});
</script>

<style scoped>
/* Custom scrollbar for range inputs */
input[type="range"]::-webkit-slider-thumb {
  appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: currentColor;
  cursor: pointer;
}

input[type="range"]::-moz-range-thumb {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: currentColor;
  cursor: pointer;
  border: none;
}
</style>
