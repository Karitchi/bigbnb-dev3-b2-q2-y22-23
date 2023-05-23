import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import About from '../views/About.vue'
import MyHotels from '../views/MyHotels.vue'
import MyBookings from '../views/MyBookings.vue'
import Modification from '../views/Modification.vue'
import InfoHotel from '../views/InfoHotel.vue'
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
    path: '/modification/:id',
    name: 'Modification',
    component: Modification
  },
  {
    path: '/hotel_info/:id',
    name: 'InfoHotel',
    component: InfoHotel
  },
  {
	path: '/filter_hotels',
	name: 'HotelFilter',
	component: HotelFilter
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
