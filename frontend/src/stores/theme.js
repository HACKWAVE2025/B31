import { defineStore } from 'pinia';

export const useThemeStore = defineStore('theme', {
  state: () => ({
    isDark: false,
    fontSize: 'medium', // small, medium, large, xl
    dyslexiaFont: false,
    highContrast: false,
    textToSpeech: false,
    speechRate: 1.0,
    preferredVoice: null,
  }),

  getters: {
    theme: (state) => (state.isDark ? 'dark' : 'light'),
    fontSizeClass: (state) => {
      const sizes = {
        small: 'text-sm',
        medium: 'text-base',
        large: 'text-lg',
        xl: 'text-xl',
      };
      return sizes[state.fontSize] || sizes.medium;
    },
    fontFamily: (state) => (state.dyslexiaFont ? 'font-dyslexic' : 'font-sans'),
  },

  actions: {
    toggleTheme() {
      this.isDark = !this.isDark;
      this.applyTheme();
      this.saveToLocalStorage();
    },

    setTheme(isDark) {
      this.isDark = isDark;
      this.applyTheme();
      this.saveToLocalStorage();
    },

    setFontSize(size) {
      this.fontSize = size;
      this.saveToLocalStorage();
    },

    toggleDyslexiaFont() {
      this.dyslexiaFont = !this.dyslexiaFont;
      this.saveToLocalStorage();
    },

    toggleHighContrast() {
      this.highContrast = !this.highContrast;
      this.applyHighContrast();
      this.saveToLocalStorage();
    },

    toggleTextToSpeech() {
      this.textToSpeech = !this.textToSpeech;
      this.saveToLocalStorage();
    },

    setSpeechRate(rate) {
      this.speechRate = rate;
      this.saveToLocalStorage();
    },

    setPreferredVoice(voice) {
      this.preferredVoice = voice;
      this.saveToLocalStorage();
    },

    applyTheme() {
      if (this.isDark) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    },

    applyHighContrast() {
      if (this.highContrast) {
        document.documentElement.classList.add('high-contrast');
      } else {
        document.documentElement.classList.remove('high-contrast');
      }
    },

    saveToLocalStorage() {
      localStorage.setItem('theme-preferences', JSON.stringify(this.$state));
    },

    loadFromLocalStorage() {
      const saved = localStorage.getItem('theme-preferences');
      if (saved) {
        const data = JSON.parse(saved);
        Object.assign(this.$state, data);
        this.applyTheme();
        this.applyHighContrast();
      } else {
        // Check system preference
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        this.isDark = prefersDark;
        this.applyTheme();
      }
    },

    initialize() {
      this.loadFromLocalStorage();
      
      // Listen for system theme changes
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem('theme-preferences')) {
          this.isDark = e.matches;
          this.applyTheme();
        }
      });
    },
  },
});
