import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import Confidentiality from '../views/Confidentiality.vue'
import About from '../views/AboutUs.vue'
import CheckCancer from '../views/CheckCancer.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomePage
    },
    {
        path: '/confidentiality',
        name: 'Confidentiality',
        component: Confidentiality
    },
    {
        path: '/check-cancer',
        name: 'CheckCancer',
        component: CheckCancer
    },
    {
        path: '/about',
        name: 'About',
        component: About
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition
        } else {
            return { x: 0, y: 0 }
        }
    }
})

export default router
 
