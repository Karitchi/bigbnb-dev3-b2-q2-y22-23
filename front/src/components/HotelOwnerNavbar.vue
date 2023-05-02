<template>
  <ul v-if="isMyHotel" class="nav justify-content-center">
    <li class="nav-item ">
      <router-link to="/my_hotels" class="nav-link disabled"><h2>Mes hôtels</h2></router-link>
    </li>
    <li class="nav-item">
      <router-link  to="/my_bookings" class="nav-link active"><h2>Mes réservations</h2></router-link>
    </li>
  </ul>

  <ul v-else class="nav justify-content-center">
    <li class="nav-item">
      <router-link to="/my_hotels" class="nav-link active"><h2>Mes hôtels</h2></router-link>
    </li>
    <li class="nav-item">
      <router-link  to="/my_bookings" class="nav-link disabled"><h2>Mes réservations</h2></router-link>
    </li>
  </ul>
</template>

<style scoped>
ul {
  margin: 10px;
}

.active {
  text-decoration: #0D6EFD underline 3px;
}
</style>

<script>
export default {
  name: "HotelOwnerNavbar",
  props: ['hotel_owner', 'isMyHotel']
}
</script>

<style scoped>

</style>
