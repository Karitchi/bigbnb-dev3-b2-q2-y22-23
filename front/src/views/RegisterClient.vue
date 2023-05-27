<template>
  <register-nav-buttons :is-client="true" />
  <form @submit="this.tryRegister" style="padding: 10px">
    <mail-input @input-mail="this.setMail" />
    <password-input @input-password="this.setPassword" />
    <name-input @input-name="this.setNameAndLastName" />
    <div>
      <button
          type="submit"
          class="btn btn-primary "
          :disabled="!this.isFormValid"
      >S'inscrire</button>
    </div>

  </form>
  <mail-exist :is-mail-exist="this.isMailExist" />
</template>

<script>
import RegisterNavButtons from "@/components/RegisterNavButtons";
import MailInput from "@/components/Register/MailInput";
import PasswordInput from "@/components/Register/PasswordInput"
import NameInput from "@/components/Register/NameInput";
import axios from "axios";
import MailExist from "@/components/Register/MailExist";
export default {
  name: "RegisterClient",
  components: {MailExist, MailInput, RegisterNavButtons, PasswordInput, NameInput},
  data() {
    return {
      mail: '',
      isMailValid: false,
      password: '',
      isPasswordValid: false,
      name: '',
      lastname: '',
      areNameAndLastNameValid: false,
      isFormValid: false,
      isMailExist: false
    }
  },

  methods: {
    setMail(data) {
      this.mail = data['mail'];
      this.isMailValid = data['isValid'];
      this.setFormValid();
      this.isMailExist = false;
    },

    setPassword(data) {
      this.password = data['password'];
      this.isPasswordValid = data['isValid'];
      this.setFormValid();
    },

    setNameAndLastName(data) {
      this.name = data['name'];
      this.lastname = data['lastname'];
      this.areNameAndLastNameValid = data['isValid'];
      this.setFormValid();
    },

    setFormValid() {
      this.isFormValid = this.isMailValid && this.isPasswordValid && this.areNameAndLastNameValid;
    },

    tryRegister(e) {
      if (!this.isFormValid)
        return;

      axios.post(`${this.$api}clients/`, {
        'info': {
          'mail': this.mail,
          'password': this.password,
          'name': this.name,
          'lastname': this.lastname
        }
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
          .then(response => this.getToken())
          .catch(error => this.catchError(error));
      e.preventDefault();
    },

    getToken() {
      axios.post(`${this.$api}token/`, {
        'mail': this.mail,
        'password': this.password
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(response => this.login(response.data));
    },

    login(data) {
      this.storeToken(data);
      this.$router.push('/');
      alert(`
      Bienvenu sur BIG_BNB, ${this.lastname} ${this.name} !\n
      Vous allez être redirigé vers la page d'accueil du site
      `)
    },

    catchError(error) {
      this.isMailExist = error.response.status === 409;
    }
  },

  beforeMount() {
    if (this.isConnected())
      this.$router.push('/');
  }
}
</script>

<style scoped>

</style>
