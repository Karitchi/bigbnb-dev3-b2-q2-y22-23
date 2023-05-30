<template>
  <nav class="navbar navbar-expand-lg my-header bg-dark" data-bs-theme="dark">
    <div class="container-fluid">

      <router-link class="navbar-brand" to="/">Big bnb</router-link>
      <!-- <router-link class="navbar-brand" to="/"><img class="logo" src="../assets/logo2.png"></router-link> -->

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <div class="ms-auto">

          <div v-if="!this.connected">
            <router-link class="btn btn-dark me-2" to="/login">Se connecter</router-link>
            <router-link class="btn btn-dark ms-2" to="/register_client">S'inscrire</router-link>
          </div>

          <div v-else>
            <router-link to="/my_hotels" v-if="this.getUserType() === 'hotel_owner'" class="btn btn-dark me-2">Mes hôtel</router-link>
            <button class="btn btn-dark ms-2" @click="this.setDisconnect()" data-test-id="button-disconnect">Se déconnecter</button>
          </div>

        </div>
      </div>

    </div>
  </nav>
</template>

<script>
import { useRoute } from "vue-router";
import { watch, ref } from "vue";

export default {
  name: 'Navbar',

  setup() {
    const route = useRoute();
    const connected = ref(localStorage.getItem('access') !== null);
    watch(
      () => route.path,
      () => connected.value = localStorage.getItem('access') !== null
    );

    return {
      connected
    };
  },

  methods: {
    setDisconnect() {
      localStorage.clear();
      this.connected = false;
      location.reload();
    },

    getUserType() {
      return localStorage.getItem('type');
    }
  }
}
</script>

<style scoped>
/* img.logo {
  height: 150px;
  width: 150px;
} */
</style>
