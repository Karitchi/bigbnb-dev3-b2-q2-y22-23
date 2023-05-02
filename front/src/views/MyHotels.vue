<template>
  <hotel-owner-navbar :hotel_owner="this.hotelOwner" :is-my-hotel="true"/>

  <section id="all-hotels">
    <div v-for="hotel in this.hotels" class="hotel">
      <card-hotel :hotel="hotel" />
    </div>
  </section>

</template>

<style scoped>

#all-hotels {
  text-align: center;

}

.hotel {
  display: inline;
}
</style>

<script>
import axios from 'axios';
import CardHotel from "@/components/CardHotel";
import HotelOwnerNavbar from "@/components/HotelOwnerNavbar";

export default {
  name: "MyHotels",
  components: {HotelOwnerNavbar, CardHotel},
  data() {
    return {
      hotelOwner: 1,
      hotels: [],
    }
  },

  methods: {
    callHotels() {
      axios.get(`${this.$api}hotels/`)
      .then(response => this.applyHotels(response.data));
    },

    applyHotels(response) {
      this.hotels = response;
      for (let i = 0; i < this.hotels.length; i++) {
        axios.get(this.hotels[i].city_id)
        .then(response => this.hotels[i].city_id = response.data);
      }
    }
  },

  mounted() {
    this.callHotels();
  }
}
</script>

<style scoped>

</style>
