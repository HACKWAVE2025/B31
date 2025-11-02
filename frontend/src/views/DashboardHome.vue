<template>
  <div class="relative w-full min-h-screen overflow-x-hidden">
    <!-- Background Effects - Same as Landing Page -->
    <DitherBackground v-if="isDark" />
    <div v-else class="fixed top-0 left-0 w-full h-full z-0">
      <Iridescence
        :color="[1, 1, 1]"
        :mouseReact="true"
        :amplitude="0.1"
        :speed="1.0"
      />
    </div>

    <!-- Main Content -->
    <div class="relative z-10 px-6 lg:px-12 py-16">
      <div class="max-w-7xl mx-auto space-y-20">
        
        <!-- Welcome Section with Gradient -->
        <div class="relative overflow-hidden rounded-3xl p-10 lg:p-14 shadow-2xl transition-all duration-500"
          :style="{
            background: isDark 
              ? 'linear-gradient(135deg, rgba(0, 0, 0, 0.6) 0%, rgba(30, 30, 30, 0.8) 100%)'
              : 'linear-gradient(135deg, rgba(255, 255, 255, 0.7) 0%, rgba(240, 240, 255, 0.9) 100%)',
            backdropFilter: 'blur(20px)',
            border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
          }"
        >
          <div class="relative z-10">
            <h1 class="font-sora font-extrabold text-4xl lg:text-5xl mb-3 transition-colors duration-500 uppercase"
              :style="{ color: textColor }">
              <DecryptedText
                :text="`Welcome back, ${authStore.user?.displayName || 'there'}! 👋`"
                :speed="100"
                :maxIterations="10"
                :sequential="true"
                revealDirection="start"
                animateOn="view"
              />
            </h1>
            <p class="font-inter text-lg lg:text-xl mb-4 transition-colors duration-500"
              :style="{ color: secondaryTextColor }">
              {{ greetingMessage }}
            </p>
            
            <!-- Activity Summary -->
            <div class="flex flex-wrap gap-6 mb-10 py-4">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full flex items-center justify-center transition-all duration-500"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
                  }">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z" :stroke="textColor" stroke-width="2"/>
                    <path d="M13 2v7h7" :stroke="textColor" stroke-width="2"/>
                  </svg>
                </div>
                <div>
                  <p class="font-sora font-bold text-2xl transition-colors duration-500" :style="{ color: textColor }">
                    {{ stats.uploads }}
                  </p>
                  <p class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
                    Total Uploads
                  </p>
                </div>
              </div>
              
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full flex items-center justify-center transition-all duration-500"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
                  }">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                    <path d="M22 4L12 14.01l-3-3" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                  </svg>
                </div>
                <div>
                  <p class="font-sora font-bold text-2xl transition-colors duration-500" :style="{ color: textColor }">
                    {{ stats.processed }}
                  </p>
                  <p class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
                    Processed Files
                  </p>
                </div>
              </div>
              
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full flex items-center justify-center transition-all duration-500"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
                  }">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <circle cx="12" cy="12" r="10" :stroke="textColor" stroke-width="2"/>
                    <path d="M12 6v6l4 2" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                  </svg>
                </div>
                <div>
                  <p class="font-sora font-bold text-2xl transition-colors duration-500" :style="{ color: textColor }">
                    {{ recentActivity }}
                  </p>
                  <p class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
                    Recent Activity
                  </p>
                </div>
              </div>
            </div>

            <div class="flex flex-wrap gap-6">
              <router-link
                to="/dashboard/upload"
                class="px-8 py-4 rounded-full font-inter font-bold shadow-lg transition-all duration-300 hover:scale-105 flex items-center gap-3"
                :style="{
                  backgroundColor: isDark ? '#ffffff' : '#000000',
                  color: isDark ? '#000000' : '#ffffff'
                }"
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12" :stroke="isDark ? '#000000' : '#ffffff'" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                Upload New Material
              </router-link>
              <router-link
                v-if="!authStore.user?.surveyCompleted"
                to="/dashboard/survey"
                class="px-8 py-4 rounded-full font-inter font-bold border-2 transition-all duration-300 hover:opacity-80"
                :style="{
                  color: textColor,
                  borderColor: isDark ? 'rgba(255, 255, 255, 0.3)' : 'rgba(0, 0, 0, 0.3)',
                  background: 'transparent'
                }"
              >
                Complete Your Profile Survey
              </router-link>
            </div>
          </div>
        </div>

        <!-- Stats Cards with BounceCards Effect -->
        <div class="mt-24">
          <BlurText
            text="YOUR STATISTICS"
            :delay="100"
            animateBy="words"
            direction="top"
            as="h2"
            className="font-sora font-extrabold text-3xl lg:text-4xl mb-12 text-center uppercase tracking-wide transition-colors duration-500"
            :style="{ color: textColor }"
          />
          
          <div class="flex justify-center">
            <BounceCards
              :items="statsCards"
              :containerWidth="1000"
              :containerHeight="300"
              :animationDelay="0.3"
              :animationStagger="0.08"
              easeType="elastic.out(1, 0.8)"
              :transformStyles="statsTransforms"
              :enableHover="true"
            />
          </div>
        </div>

        <!-- Progress Tracker & Notifications Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 mt-24">
          <!-- Progress Tracker Section -->
          <div class="rounded-3xl shadow-xl overflow-hidden transition-all duration-500"
            :style="{
              background: isDark 
                ? 'rgba(0, 0, 0, 0.4)'
                : 'rgba(255, 255, 255, 0.6)',
              backdropFilter: 'blur(20px)',
              border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
            }">
            <div class="p-8">
              <div class="flex items-center gap-3 mb-6">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
                  <circle cx="12" cy="12" r="10" :stroke="textColor" stroke-width="2"/>
                  <path d="M12 6v6l4 2" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
                <h2 class="font-sora font-bold text-2xl transition-colors duration-500"
                  :style="{ color: textColor }">
                  Progress Tracker
                </h2>
              </div>

              <!-- Progress Overview -->
              <div class="mb-6">
                <div class="flex justify-between items-center mb-3">
                  <p class="font-inter text-lg font-semibold transition-colors duration-500" :style="{ color: textColor }">
                    {{ stats.processed }} of {{ stats.uploads }} files fully processed
                  </p>
                  <p class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
                    {{ completionRate }}%
                  </p>
                </div>
                
                <!-- Progress Bar -->
                <div class="w-full h-3 rounded-full overflow-hidden transition-all duration-500"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
                  }">
                  <div 
                    class="h-full rounded-full transition-all duration-1000 ease-out"
                    :style="{
                      width: `${completionRate}%`,
                      background: isDark 
                        ? 'linear-gradient(90deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.5))'
                        : 'linear-gradient(90deg, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.5))'
                    }">
                  </div>
                </div>
              </div>

              <!-- Accessibility Completion Rate -->
              <div class="rounded-2xl p-6 transition-all duration-500"
                :style="{
                  background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                }">
                <p class="font-inter text-sm font-semibold mb-2 transition-colors duration-500" :style="{ color: textColor }">
                  Accessibility Completion Rate
                </p>
                <p class="font-inter text-sm leading-relaxed transition-colors duration-500" :style="{ color: secondaryTextColor }">
                  Your content is {{ accessibilityScore }}% accessible. Keep up the great work making education inclusive for everyone!
                </p>
                
                <!-- Recent Processing Stats -->
                <div class="grid grid-cols-2 gap-4 mt-4">
                  <div>
                    <p class="font-sora font-bold text-xl transition-colors duration-500" :style="{ color: textColor }">
                      {{ stats.processed }}
                    </p>
                    <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                      Completed
                    </p>
                  </div>
                  <div>
                    <p class="font-sora font-bold text-xl transition-colors duration-500" :style="{ color: textColor }">
                      {{ stats.uploads - stats.processed }}
                    </p>
                    <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                      In Progress
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Notifications / Insights Section -->
          <div class="rounded-3xl shadow-xl overflow-hidden transition-all duration-500"
            :style="{
              background: isDark 
                ? 'rgba(0, 0, 0, 0.4)'
                : 'rgba(255, 255, 255, 0.6)',
              backdropFilter: 'blur(20px)',
              border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
            }">
            <div class="p-8">
              <div class="flex items-center gap-3 mb-6">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
                  <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9M13.73 21a2 2 0 0 1-3.46 0" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
                <h2 class="font-sora font-bold text-2xl transition-colors duration-500"
                  :style="{ color: textColor }">
                  Accessibility Insights
                </h2>
              </div>

              <!-- Insights List -->
              <div class="space-y-4">
                <div 
                  v-for="(insight, idx) in accessibilityInsights" 
                  :key="idx"
                  class="flex gap-4 p-4 rounded-xl transition-all duration-300 hover:scale-[1.02]"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                  }">
                  <div class="flex-shrink-0 mt-1">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                      <path :d="getInsightIcon(insight.type)" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                  </div>
                  <div class="flex-1">
                    <p class="font-inter text-sm font-semibold mb-1 transition-colors duration-500" :style="{ color: textColor }">
                      {{ insight.title }}
                    </p>
                    <p class="font-inter text-sm leading-relaxed transition-colors duration-500" :style="{ color: secondaryTextColor }">
                      {{ insight.description }}
                    </p>
                  </div>
                </div>

                <!-- No Insights State -->
                <div v-if="accessibilityInsights.length === 0" class="text-center py-8">
                  <svg class="w-16 h-16 mx-auto mb-4" viewBox="0 0 24 24" fill="none">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" :stroke="secondaryTextColor" stroke-width="2" stroke-linecap="round"/>
                    <path d="M22 4L12 14.01l-3-3" :stroke="secondaryTextColor" stroke-width="2" stroke-linecap="round"/>
                  </svg>
                  <p class="font-inter text-sm transition-colors duration-500" :style="{ color: secondaryTextColor }">
                    Great job! All your content meets accessibility standards.
                  </p>
                </div>
              </div>

              <!-- View All Insights Button -->
              <button 
                class="w-full mt-6 px-6 py-3 rounded-full font-inter font-semibold text-sm transition-all duration-300 hover:scale-[1.02]"
                :style="{
                  background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                  color: textColor
                }">
                View All Insights
              </button>
            </div>
          </div>
        </div>

        <!-- User Settings & Help Support Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 mt-24">
          <!-- User Settings Section -->
          <div class="rounded-3xl shadow-xl overflow-hidden transition-all duration-500"
            :style="{
              background: isDark 
                ? 'rgba(0, 0, 0, 0.4)'
                : 'rgba(255, 255, 255, 0.6)',
              backdropFilter: 'blur(20px)',
              border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
            }">
            <div class="p-8">
              <div class="flex items-center gap-3 mb-6">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
                  <circle cx="12" cy="12" r="3" :stroke="textColor" stroke-width="2"/>
                  <path d="M12 1v6m0 6v6M5.64 5.64l4.24 4.24m4.24 4.24l4.24 4.24M1 12h6m6 0h6M5.64 18.36l4.24-4.24m4.24-4.24l4.24-4.24" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
                <h2 class="font-sora font-bold text-2xl transition-colors duration-500"
                  :style="{ color: textColor }">
                  Accessibility Preferences
                </h2>
              </div>

              <!-- Settings Options -->
              <div class="space-y-5">
                <div class="flex items-center justify-between p-4 rounded-xl transition-all duration-500"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                  }">
                  <div class="flex items-center gap-3">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                      <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z" :stroke="textColor" stroke-width="2"/>
                      <path d="M19 10v2a7 7 0 0 1-14 0v-2M12 19v4M8 23h8" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                    <div>
                      <p class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">
                        Text-to-Speech Voice
                      </p>
                      <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                        {{ userPreferences.ttsVoice }}
                      </p>
                    </div>
                  </div>
                  <router-link to="/dashboard/settings" class="font-inter text-xs px-3 py-1 rounded-full transition-all hover:scale-105"
                    :style="{
                      background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                      color: textColor
                    }">
                    Change
                  </router-link>
                </div>

                <div class="flex items-center justify-between p-4 rounded-xl transition-all duration-500"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                  }">
                  <div class="flex items-center gap-3">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                      <path d="M4 7V4h16v3M9 20h6M12 4v16" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                    <div>
                      <p class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">
                        Font Type
                      </p>
                      <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                        {{ userPreferences.fontType }}
                      </p>
                    </div>
                  </div>
                  <router-link to="/dashboard/settings" class="font-inter text-xs px-3 py-1 rounded-full transition-all hover:scale-105"
                    :style="{
                      background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                      color: textColor
                    }">
                    Change
                  </router-link>
                </div>

                <div class="flex items-center justify-between p-4 rounded-xl transition-all duration-500"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                  }">
                  <div class="flex items-center gap-3">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                      <circle cx="12" cy="12" r="10" :stroke="textColor" stroke-width="2"/>
                      <path d="M8 12h8M12 8v8" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                    <div>
                      <p class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">
                        Color Contrast
                      </p>
                      <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                        {{ userPreferences.colorContrast }}
                      </p>
                    </div>
                  </div>
                  <router-link to="/dashboard/settings" class="font-inter text-xs px-3 py-1 rounded-full transition-all hover:scale-105"
                    :style="{
                      background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                      color: textColor
                    }">
                    Change
                  </router-link>
                </div>

                <div class="flex items-center justify-between p-4 rounded-xl transition-all duration-500"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                  }">
                  <div class="flex items-center gap-3">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                      <circle cx="12" cy="12" r="10" :stroke="textColor" stroke-width="2"/>
                      <path d="M2 12h20" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                      <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" :stroke="textColor" stroke-width="2"/>
                    </svg>
                    <div>
                      <p class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">
                        Language
                      </p>
                      <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                        {{ userPreferences.language }}
                      </p>
                    </div>
                  </div>
                  <router-link to="/dashboard/settings" class="font-inter text-xs px-3 py-1 rounded-full transition-all hover:scale-105"
                    :style="{
                      background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)',
                      color: textColor
                    }">
                    Change
                  </router-link>
                </div>
              </div>

              <!-- Go to Settings -->
              <router-link to="/dashboard/settings"
                class="block w-full mt-6 px-6 py-3 rounded-full font-inter font-semibold text-sm text-center transition-all duration-300 hover:scale-[1.02]"
                :style="{
                  background: isDark ? '#ffffff' : '#000000',
                  color: isDark ? '#000000' : '#ffffff'
                }">
                View All Settings
              </router-link>
            </div>
          </div>

          <!-- Help & Support Section -->
          <div class="rounded-3xl shadow-xl overflow-hidden transition-all duration-500"
            :style="{
              background: isDark 
                ? 'rgba(0, 0, 0, 0.4)'
                : 'rgba(255, 255, 255, 0.6)',
              backdropFilter: 'blur(20px)',
              border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
            }">
            <div class="p-8">
              <div class="flex items-center gap-3 mb-6">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
                  <circle cx="12" cy="12" r="10" :stroke="textColor" stroke-width="2"/>
                  <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3M12 17h.01" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
                <h2 class="font-sora font-bold text-2xl transition-colors duration-500"
                  :style="{ color: textColor }">
                  Help & Support
                </h2>
              </div>

              <p class="font-inter text-sm leading-relaxed mb-6 transition-colors duration-500" :style="{ color: secondaryTextColor }">
                Need help? Access quick tutorials, FAQs, or contact our support team for accessibility troubleshooting and guidance.
              </p>

              <!-- Help Resources -->
              <div class="space-y-4">
                <a href="#tutorials" 
                  class="flex items-center gap-4 p-4 rounded-xl transition-all duration-300 hover:scale-[1.02] hover:translate-x-1"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                  }">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <polygon points="5 3 19 12 5 21 5 3" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <div>
                    <p class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">
                      Quick Tutorials
                    </p>
                    <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                      Watch step-by-step guides
                    </p>
                  </div>
                </a>

                <a href="#faqs" 
                  class="flex items-center gap-4 p-4 rounded-xl transition-all duration-300 hover:scale-[1.02] hover:translate-x-1"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                  }">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                  </svg>
                  <div>
                    <p class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">
                      FAQs
                    </p>
                    <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                      Find answers to common questions
                    </p>
                  </div>
                </a>

                <a href="mailto:skillsetai.cw@gmail.com" 
                  class="flex items-center gap-4 p-4 rounded-xl transition-all duration-300 hover:scale-[1.02] hover:translate-x-1"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                  }">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" :stroke="textColor" stroke-width="2"/>
                    <path d="M22 6l-10 7L2 6" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                  </svg>
                  <div>
                    <p class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">
                      Contact Support
                    </p>
                    <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                      Get personalized assistance
                    </p>
                  </div>
                </a>

                <a href="#docs" 
                  class="flex items-center gap-4 p-4 rounded-xl transition-all duration-300 hover:scale-[1.02] hover:translate-x-1"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                  }">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" :stroke="textColor" stroke-width="2"/>
                  </svg>
                  <div>
                    <p class="font-inter text-sm font-semibold transition-colors duration-500" :style="{ color: textColor }">
                      Documentation
                    </p>
                    <p class="font-inter text-xs transition-colors duration-500" :style="{ color: secondaryTextColor }">
                      Read detailed guides
                    </p>
                  </div>
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Recent Activity Section -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 mt-24">
          <!-- Recent Uploads -->
          <div class="rounded-3xl shadow-xl overflow-hidden transition-all duration-500"
            :style="{
              background: isDark 
                ? 'rgba(0, 0, 0, 0.4)'
                : 'rgba(255, 255, 255, 0.6)',
              backdropFilter: 'blur(20px)',
              border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
            }"
          >
            <div class="p-6 border-b transition-colors duration-500"
              :style="{ borderColor: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)' }">
              <div class="flex items-center justify-between">
                <h2 class="font-sora font-bold text-2xl transition-colors duration-500"
                  :style="{ color: textColor }">
                  Recent Uploads
                </h2>
                <router-link
                  to="/dashboard/history"
                  class="font-inter text-sm font-semibold hover:opacity-70 transition-opacity"
                  :style="{ color: textColor }"
                >
                  View all →
                </router-link>
              </div>
            </div>
            <div class="p-6">
              <div v-if="contentStore.recentUploads.length === 0" class="text-center py-16">
                <svg class="w-20 h-20 mx-auto mb-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z" :stroke="secondaryTextColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M13 2v7h7" :stroke="secondaryTextColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <p class="font-inter transition-colors duration-500" :style="{ color: secondaryTextColor }">
                  No uploads yet
                </p>
                <router-link 
                  to="/dashboard/upload" 
                  class="font-inter inline-block mt-4 hover:opacity-70 transition-opacity font-semibold"
                  :style="{ color: textColor }"
                >
                  Upload your first file
                </router-link>
              </div>
              <div v-else class="space-y-4">
                <div
                  v-for="upload in contentStore.recentUploads"
                  :key="upload.id"
                  class="flex items-center justify-between p-4 rounded-xl transition-all duration-300 hover:scale-[1.02] cursor-pointer"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                  }"
                >
                  <div class="flex items-center space-x-4 flex-1 min-w-0">
                    <div class="flex-shrink-0">
                      <svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M13 2v7h7" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                    </div>
                    <div class="flex-1 min-w-0">
                      <p class="font-inter text-sm font-semibold truncate transition-colors duration-500"
                        :style="{ color: textColor }">
                        {{ upload.fileName }}
                      </p>
                      <p class="font-inter text-xs transition-colors duration-500"
                        :style="{ color: secondaryTextColor }">
                        {{ formatDate(upload.uploadedAt || upload.createdAt) }}
                      </p>
                    </div>
                  </div>
                  <span class="px-3 py-1 rounded-full text-xs font-inter font-semibold"
                    :style="{
                      background: isDark ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.2)',
                      color: textColor
                    }">
                    {{ upload.status }}
                  </span>
                </div>
              </div>
            </div>
          </div>

          <!-- Saved Content -->
          <div class="rounded-3xl shadow-xl overflow-hidden transition-all duration-500"
            :style="{
              background: isDark 
                ? 'rgba(0, 0, 0, 0.4)'
                : 'rgba(255, 255, 255, 0.6)',
              backdropFilter: 'blur(20px)',
              border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)'
            }"
          >
            <div class="p-6 border-b transition-colors duration-500"
              :style="{ borderColor: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)' }">
              <div class="flex items-center justify-between">
                <h2 class="font-sora font-bold text-2xl transition-colors duration-500"
                  :style="{ color: textColor }">
                  Saved Content
                </h2>
                <router-link
                  to="/dashboard/saved"
                  class="font-inter text-sm font-semibold hover:opacity-70 transition-opacity"
                  :style="{ color: textColor }"
                >
                  View all →
                </router-link>
              </div>
            </div>
            <div class="p-6">
              <div v-if="contentStore.savedContent.length === 0" class="text-center py-16">
                <svg class="w-20 h-20 mx-auto mb-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" :stroke="secondaryTextColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <p class="font-inter transition-colors duration-500" :style="{ color: secondaryTextColor }">
                  No saved content yet
                </p>
              </div>
              <div v-else class="space-y-4">
                <div
                  v-for="saved in contentStore.savedContent.slice(0, 5)"
                  :key="saved.id"
                  class="flex items-center justify-between p-4 rounded-xl transition-all duration-300 hover:scale-[1.02] cursor-pointer"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)'
                  }"
                >
                  <div class="flex items-center space-x-4 flex-1 min-w-0">
                    <div class="flex-shrink-0">
                      <svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                    </div>
                    <div class="flex-1 min-w-0">
                      <p class="font-inter text-sm font-semibold truncate transition-colors duration-500"
                        :style="{ color: textColor }">
                        Processed Content
                      </p>
                      <p class="font-inter text-xs transition-colors duration-500"
                        :style="{ color: secondaryTextColor }">
                        {{ formatDate(saved.savedAt) }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Actions with BounceCards -->
        <div class="mt-24">
          <BlurText
            text="QUICK ACTIONS"
            :delay="100"
            animateBy="words"
            direction="top"
            as="h2"
            className="font-sora font-extrabold text-3xl lg:text-4xl mb-12 text-center uppercase tracking-wide transition-colors duration-500"
            :style="{ color: textColor }"
          />
          
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 max-w-6xl mx-auto">
            <router-link
              v-for="(action, idx) in quickActions"
              :key="idx"
              :to="action.link"
              class="block transform transition-all duration-300 hover:scale-105 cursor-pointer"
            >
              <div
                class="rounded-2xl p-8 h-full flex flex-col items-center text-center shadow-xl transition-all duration-500"
                :style="{
                  background: isDark 
                    ? 'rgba(255, 255, 255, 0.05)'
                    : 'rgba(255, 255, 255, 0.6)',
                  backdropFilter: 'blur(20px)',
                  border: isDark ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.2)'
                }"
              >
                <!-- Icon -->
                <div class="mb-6 w-16 h-16 rounded-full flex items-center justify-center transition-all duration-500"
                  :style="{
                    background: isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)'
                  }">
                  <!-- Upload File Icon -->
                  <svg v-if="action.title === 'Upload File'" width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <!-- View History Icon -->
                  <svg v-else-if="action.title === 'View History'" width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="12" cy="12" r="10" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M12 6v6l4 2" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <!-- Saved Content Icon -->
                  <svg v-else-if="action.title === 'Saved Content'" width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" :stroke="textColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <!-- Settings Icon -->
                  <svg v-else-if="action.title === 'Settings'" width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="12" cy="12" r="3" :stroke="textColor" stroke-width="2"/>
                    <path d="M12 1v6m0 6v6M5.64 5.64l4.24 4.24m4.24 4.24l4.24 4.24M1 12h6m6 0h6M5.64 18.36l4.24-4.24m4.24-4.24l4.24-4.24" :stroke="textColor" stroke-width="2" stroke-linecap="round"/>
                  </svg>
                </div>
                
                <!-- Title -->
                <h3 class="font-sora font-bold text-xl mb-3 transition-colors duration-500"
                  :style="{ color: textColor }">
                  {{ action.title }}
                </h3>
                
                <!-- Description -->
                <p class="font-inter text-sm transition-colors duration-500"
                  :style="{ color: secondaryTextColor }">
                  {{ action.description }}
                </p>
              </div>
            </router-link>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useDark } from '@vueuse/core'
import { useAuthStore } from '../stores/auth'
import { useContentStore } from '../stores/content'
import DitherBackground from '../components/DitherBackground.vue'
import Iridescence from '../components/Iridescence.vue'
import DecryptedText from '../components/DecryptedText.vue'
import BlurText from '../components/BlurText.vue'
import BounceCards from '../components/BounceCards.vue'

const router = useRouter()
const authStore = useAuthStore()
const contentStore = useContentStore()
const isDark = useDark()

const textColor = computed(() => isDark.value ? '#ffffff' : '#000000')
const secondaryTextColor = computed(() => isDark.value ? 'rgba(255, 255, 255, 0.7)' : 'rgba(0, 0, 0, 0.7)')

// Progress Tracker
const completionRate = computed(() => {
  if (stats.value.uploads === 0) return 0
  return Math.round((stats.value.processed / stats.value.uploads) * 100)
})

const accessibilityScore = computed(() => {
  // Calculate based on processed files and quality
  const baseScore = completionRate.value
  const qualityBonus = Math.min(stats.value.processed * 2, 15)
  return Math.min(baseScore + qualityBonus, 100)
})

// Accessibility Insights
const accessibilityInsights = ref([
  {
    type: 'text',
    title: 'Simplify Long Sentences',
    description: 'Consider breaking down complex sentences in "Advanced Physics.pdf" for better readability.'
  },
  {
    type: 'image',
    title: 'Add Alternative Text',
    description: '2 images in "Biology Chapter 3.pdf" need descriptive alt text for screen readers.'
  },
  {
    type: 'contrast',
    title: 'Improve Color Contrast',
    description: 'Some text in "Chemistry Notes.pdf" has low contrast. Adjust for WCAG AA compliance.'
  }
])

// Helper to get insight icons
const getInsightIcon = (type) => {
  const icons = {
    'text': 'M4 7V4h16v3M9 20h6M12 4v16',
    'image': 'M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3',
    'contrast': 'M12 1a11 11 0 1 0 0 22 11 11 0 0 0 0-22zm0 5v12'
  }
  return icons[type] || icons['text']
}

// User Preferences
const userPreferences = ref({
  ttsVoice: 'Natural Female (English US)',
  fontType: 'OpenDyslexic',
  colorContrast: 'High Contrast',
  language: 'English (US)'
})

const stats = ref({
  uploads: 0,
  processed: 0,
  saved: 0,
})

const greetingMessage = computed(() => {
  const hour = new Date().getHours()
  if (hour < 12) return 'Good morning! Ready to make learning accessible?'
  if (hour < 18) return 'Good afternoon! Let\'s transform some content today.'
  return 'Good evening! Keep making education accessible for everyone.'
})

const statsCards = computed(() => [
  {
    title: 'Total Uploads',
    description: `${stats.value.uploads} files uploaded and ready for processing`,
    icon: '▲'
  },
  {
    title: 'Processed Files',
    description: `${stats.value.processed} documents successfully transformed`,
    icon: '■'
  },
  {
    title: 'Saved Items',
    description: `${stats.value.saved} items bookmarked for quick access`,
    icon: '●'
  }
])

const statsTransforms = [
  'rotate(5deg) translate(-200px)',
  'rotate(-3deg)',
  'rotate(5deg) translate(200px)'
]

const quickActions = [
  {
    title: 'Upload File',
    description: 'Upload documents, PDFs, or images for accessibility processing',
    link: '/dashboard/upload'
  },
  {
    title: 'View History',
    description: 'Browse through all your previously uploaded and processed files',
    link: '/dashboard/history'
  },
  {
    title: 'Saved Content',
    description: 'Access your bookmarked and favorite processed materials',
    link: '/dashboard/saved'
  },
  {
    title: 'Settings',
    description: 'Customize your preferences and accessibility options',
    link: '/dashboard/settings'
  }
]

const formatDate = (dateString) => {
  if (!dateString) return 'Unknown date'
  
  // Backend sends UTC timestamps without 'Z' suffix
  // If no timezone indicator, append 'Z' to treat as UTC
  let dateStr = dateString
  if (dateStr.includes('T') && !dateStr.includes('Z') && !dateStr.includes('+') && !dateStr.includes('-', 10)) {
    dateStr = dateStr + 'Z'
  }
  
  const date = new Date(dateStr)
  if (isNaN(date.getTime())) return 'Invalid date'
  
  const now = new Date()
  const diffMs = now - date
  const diffMins = Math.floor(diffMs / 60000)
  const diffHours = Math.floor(diffMs / 3600000)
  const diffDays = Math.floor(diffMs / 86400000)

  if (diffMins < 1) return 'Just now'
  if (diffMins < 60) return `${diffMins} min${diffMins > 1 ? 's' : ''} ago`
  if (diffHours < 24) return `${diffHours} hour${diffHours > 1 ? 's' : ''} ago`
  if (diffDays < 7) return `${diffDays} day${diffDays > 1 ? 's' : ''} ago`
  return date.toLocaleDateString()
}

onMounted(async () => {
  if (authStore.user) {
    await contentStore.fetchUserContent(authStore.user.uid)
    stats.value = {
      uploads: contentStore.uploads.length,
      processed: contentStore.processedContent.length,
      saved: contentStore.savedContent.length,
    }
  }
})
</script>

<style scoped>
/* Match landing page animations */
</style>
