import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import About from '../views/About.vue'
import MyHotels from '../views/MyHotels.vue'
import MyBookings from '../views/MyBookings.vue'
import HotelDetails from '../views/HotelDetails.vue'
import Modification from '../views/Modification.vue'
import InfoHotel from '../views/InfoHotel.vue'
import HotelFilter from '../views/HotelFilter.vue'
import Hotel from '@/views/Hotel.vue'
import RegisterClient from '@/views/RegisterClient.vue'
import RegisterHotelOwner from '@/views/RegisterHotelOwner.vue'


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
    path: '/hotels/:id',
    name: 'Hotel',
    component: Hotel
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
  },
  {
    path: '/register_client',
    name: 'RegisterClient',
    component: RegisterClient
  },
  {
    path: '/register_hotel_owner',
    name: 'RegisterHotelOwner',
    component: RegisterHotelOwner
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
