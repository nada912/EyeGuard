import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Confidentiality from '../views/Confidentiality.vue'
import About from '../views/AboutUs.vue'
import CheckCancer from '../views/CheckCancer.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
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

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
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
 
