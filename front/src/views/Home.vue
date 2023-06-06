<template>
  <search @input="this.onInput" />

  <div v-if="this.hotels.length !== 0">
    <div class="row row-cols-xl-5 row-cols-lg-4 row-cols-md-3 row-cols-sm-2 row-cols-1 m-0">
      <div v-for="hotel in hotels" :key="hotel.id" class="col m-0 p-3">
        <CardHotel :hotel="hotel" />
      </div>
    </div>
  </div>

  <p v-else class="d-flex justify-content-center">No hotels found.</p>
</template>


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
