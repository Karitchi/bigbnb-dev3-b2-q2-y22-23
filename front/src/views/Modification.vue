<template>
  <div class="page-container">
    <div class="content-container">
      <button @click="goBack" class="my-button hover-button">Retour</button>
      <h1 class="my-heading titre">Modification de l'hôtel</h1>

      <form @submit.prevent="modifierHotel" class="my-form">

        <div v-if="errorForm !== ''" class="alert alert-danger" role="alert">
          {{ errorForm }}
        </div>

        <div class="alert alert-success" role="alert" v-if="success">
          Changements effectués avec succès !
        </div>

        <div class="form-row">
          <label for="nom" class="my-label">Nom de l'hôtel:</label>
          <input type="text" id="nom" v-model="name" class="my-input input1">
        </div>

        <div class="form-row">
          <label for="image" class="my-label">img:</label>
          <input type="text" id="image" v-model="img" class="my-input input2">
        </div>

        <div class="form-row">
          <label for="description" class="my-label">Description:</label>
          <textarea id="description" v-model="description" class="my-textarea input3"></textarea>
        </div>

        <div class="form-row">
          <label for="prix" class="my-label">Prix de la chambre:</label>
          <input type="number" step="0.01" id="prix" v-model="price" class="my-input input4">
        </div>

        <div class="form-row">
          <label for="phone" class="my-label">Numéro de téléphone:</label>
          <input type="tel" id="phone" v-model="phone_number" class="my-input input5">
        </div>

        <div class="form-row">
          <label for="mail" class="my-label">mail:</label>
          <input type="email" id="mail" v-model="mail" class="my-input input6">
        </div>

        <div v-for="(facility, index) in facilities" :key="index">
          <div class="form-row">
            <label :for="'facility-name-' + index" class="my-label">Equipement/service:</label>
            <input :id="'facility-name-' + index" v-model="facility.name" class="my-input">
          </div>
          <div class="form-row">
            <label :for="'facility-description-' + index" class="my-label">Equipement/service Description:</label>
            <input :id="'facility-description-' + index" v-model="facility.description" class="my-input">
          </div>
        </div>

        <div class="controls">
          <a href="#" id="add_more_fields" @click.prevent="addFacility"><i class="fa fa-plus"></i> Ajouter</a>
          <a href="#" id="remove_fields" @click.prevent="removeFacility"><i class="fa fa-plus"></i> Retirer</a>
        </div>

        <button type="submit" class="my-button hover-button">Enregistrer les modifications</button>

      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      hotel: {},
      name: "",
      img: "",
      description: "",
      price: "",
      phone_number: "",
      mail: "",
      errorForm: '',
      success: false,
      facilities: [{ name: '', description: '' }],
    }
  },

  mounted() {
    axios.get(`${this.$api}hotels/${this.$route.params.id}`)
      .then(response => this.responseHotel(response.data))
      .catch(error => console.log("certaines données sont introuvables"))
  },

  methods: {
    goBack() {
      this.$router.go(-1);
    },

    isValidPhoneNumber(phoneNumber) {
      const phoneRegex = /^[0-9]{10}$/;
      return phoneRegex.test(phoneNumber);
    },

    isValidEmail(email) {
      const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
      return emailRegex.test(email);
    },

    modifierHotel() {
      if (this.name.length < 3 || this.name.length > 30) {
        this.errorForm = "Le nom de l'hôtel doit contenir entre 3 et 30 caractères.";
        this.success = false;
        return;
      }

      if (this.price <= 0) {
        this.errorForm = "Le prix de la chambre doit être supérieur à zéro";
        this.success = false;
        return;
      }

      if (this.phone_number && !this.isValidPhoneNumber(this.phone_number)) {
        this.errorForm = "Le numéro de téléphone n'est pas valide.";
        this.success = false;
        return;
      }

      if (this.mail && !this.isValidEmail(this.mail)) {
        this.errorForm = "L'adresse e-mail n'est pas valide.";
        this.success = false;
        return;
      }

      this.errorForm = '';

      this.hotel.name = this.name;
      this.hotel.description = this.description;
      this.hotel.price = this.price;
      this.hotel.phone_number = this.phone_number;
      this.hotel.mail = this.mail;

      axios.patch(`${this.$api}hotels/${this.$route.params.id}/`, {
        name: this.hotel.name,
        price: this.hotel.price,
        description: this.hotel.description,
        phone_number: this.hotel.phone_number,
        mail: this.hotel.mail
      })
        .catch(error => {
          console.log("test");
          this.success = false;
        })
        .then(response => this.success = true);

      this.facilities.forEach((facility, index) => {
        axios.post(`${this.$api}facilities/${this.$route.params.id}/`, {
          name: facility.name,
          description: facility.description
        })
          .catch(error => {
            console.log("test2");
            this.success = false;
          })
          .then(response => {
            this.success = true;
          });
      });
    },

    responseHotel(responseData) {
      this.hotel = responseData;
      if (!this.isHotelOwnerOf(this.hotel.hotel_owner)) {
        this.$router.go(-1);
      }
      this.name = this.hotel.name;
      this.description = this.hotel.description;
      this.price = this.hotel.price;
      this.phone_number = this.hotel.phone_number;
      this.mail = this.hotel.mail;
    },

    addFacility() {
      this.facilities.push({ name: '', description: '' });
    },

    removeFacility() {
      if (this.facilities.length > 1) {
        this.facilities.pop();
      }
    },

    onFileChange(event) {
      /*Gérer le changement de fichier d'image ici
       Par exemple, lire le fichier image et effectuer des actions supplémentaires si nécessaire*/
    },

    test() {
      console.log(this.name)
    },
  },
};
</script>

<style scoped>
.page-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.content-container {
  flex: 1;
  padding-bottom: 80px; /* Espacement en bas pour éviter que le footer ne chevauche le contenu */
}

.my-button {
  background-color: #75ABBC;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 10px;
  margin-bottom: 20px;
}

.my-heading {
  font-size: 24px;
  margin-bottom: 20px;
}

.my-form {
  margin-top: 20px;
  border: 3px solid #DFE0E2;
  padding: 20px;
  max-width: 1400px;
  margin-left: 10px;
}

.form-row {
  display: flex;
  margin-bottom: 20px;
  vertical-align: top;
}

.my-alert {
  background-color: #F0AD4E;
  color: white;
  padding: 10px;
  margin-bottom: 20px;
}

.my-label {
  font-weight: bold;
  float: left;
}

.my-input {
  width: 40%;
  margin-bottom: 10px;
  border: 1px solid #DFE0E2;
  border-radius: 4px;
  box-sizing: border-box;
}

.my-textarea {
  width: 40%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #DFE0E2;
  border-radius: 4px;
  resize: vertical;
  box-sizing: border-box;
}

.hover-button:hover {
  background-color: #326b80; /* Couleur plus foncée pour l'effet de survol */
}

.input1 {
  margin-left: 9.7%;
}

.input2 {
  margin-left: 16%;
}

.input3 {
  margin-left: 11.6%;
}

.input4 {
  margin-left: 7.4%;
}

.input5 {
  margin-left: 5.5%;
}

.input6 {
  margin-left: 15.5%;
}
</style>
