<template>
    <nav class="navbar navbar-expand-lg my-header" data-bs-theme="dark">
        <div class="container-fluid">

            <router-link class="navbar-brand" to="/"><img class="logo" src="../assets/logo2.png"></router-link>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <div class="d-flex ms-auto">
                <div v-if="!this.connected">
                  <router-link class="connect" to="/login">Se connecter</router-link>
                  <router-link class="connect" to="/register_client">S'inscrire</router-link>
                </div>
                <div v-else>
                  <router-link to="/">Mon profil</router-link>
                  <button @click="this.setDisconnect()" data-test-id="button-disconnect">Se déconnecter</button>
                </div>

              </div>
            </div>

        </div>
    </nav>
</template>

<script>


import {useRoute} from "vue-router";
import {watch, ref} from "vue";

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
    }
  }
}
</script>

<style scoped>
  .connect {
  text-decoration: none;
  display: inline-block;
  padding: 10px 20px;
  background-color: #75ABBC;
  color: whitesmoke;
  border-radius: 5px;
  font-size: 25px;
}

.connect:hover {
  text-decoration: underline;
  font-weight: bold;
}

img.logo{
  height: 150px;
  width: 150px;
}
</style>
