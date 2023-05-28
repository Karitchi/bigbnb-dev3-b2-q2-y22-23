<template>
  <register-nav-buttons :is-client="false" />
  <form @submit="this.tryRegister" style="padding: 10px">
    <mail-input @input="this.setMail" />
    <password-input @input="this.setPassword" />
    <name-input @input="this.setNameAndLastname" />
    <society-input @input="this.setSociety" />
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
import PasswordInput from "@/components/Register/PasswordInput";
import NameInput from "@/components/Register/NameInput";
import SocietyInput from "@/components/Register/SocietyInput";
import MailExist from "@/components/Register/MailExist";
import axios from "axios";
export default {
  name: "RegisterHotelOwner",
  components: {SocietyInput, NameInput, MailInput, RegisterNavButtons, PasswordInput, MailExist},

  data() {
    return {
      mail: '',
      isMailValid: false,
      password: '',
      isPasswordValid: false,
      name: '',
      lastname: '',
      areNameAndLastNameValid: false,
      society: '',
      isSocietyValid: false,
      isFormValid: false,
      isMailExist: false
    }
  },

  methods: {
    setMail(data) {
      this.mail = data['mail'];
      this.isMailValid = data['isValid'];
      this.isMailExist = false;
      this.setFormValid();
    },

    setPassword(data) {
      this.password = data['password'];
      this.isPasswordValid = data['isValid'];
      this.setFormValid();
    },

    setNameAndLastname(data) {
      this.name = data['name'];
      this.lastname = data['lastname'];
      this.areNameAndLastNameValid = data['isValid'];
      this.setFormValid();
    },

    setSociety(data) {
      this.society = data['society'];
      this.isSocietyValid = data['isValid'];
      this.setFormValid();
    },

    setFormValid() {
      this.isFormValid = this.isMailValid && this.isPasswordValid && this.areNameAndLastNameValid && this.isSocietyValid;
    },

    tryRegister(e) {
      if (!this.isFormValid)
        return;

      axios.post(`${this.$api}hotel_owners/`, {
        'company': this.society,
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

    catchError(error) {
      this.isMailExist = error.response.status === 409;
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
      `);
    },
  }
}
</script>

<style scoped>

</style>
