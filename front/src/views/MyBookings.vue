<template>
  <hotel-owner-navbar :hotel_owner="this.hotel_owner" :is-my-hotel="false" />
</template>

<script>
import HotelOwnerNavbar from "../components/HotelOwnerNavbar";
export default {
  name: "MyBookings",
  components: {HotelOwnerNavbar},
  props: ['hotel_owner']
}
</script>

<style scoped>

</style>
