import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import About from '../views/About.vue'
import MyHotels from '../views/MyHotels.vue'
import MyBookings from '../views/MyBookings.vue'
import HotelFilter from '../views/HotelFilter.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/my_hotels',
    name: 'MyHotels',
    component: MyHotels
  },
  {
    path: '/my_bookings',
    name: 'MyBookins',
    component: MyBookings
  },
  {
	path: '/Hotelfilter',
	name: 'HotelFilter',
	component: HotelFilter.vue
}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
