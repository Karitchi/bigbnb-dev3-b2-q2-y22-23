<template>
  <card-hotel v-if="this.hotel !== null" :hotel="this.hotel"/>
</template>

<script>
import CardHotel from "@/components/CardHotel";
import axios from "axios";

export default {
  name: "InfoHotel",
  components: {CardHotel},
  data() {
    return {
      hotel: null
    }
  },


  mounted() {
    axios.get(`${this.$api}hotels/${this.$route.params.id}`)
    .then(response => this.hotel = response.data)
    .catch(error => console.log(error));
  }
}
</script>

<style scoped>

</style>
