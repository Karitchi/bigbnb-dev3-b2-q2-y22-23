<template>
  <div>
    <Navbar />
    <router-view/>
    <!-- Contenu de la page ici -->

    <footer class="my-footer py-3">
      <div class="container">
        <div class="row">
          <div class="col-md-12 text-center">
            <a href="#" class="mx-2">big_bnb.inc</a>|
            <router-link to="/login" class="mx-2">Confidentialité</router-link>|
            <a href="#" class="mx-2">Conditions générales</a>|
            <a href="#" class="mx-2">Plan du site</a>|
            <router-link to="/about" class="mx-2">Infos de l'entreprise</router-link>|
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
