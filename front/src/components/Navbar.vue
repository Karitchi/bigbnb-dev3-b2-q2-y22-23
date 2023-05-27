<template>
    <nav class="navbar navbar-expand-lg my-header" data-bs-theme="dark">
        <div class="container-fluid">

            <router-link class="navbar-brand" to="/">Big bnb</router-link>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link class="nav-link active" aria-current="page" to="/">Home</router-link>
                    </li>

                    <li class="nav-item">
                        <router-link class="nav-link active" aria-current="page" to="/about">About</router-link>
                    </li>
                </ul>


              <div class="d-flex ms-auto">
                <div v-if="!this.connected">
                  <router-link to="/login">Se connecter</router-link>
                  <router-link to="/register_client">S'inscrire</router-link>
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
      this.$router.push('/');
    }
  }
}
</script>
