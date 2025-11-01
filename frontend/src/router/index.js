import { createRouter, createWebHistory } from 'vue-router';
import { watch } from 'vue';
import { useFirebaseAuth } from '../composables/useFirebaseAuth';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/HomePage.vue'),
  },
  {
    path: '/dashboard',
    component: () => import('../layouts/DashboardLayout.vue'),
    meta: { requiresAuth: true },
    children: [
      {
        path: '',
        name: 'Dashboard',
        component: () => import('../views/DashboardHome.vue'),
      },
      {
        path: 'upload',
        name: 'Upload',
        component: () => import('../views/UploadPage.vue'),
      },
      {
        path: 'survey',
        name: 'Survey',
        component: () => import('../views/SurveyPage.vue'),
      },
      {
        path: 'process/:id?',
        name: 'Process',
        component: () => import('../views/ProcessPage.vue'),
      },
      {
        path: 'content/:id',
        name: 'ContentViewer',
        component: () => import('../views/ContentViewer.vue'),
      },
      {
        path: 'profile',
        name: 'Profile',
        component: () => import('../views/ProfilePage.vue'),
      },
      {
        path: 'history',
        name: 'History',
        component: () => import('../views/HistoryPage.vue'),
      },
      {
        path: 'saved',
        name: 'SavedContent',
        component: () => import('../views/SavedContent.vue'),
      },
      {
        path: 'settings',
        name: 'Settings',
        component: () => import('../views/SettingsPage.vue'),
      },
    ],
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFound.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation guards
router.beforeEach(async (to, from, next) => {
  const { currentUser, isLoading } = useFirebaseAuth();
  
  // Wait for auth to initialize
  if (isLoading.value) {
    await new Promise(resolve => {
      const unwatch = watch(isLoading, (loading) => {
        if (!loading) {
          unwatch();
          resolve();
        }
      });
    });
  }

  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);

  if (requiresAuth && !currentUser.value) {
    // Redirect to home page if not authenticated
    next({ name: 'Home' });
  } else if (to.name === 'Home' && currentUser.value) {
    // Redirect to dashboard if already logged in and trying to access home
    next({ name: 'Dashboard' });
  } else {
    next();
  }
});

export default router;
