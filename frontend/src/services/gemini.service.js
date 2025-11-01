import { GoogleGenerativeAI } from '@google/generative-ai';

const API_KEY = import.meta.env.VITE_GEMINI_API_KEY;

// Initialize Gemini AI
const genAI = new GoogleGenerativeAI(API_KEY);

class GeminiService {
  constructor() {
    this.model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash-exp' });
  }

  /**
   * Simplify complex text for better comprehension
   */
  async simplifyText(text, level = 'simple') {
    const prompts = {
      simple: `Simplify the following text to an 8th-grade reading level. Keep all important information but use simpler words and shorter sentences:\n\n${text}`,
      'very-simple': `Simplify the following text to a 5th-grade reading level. Use very simple words and short sentences:\n\n${text}`,
      medium: `Simplify the following text to a 10th-grade reading level. Make it easier to understand while maintaining technical accuracy:\n\n${text}`,
    };

    try {
      const result = await this.model.generateContent(prompts[level] || prompts.simple);
      const response = await result.response;
      return {
        success: true,
        simplifiedText: response.text(),
        originalText: text,
      };
    } catch (error) {
      console.error('Gemini simplification error:', error);
      return {
        success: false,
        error: error.message,
        simplifiedText: text,
      };
    }
  }

  /**
   * Generate comprehensive summary of text
   */
  async generateSummary(text, maxLength = 200) {
    const prompt = `Provide a comprehensive summary of the following text in about ${maxLength} words. Focus on key points and main ideas:\n\n${text}`;

    try {
      const result = await this.model.generateContent(prompt);
      const response = await result.response;
      return {
        success: true,
        summary: response.text(),
      };
    } catch (error) {
      console.error('Gemini summary error:', error);
      return {
        success: false,
        error: error.message,
        summary: '',
      };
    }
  }

  /**
   * Generate alternative text for images
   */
  async generateImageAltText(imageData, context = '') {
    const prompt = `Generate a detailed, accessible alternative text description for this image. ${
      context ? `Context: ${context}` : ''
    } The description should be clear and helpful for visually impaired users. Include important visual details, text in the image, and the overall purpose or message of the image.`;

    try {
      const model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash-exp' });
      const result = await model.generateContent([prompt, imageData]);
      const response = await result.response;
      return {
        success: true,
        altText: response.text(),
      };
    } catch (error) {
      console.error('Gemini image description error:', error);
      return {
        success: false,
        error: error.message,
        altText: 'Unable to generate description',
      };
    }
  }

  /**
   * Explain mathematical equations in plain language
   */
  async explainMath(equation) {
    const prompt = `Explain the following mathematical equation in simple, plain language. Break down what each part means and provide a step-by-step explanation:\n\nEquation: ${equation}\n\nProvide:\n1. What the equation represents\n2. Explanation of each component\n3. Step-by-step solution (if applicable)`;

    try {
      const result = await this.model.generateContent(prompt);
      const response = await result.response;
      return {
        success: true,
        explanation: response.text(),
      };
    } catch (error) {
      console.error('Gemini math explanation error:', error);
      return {
        success: false,
        error: error.message,
        explanation: '',
      };
    }
  }

  /**
   * Convert flowcharts or diagrams to text descriptions
   */
  async describeFlowchart(flowchartData, context = '') {
    const prompt = `Describe this flowchart or diagram in a clear, linear text format that can be easily understood by someone who cannot see the visual representation. ${
      context ? `Context: ${context}` : ''
    } Include:\n1. The overall purpose\n2. Each step in sequence\n3. Decision points and branches\n4. Final outcomes`;

    try {
      const model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash-exp' });
      const result = await model.generateContent([prompt, flowchartData]);
      const response = await result.response;
      return {
        success: true,
        description: response.text(),
      };
    } catch (error) {
      console.error('Gemini flowchart description error:', error);
      return {
        success: false,
        error: error.message,
        description: '',
      };
    }
  }

  /**
   * Generate key points from long content
   */
  async extractKeyPoints(text, numPoints = 5) {
    const prompt = `Extract the ${numPoints} most important key points from the following text. Present them as a numbered list:\n\n${text}`;

    try {
      const result = await this.model.generateContent(prompt);
      const response = await result.response;
      return {
        success: true,
        keyPoints: response.text(),
      };
    } catch (error) {
      console.error('Gemini key points error:', error);
      return {
        success: false,
        error: error.message,
        keyPoints: '',
      };
    }
  }

  /**
   * Describe chemistry diagrams and molecular structures
   */
  async describeChemistry(imageData, context = '') {
    const prompt = `Describe this chemistry diagram or molecular structure in detail for a visually impaired student. ${
      context ? `Context: ${context}` : ''
    } Include:\n1. The type of diagram (molecular structure, reaction, etc.)\n2. Elements and compounds present\n3. Bonds and connections\n4. Overall chemical significance`;

    try {
      const model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash-exp' });
      const result = await model.generateContent([prompt, imageData]);
      const response = await result.response;
      return {
        success: true,
        description: response.text(),
      };
    } catch (error) {
      console.error('Gemini chemistry description error:', error);
      return {
        success: false,
        error: error.message,
        description: '',
      };
    }
  }
}

export default new GeminiService();
