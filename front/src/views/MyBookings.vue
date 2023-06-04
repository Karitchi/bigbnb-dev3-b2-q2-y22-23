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
import {ref} from "vue";
export default {
  name: "MyBookings",
  components: {CardBooking, HotelOwnerNavbar},

  data() {
    return {
      hotelOwner: null,
      hotels: [],
      bookings: [],
    }
  },

  methods: {
    fetchHotels() {
      axios.get(`${this.$api}hotels/`)
          .then(responses => this.setHotels(responses.data));
    },

    setHotels(responseData) {
      for (let data of responseData) {
        if (data.hotel_owner === this.hotelOwner) {
          this.hotels.push(data.id);
        }
      }
    },

    fetchBookings() {
      axios.get(`${this.$api}bookings/`)
      .then(responses => this.setBookings(responses.data));
    },

    setBookings(responseData) {
      this.bookings = responseData
          .filter(data => this.hotels.includes(data.hotel) && data.approved === null)
          .sort((a, b) => {
            if (!a.unread && b.unread)
              return 1;
            if (a.unread && !b.unread)
              return -1;
          });
    },

    onAccept(id) {
      axios.patch(`${this.$api}/bookings/set_booking_approved/${id}/`, {'approved': true})
      .then(response => this.bookings = this.bookings.filter(booking => booking.id !== id));
    },

    onRefuse(id) {
      axios.patch(`${this.$api}/bookings/set_booking_approved/${id}/`, {'approved': false})
      .then(response =>this.bookings = this.bookings.filter(booking => booking.id !== id));
    },

    setBookingsToRead() {
      for (let booking of this.bookings) {
        if (booking.unread)
          axios.patch(`${this.$api}/bookings/set_booking_read/${booking.id}/`, {'unread': false})
      }
    }
  },

  beforeMount() {
    if (this.getUserType() !== this.$hotelOwnerUserType)
      this.$router.go(-1);
    this.hotelOwner = this.getID();
  },

  mounted() {
    window.onbeforeunload = this.setBookingsToRead;
    window.onblur = this.setBookingsToRead;
    window.onmouseout = this.setBookingsToRead;
    this.fetchHotels();
    this.fetchBookings();
  },

}
</script>
