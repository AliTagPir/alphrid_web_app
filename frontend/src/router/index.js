import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../pages/LoginPage.vue'
import HomePage from '../pages/HomePage.vue'
import TrackerPage from '../pages/TrackerPage.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: LoginPage },
  { path: '/home', component: HomePage },
  { path: '/tracker', component: TrackerPage }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router