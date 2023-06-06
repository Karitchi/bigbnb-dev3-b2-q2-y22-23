<template>
  <div>
    <Navbar />
    <router-view/>
    <Footer :style="['/login', '/register_client', '/register_hotel_owner', '/my_hotels', '/my_bookings', '/add_hotel'].includes($route.path) || $route.path.startsWith('/modification/') ? 'position: fixed; left: 0; bottom: 0; width: 100%;' : ''"/>
  </div>
</template>

<script lang="ts">
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    Footer,
  }
}
</script>