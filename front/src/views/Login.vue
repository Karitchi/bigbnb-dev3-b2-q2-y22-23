<template>
  <form @submit="this.login">
    <label for="login-email">Email :</label>
    <input type="email" id="login-email" v-model="this.email"><br>
    <label for="login-pw">Mot de passe :</label>
    <input type="password" id="login-pw" v-model="this.password"><br>
    <button type="submit">Se connecter</button>
  </form>

  <div v-if="this.errorMsg !== ''">
    <p>Erreur : {{ this.errorMsg }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",

  data() {
    return {
      email: "",
      password: "",
      errorMsg: ""
    }
  },

  methods: {
    login(e) {
      axios.post(`${this.$api}token/`, {
        'mail': this.email,
        'password': this.password
      },{
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => this.loginResponse(response))
      .catch(reason => this.errorMsg = "Erreur de connexion");

      e.preventDefault();
    },

    loginResponse(response) {
      if (response.status === 200) {
        this.$router.push('/');
        try {
          this.storeToken(response.data);
        } catch (err) {
          console.log(err)
        }
      }
    }
  },

  mounted() {
    this.forceRedirectionIfConnected();
  }
}
</script>

<style scoped>

</style>
