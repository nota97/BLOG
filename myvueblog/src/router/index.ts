import HelloWorldVue from '@/components/HelloWorld.vue'
import HomeitemVue from '@/components/Homeitem.vue'
import HomeKnowitem from '@/components/HomeKnowitem.vue'
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      children: [{path: '/home/helloworld',component: HelloWorldVue},{path: '/',component:HomeitemVue},{path: '/home/knowitem/:index',name:'knowitem',component:HomeKnowitem}]
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/lx',
      name: 'lx',
      component: () => import('../views/LxView.vue')
    },
    {
      path: '/bloglist',
      name: 'bloglist',
      component: () => import('../views/BlogListView.vue')
    },
    {
      path: '/blogadd',
      name: 'blogadd',
      component: () => import('../views/BlogAddView.vue')
    },
    {
      path: '/blogedit',
      name: 'blogedit',
      component: () => import('../views/BlogEditView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
  ]
})

export default router
