<template>
  <div class="container-fluid p-5" id="all-hotels">
    <div v-for="hotel in this.hotels" class="row m-0 hotel" >
      <card-hotel :hotel="hotel"/>
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
      .then(response => this.setHotels(response.data));
    },

    setHotels(responseData) {
      this.hotels = responseData;
      if (!this.isHotelOwnerOf(this.hotel.id))
        return;
      let id = this.getID();
      this.hotels = this.hotels.sort((a, b) => {
        if (a.hotelOwner === id) return 1;
        if (b.hotelOwner === id) return -1;
      });
    }
  },

  mounted() {
    this.fetchAllHotels();
  }

}
</script>
