<template>
  <div class="container-fluid p-5">
    <div v-for="hotel in this.hotels" class="row m-0">
      <card-hotel :hotel="hotel" />
    </div>
  </div>
</template>

<style scoped>
  @import '../assets/variables.scss'
</style>


<script>
import CardHotel from '../components/CardHotel.vue'
import axios from "axios";

export default {
  name: 'App',
  components: {
        CardHotel,
  },

  data() {
    return {
      hotels: []
    }
  },

  methods: {
    fetchAllHotels() {
      axios.get(`${this.$api}hotels/`)
      .then(response => this.hotels = response.data)
    }
  },

  mounted() {
    this.fetchAllHotels();
  }

}
</script>
