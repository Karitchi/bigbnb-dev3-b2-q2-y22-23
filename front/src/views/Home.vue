<template>
  
  <search></search>
  <div class="container-fluid p-5" id="all-hotels">
    <div v-for="hotel in this.hotels" class="row m-0 hotel">
      <card-hotel :hotel="hotel" />
    </div>
  </div>
</template>

<style scoped>
@import '../assets/variables.scss';

#all-hotels {
  text-align: center;
}

.hotel {
  display: inline;
}
</style>


<script>
import CardHotel from '../components/CardHotel.vue'
import Search from '../components/search.vue';
import axios from "axios";

export default {
  name: 'App',
  components: {
    CardHotel,
    Search,
  },

  data() {
    return {
      hotels: []
    }
  },

  methods: {
    fetchAllHotels() {
      axios.get(`${this.$api}hotels/`)
        .then(response => this.setHotels(response.data));
    },

    setHotels(responseData) {
      this.hotels = responseData;
      if (this.getUserType() !== this.$hotelOwnerUserType)
        return;

      this.hotels = this.hotels
        .sort((a, b) => {
          if (this.isHotelOwnerOf(a.hotel_owner) && !this.isHotelOwnerOf(b.hotel_owner))
            return -1;
          if (this.isHotelOwnerOf(b.hotel_owner) && !this.isHotelOwnerOf(a.hotel_owner))
            return 1;
        })

      console.log(this.hotels)
    }
  },

  mounted() {
    this.fetchAllHotels();
  }

}
</script>

<style scoped>

</style>