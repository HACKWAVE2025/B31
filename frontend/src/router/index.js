import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '../stores/auth';

const routes = [
  {
    path: '/',
    redirect: '/dashboard',
  },
  {
    path: '/dashboard',
    component: () => import('../layouts/DashboardLayout.vue'),
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
  // Skip all authentication - go straight to dashboard
  next();
});

export default router;
