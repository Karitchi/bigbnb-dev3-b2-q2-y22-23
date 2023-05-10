<template>
  <div>
    <button @click="goBack">Retour</button>
    <h1>Modification de l'hôtel</h1>

    <form @submit.prevent="modifierHotel">
      <label for="nom">Nom de l'hôtel:</label>
      <input type="text" id="nom" v-model="name">

      <label for="image">Image:</label>
      <input type="file" id="image" @change="onFileChange">

      <label for="description">Description:</label>
      <textarea id="description" v-model="hotel.description"></textarea>

      <label for="prix">Prix de la chambre:</label>
      <input type="number" step="0.01" id="prix" v-model="hotel.price">

      <button @click="test" type="submit">Enregistrer les modifications</button>
    </form>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      hotel: {},
      name : "",
      image : "",
      description : "",
      price : ""
    }
  },
  mounted() {
    axios.get(`${this.$api}hotels/${this.$route.params.id}`).then(response=>this.hotel=response.data).catch(error => console.log("certaines données sont introuvables"))
  }, // get {export default.$api -> django -> localhost port 8000} dans le tableau hotels/ ${export default.modification:id}on met tout dans une variabel reponse
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    modifierHotel() {
      // Effectuer les modifications de l'hôtel ici
      // utiliser les données de l'objet `hotel` pour envoyer les modifications au backend

      // Exemple de code fictif pour l'envoi des modifications au backend
      axios.put(`${this.$api}hotels/${this.$route.params.id}`, {
        name: "nom",
        price: 10.4,
        image: "image.png",
        description: "mon hôtel"
      })
        .then(response => {
          // Traitement de la réponse du backend
          // Par exemple, afficher un message de succès ou rediriger vers une autre page
        })
        .catch(error => {
          console.log("test");
          // Gérer les erreurs lors de la modification de l'hôtel
          // Par exemple, afficher un message d'erreur ou effectuer une autre action appropriée
        });
    },
    onFileChange(event) {
      // Gérer le changement de fichier d'image ici
      // Par exemple, lire le fichier image et effectuer des actions supplémentaires si nécessaire
    },
    test(){
      console.log(this.name)
    }
  },
};
</script>

<style scoped>
  /* Styles CSS spécifiques à votre vue */
</style>
  