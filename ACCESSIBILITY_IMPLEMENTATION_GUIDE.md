# Accessibility Features Implementation Guide

## 🎯 Features to Implement (From Survey)

Based on the survey image you showed, these features need actual implementation:

### 1. 🔊 Text-to-Speech

**What it does:** Reads content aloud using browser's speech synthesis

**Implementation:**
```javascript
// Add to ProcessPage.vue or create a new composable

const speakText = (text) => {
  if ('speechSynthesis' in window) {
    // Cancel any ongoing speech
    window.speechSynthesis.cancel();
    
    const utterance = new SpeechSynthesisUtterance(text);
    
    // Configure voice based on user preferences
    const voices = window.speechSynthesis.getVoices();
    utterance.voice = voices.find(v => v.lang === 'en-US') || voices[0];
    utterance.rate = 1.0; // Normal speed
    utterance.pitch = 1.0;
    utterance.volume = 1.0;
    
    window.speechSynthesis.speak(utterance);
  } else {
    alert('Text-to-Speech not supported in your browser');
  }
};

const stopSpeaking = () => {
  window.speechSynthesis.cancel();
};
```

**Add to UI (ProcessPage.vue results section):**
```vue
<button
  v-if="survey.features.textToSpeech"
  @click="speakText(formatText(generatedContent.simplified))"
  class="px-4 py-2 bg-blue-500 text-white rounded-lg flex items-center gap-2"
>
  <span>🔊</span> Read Aloud
</button>
```

---

### 2. 📖 Dyslexia-Friendly Font

**What it does:** Applies OpenDyslexic font for easier reading

**Installation:**
```bash
# Download OpenDyslexic font
# Place in frontend/public/fonts/
```

**CSS (Add to style.css):**
```css
@font-face {
  font-family: 'OpenDyslexic';
  src: url('/fonts/OpenDyslexic-Regular.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}

.dyslexia-font {
  font-family: 'OpenDyslexic', sans-serif !important;
  letter-spacing: 0.05em;
  word-spacing: 0.1em;
  line-height: 1.8;
}
```

**Implementation (ProcessPage.vue):**
```vue
<div 
  :class="{ 'dyslexia-font': survey.features.dyslexiaFont }"
  class="prose prose-lg dark:prose-invert max-w-none"
>
  <div v-html="formatTextToHTML(generatedContent.simplified)"></div>
</div>
```

---

### 3. 🎨 High Contrast Mode

**What it does:** Increases color contrast for better visibility

**CSS (Add to style.css):**
```css
.high-contrast {
  --text-color: #000000;
  --bg-color: #FFFFFF;
  --border-color: #000000;
  filter: contrast(1.5);
}

.dark .high-contrast {
  --text-color: #FFFFFF;
  --bg-color: #000000;
  --border-color: #FFFFFF;
  filter: contrast(1.8);
}

.high-contrast * {
  color: var(--text-color) !important;
  background-color: var(--bg-color) !important;
  border-color: var(--border-color) !important;
}
```

**Implementation (ProcessPage.vue):**
```vue
<div 
  :class="{ 'high-contrast': survey.features.highContrast }"
  class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8"
>
  <!-- Content -->
</div>
```

---

### 4. 🖼️ Image Descriptions (AI-Generated)

**What it does:** Uses Gemini Vision API to generate alt text for images

**Already implemented in gemini.service.js!**
```javascript
async generateImageAltText(imageData, context = '') { ... }
```

**Implementation for uploaded PDFs with images:**

1. **Extract images from PDF (backend/services/document_processor.py):**
```python
# Already partially implemented
# Returns: { 'images': [...], 'has_images': True }
```

2. **Process images on frontend:**
```javascript
// In ProcessPage.vue processWithAI()
if (extractedData.has_images) {
  processingSteps.value[5] = {
    name: 'Generating Image Descriptions',
    description: 'Creating alt text for images...',
    status: 'processing'
  };
  
  for (const image of extractedData.images) {
    const altText = await geminiService.generateImageAltText(
      image.data,
      additionalContext.value
    );
    image.altText = altText.altText;
  }
  
  processingSteps.value[5].status = 'complete';
}
```

3. **Display with alt text:**
```vue
<div v-if="generatedContent.images?.length > 0">
  <h3>Images with Descriptions</h3>
  <div v-for="(img, idx) in generatedContent.images" :key="idx">
    <img :src="img.src" :alt="img.altText" />
    <p class="image-description">{{ img.altText }}</p>
  </div>
</div>
```

---

## 🎯 Complete Implementation Example

### Create `useAccessibility.js` composable:

```javascript
// frontend/src/composables/useAccessibility.js

import { ref, watch } from 'vue';

export function useAccessibility(survey) {
  const isSpeaking = ref(false);
  
  // Text-to-Speech
  const speak = (text) => {
    if (!survey.features.textToSpeech) return;
    
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      
      const utterance = new SpeechSynthesisUtterance(text);
      const voices = window.speechSynthesis.getVoices();
      utterance.voice = voices.find(v => v.lang === 'en-US') || voices[0];
      
      utterance.onstart = () => { isSpeaking.value = true; };
      utterance.onend = () => { isSpeaking.value = false; };
      
      window.speechSynthesis.speak(utterance);
    }
  };
  
  const stopSpeaking = () => {
    window.speechSynthesis.cancel();
    isSpeaking.value = false;
  };
  
  // Font class
  const fontClass = computed(() => {
    return survey.features.dyslexiaFont ? 'dyslexia-font' : '';
  });
  
  // Contrast class
  const contrastClass = computed(() => {
    return survey.features.highContrast ? 'high-contrast' : '';
  });
  
  // Combined classes
  const accessibilityClasses = computed(() => {
    return [fontClass.value, contrastClass.value].filter(Boolean).join(' ');
  });
  
  return {
    speak,
    stopSpeaking,
    isSpeaking,
    fontClass,
    contrastClass,
    accessibilityClasses
  };
}
```

### Use in ProcessPage.vue:

```vue
<script setup>
import { useAccessibility } from '../composables/useAccessibility';

// ... existing code ...

const { speak, stopSpeaking, isSpeaking, accessibilityClasses } = useAccessibility(survey);
</script>

<template>
  <div :class="accessibilityClasses">
    <!-- Content with accessibility applied -->
    
    <button 
      v-if="survey.features.textToSpeech"
      @click="speak(formatText(generatedContent.simplified))"
      class="px-4 py-2 bg-blue-500 text-white rounded-lg"
    >
      {{ isSpeaking ? '⏸️ Stop' : '🔊 Read Aloud' }}
    </button>
  </div>
</template>
```

---

## 🚀 Quick Start Implementation

1. **Add TTS buttons** to each content section (10 minutes)
2. **Download OpenDyslexic font** and add CSS (15 minutes)
3. **Create high-contrast CSS** classes (10 minutes)
4. **Create useAccessibility composable** (20 minutes)
5. **Test each feature** with survey selections (15 minutes)

**Total time: ~70 minutes for all 4 features!**

---

## 📊 Testing Checklist

- [ ] Survey - Select "Text-to-Speech" → Upload file → See "Read Aloud" button
- [ ] Survey - Select "Dyslexia-Friendly Font" → Upload file → Text uses OpenDyslexic
- [ ] Survey - Select "High Contrast Mode" → Upload file → High contrast colors applied
- [ ] Survey - Select "Image Descriptions" → Upload PDF with images → See AI-generated alt text
- [ ] Test all features together
- [ ] Test on different browsers (Chrome, Firefox, Safari)
- [ ] Test with screen reader (NVDA, JAWS, VoiceOver)

---

## 💡 Pro Tips

1. **TTS:** Add playback controls (pause, resume, speed adjustment)
2. **Font:** Let users choose font size multiplier
3. **Contrast:** Offer different contrast levels (moderate, high, maximum)
4. **Images:** Cache generated alt text to avoid re-processing

---

## 🎉 After Implementation

Your app will have:
- ✅ Real AI processing with Gemini
- ✅ Personalized content based on survey
- ✅ Study flashcards
- ✅ Full accessibility features working
- ✅ Truly adaptive learning experience

**This will be a complete, production-ready accessible learning platform! 🚀**
