<template>
  <div class="page-container">
    <div class="content-container">
      <button @click="goBack" class="my-button hover-button">Retour</button>
      <h1 class="my-heading titre">Modification de l'hôtel</h1>

      <form @submit.prevent="modifierHotel" class="my-form">
        <div v-if="errorForm !== ''" class="my-alert" role="alert">
          {{ this.errorForm }}
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

        <button @click="test" type="submit" class="my-button hover-button">Enregistrer les modifications</button>
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
       name : "",
       img : "",
       description : "",
        price : "",
        errorForm: ''
      }
   },

    mounted() {
      axios.get(`${this.$api}hotels/${this.$route.params.id}`)
          .then(response=>this.responseHotel(response.data))
          .catch(error => console.log("certaines données sont introuvables"))
    }, // get {export default.$api -> django -> localhost port 8000} dans le tableau hotels/ {export default.modification:id}on met tout dans une variabel reponse
    methods: {
     goBack() {
        this.$router.go(-1);
     },
      modifierHotel() {
       /*const imageRegex = /\.(jpeg|jpg|gif|png)$/i; // Expression régulière pour vérifier les extensions d'image courantes, a voir quelles extensions on utilisera !

       if (!imageRegex.test(this.img)) {
          this.errorForm = "Le lien vers l'image de l'hôtel n'est pas valide.";
          return;
       }
       if (this.image.length > 100){
         this.errorForm = "Le lien vers l'image de l'hotel ne doit pas dépasser 100 caractères"
       }*/
       if (this.name.length < 3 || this.name.length > 30) {
         this.errorForm = "Le nom de l'hôtel doit contenir entre 3 et 30 caractères.";
          return
       }
       if (this.price <= 0){
          this.errorForm = "Le prix de la chambre doit être supérieur à zéro"
          return
       }
       this.errorForm = ''
        this.hotel.name = this.name
        this.hotel.description = this.description
        this.hotel.price = this.price
        axios.patch(`${this.$api}hotels/${this.$route.params.id}/`, {
          name: this.hotel.name,
         price: this.hotel.price,
         description: this.hotel.description
        }).catch(error => {
           console.log("test");
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
     },
     onFileChange(event) {
       /*Gérer le changement de fichier d'image ici
        Par exemple, lire le fichier image et effectuer des actions supplémentaires si nécessaire*/
     },
     test(){
        console.log(this.name)
     },
    },
  };
</script>

<style scoped>

.titre {
  margin-left: 20px;
}

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
  float : left;
}

.my-input {
  width: 40%;
  padding: 8px;
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

</style>
