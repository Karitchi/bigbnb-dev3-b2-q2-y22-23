<template>
  <hotel-owner-navbar :hotel_owner="this.hotelOwner.id" :is-my-hotel="false" />

  <section id="all-bookings">
    <div v-if="this.bookings.length > 0" v-for="booking in this.bookings" class="booking">
      <card-booking :booking="booking" :on_accept="this.onAccept" :on_refuse="this.onRefuse" />
    </div>

    <div v-else>
      Pas de bookings
    </div>
  </section>
</template>


<style scoped>
#all-bookings {
  text-align: center;
}

.booking {
  margin: 10px;
}
</style>


<script>

import HotelOwnerNavbar from "../components/HotelOwnerNavbar";
import CardBooking from "@/components/CardBooking";
import axios from "axios";
export default {
  name: "MyBookings",
  components: {CardBooking, HotelOwnerNavbar},

  data() {
    return {
      hotelOwner: 1,
      hotels: [],
      bookings: [],
      bookingsFiltered: [],
    }
  },

  methods: {
    fetchHotels() {
      axios.get(`${this.$api}hotels/`)
          .then(responses => this.setHotels(responses.data));
    },

    setHotels(responseData) {
      for (let i in responseData) {
        if (responseData[i].hotel_owner === this.hotelOwner) {
          this.hotels.push(responseData[i].id);
        }
      }
    },

    fetchBookings() {
      axios.get(`${this.$api}bookings/`)
      .then(responses => this.setBookings(responses.data));
    },

    setBookings(responseData) {
      this.bookings = responseData
          .filter(data => this.hotels.includes(data.hotel))
          .sort((a, b) => {
            if (!a.unread && b.unread)
              return 1;
            if (a.unread && !b.unread)
              return -1;
          });
      this.bookingsFiltered = this.bookings;
    },



    onAccept(id) {
      this.bookings = this.bookings.filter(booking => booking.id !== id);
    },

    onRefuse(id) {
      this.bookings = this.bookings.filter(booking => booking.id !== id);
    }
  },

  mounted() {
    this.fetchHotels();
    this.fetchBookings();
  }
}
</script>
