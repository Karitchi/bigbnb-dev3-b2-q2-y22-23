<template>
  <div class="login-container">
    <h2>Connexion</h2>
    <form @submit="login" class="login-form">
      <div class="form-group">
        <label for="login-email">Email :</label>
        <input type="email" id="login-email" v-model="email" class="form-control">
      </div>
      <div class="form-group">
        <label for="login-pw">Mot de passe :</label>
        <input type="password" id="login-pw" v-model="password" class="form-control">
      </div>
      <button type="submit" class="btn btn-primary">Se connecter</button>
    </form>

    <div v-if="errorMsg !== ''" class="error-message">
      <p>Erreur : {{ errorMsg }}</p>
    </div>
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
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 100px;
}

.login-form {
  width: 300px;
  margin-top: 20px;
}

.form-group {
  margin-bottom: 10px;
}

.error-message {
  color: red;
  margin-top: 10px;
}
</style>

