<template>
  <div>
    <button @click="goBack">Retour</button>
    <h1>Modification de l'hôtel</h1>

    <form @submit.prevent="modifierHotel">
      <label for="nom">Nom de l'hôtel:</label>
      <input type="text" id="nom" v-model="hotel.name">

      <label for="image">Image:</label>
      <input type="file" id="image" @change="onFileChange">

      <label for="description">Description:</label>
      <textarea id="description" v-model="hotel.description"></textarea>

      <label for="prix">Prix de la chambre:</label>
      <input type="number" step="0.01" id="prix" v-model="hotel.price">

      <button type="submit">Enregistrer les modifications</button>
    </form>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    modifierHotel() {
      // Effectuer les modifications de l'hôtel ici
      // utiliser les données de l'objet `hotel` pour envoyer les modifications au backend

      // Exemple de code fictif pour l'envoi des modifications au backend
      axios.put(`/api/hotels/${this.hotel.hotel_id}`, this.hotel)
        .then(response => {
          // Traitement de la réponse du backend
          // Par exemple, afficher un message de succès ou rediriger vers une autre page
        })
        .catch(error => {
          // Gérer les erreurs lors de la modification de l'hôtel
          // Par exemple, afficher un message d'erreur ou effectuer une autre action appropriée
        });
    },
    onFileChange(event) {
      // Gérer le changement de fichier d'image ici
      // Par exemple, lire le fichier image et effectuer des actions supplémentaires si nécessaire
    },
  },
};
</script>

<style scoped>
  /* Styles CSS spécifiques à votre vue */
</style>
  