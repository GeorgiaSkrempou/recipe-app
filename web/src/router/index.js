import {
  createRouter,
  createWebHistory,
} from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'public.home',
    component: () => import(/* webpackChunkName: 'about' */ '../views/Home.vue'),
  },
  {
    path: '/login',
    name: 'public.login',
    component: () => import(/* webpackChunkName: 'login' */ '../views/Login.vue'),
  },
  {
    path: '/admin',
    name: 'admin.dashboard',
    component: () => import(/* webpackChunkName: 'admin.dashboard' */'../views/admin/Dashboard.vue'),
    children: [
      {
        path: '',
        name: 'admin.recipes.all',
        component: () => import(/* webpackChunkName: 'admin.workouts' */'../views/admin/AllRecipes.vue'),
      },
      {
        path: '/add',
        name: 'admin.recipes.add',
        component: () => import(/* webpackChunkName: 'admin.workouts' */'../views/admin/Add.vue'),
      },
    ],
  },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});