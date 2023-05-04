<template>
  <hotel-owner-navbar :hotel_owner="this.hotelOwner" :is-my-hotel="true"/>

  <span class="nav justify-content-center">
    <input @input="this.onInputSearchHotels" type="search" id="my-hotels-search" class="form-control w-25" placeholder="Entrez le nom de l'hôtel ...">
  </span>

  <section id="all-hotels">
    <div v-for="hotel in this.hotelsFiltered" class="hotel">
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

#my-hotels-search {
  margin-top: 3px;
  margin-bottom: 10px;
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
      hotelsFiltered: []
    }
  },

  methods: {
    callHotels() {
      axios.get(`${this.$api}hotels/`)
      .then(response => this.applyHotels(response.data));
    },

    applyHotels(responseData) {
      this.hotels = responseData.filter(hotel => hotel.hotel_owner === this.hotelOwner);
      for (let i = 0; i < this.hotels.length; i++) {
        axios.get(`${this.$api}cities/${this.hotels[i].city}`)
        .then(response => this.hotels[i].city = response.data);
      }
      this.hotelsFiltered = JSON.parse(JSON.stringify(this.hotels));
    },

    onInputSearchHotels(input) {
      let value = input.target.value
      this.hotelsFiltered = this.hotels.filter(hotel => hotel.name.toLowerCase().includes(value.toLowerCase()));
    },
  },

  mounted() {
    this.callHotels();
    this.hotelsFiltered = this.hotels;
  }
}
</script>

