<template>
  <div class="container-img">
      <img class="home-img" src="../assets/home.png" alt="Big_BNB logo">
</div>
  <search @input="this.onInput" />
  <div id="all-hotels">
    <div v-for="hotel in this.hotels" class="hotel">
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
      hotels: [],
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

      this.sortHotel();

    },

    onInput(data) {
      this.hotels = data['hotels'];
      this.sortHotel();
    },

    sortHotel() {
      this.hotels = this.hotels.sort((a, b) => {
        if (this.isHotelOwnerOf(a.hotel_owner) && !this.isHotelOwnerOf(b.hotel_owner))
          return -1;
        if (this.isHotelOwnerOf(b.hotel_owner) && !this.isHotelOwnerOf(a.hotel_owner))
          return 1;
      })
    }
  },

  mounted() {
    this.fetchAllHotels();
  }

}
</script>

<style scoped>
.container-img {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 400px;
  margin-top: 50px;
}

.home-img {
  max-width: 100%;
  max-height: 100%;
}
</style>
