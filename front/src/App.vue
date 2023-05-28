<template>
  <div>
    <Navbar />
    <router-view/>
    <!-- Contenu de la page ici -->

    <footer class="my-footer py-3 footer-bottom" :style="['/login', '/register_client', '/register_hotel_owner', '/my_hotels', '/my_bookings'].includes($route.path) || $route.path.startsWith('/modification/') ? 'position: fixed; left: 0; bottom: 0; width: 100%;' :''">
      <div class="footer-container">
        <div class="row">
          <div class="col-md-12 text-center">
            <a href="#" class="custom-footer">Big_bnb.inc</a>
            <router-link to="/login" class="custom-footer">Privacy</router-link>
            <a href="#" class="custom-footer">Terms and Conditions</a>
            <a href="#" class="custom-footer">Site map</a>
            <router-link to="/about" class="custom-footer">Infos</router-link>
          </div>
        </div>
      </div>
    </footer>
  </div>

</template>


<style lang="scss">
  @import './assets/variables.scss';
</style>

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

<style scoped>
/* .footer-container{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-gap: 10px;
} */
.custom-footer {
  display: inline-block;
  background-color: #75ABBC;
  text-decoration: none;
  color: whitesmoke;
  padding-right: 15px;
  padding-left: 15px;

}

a.custom-footer:hover {
  text-decoration: underline;
}
</style>
