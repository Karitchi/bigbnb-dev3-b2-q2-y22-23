<template>
  <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3 col-xl-2 p-3" id="hotel-card">
      <div class="card m-auto">
          <img src="https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" class="card-img-top" alt="...">
          <div class="card-body">
              <h3 class="cart-title">{{ this.hotel.name }}</h3>
            <p class="card-text"> <i>{{ this.hotel.description }}</i></p>
              <button @click="this.goToHotel" class="btn btn-primary" style="margin-bottom: 5px">{{ this.infoMsg }}</button>
            <p class="card-footer">By <i>{{ this.hotelOwner.company }}</i></p>

          </div>
      </div>
  </div>
</template>

<style scoped>
#hotel-card {
  display: inline-block;
}
</style>
<script>
import axios from "axios";


export default {
  name: 'Card',
  props: ['hotel'],
  data() {
    return {
      hotelOwner: {},
      infoMsg: "",
    }
  },

  methods: {
    setHotelOwner() {
      axios.get(`${this.$api}hotel_owners/${this.hotel.hotel_owner}`)
      .then(response => this.hotelOwner = response.data);
    },

    goToHotel() {
      if (!this.isHotelOwnerOf(this.hotel.hotel_owner)) {
        this.$router.push(`/hotels/${this.hotel.id}`)
      } else {
        this.$router.push(`/modification/${this.hotel.id}`)
      }
    }
  },

  mounted() {
    if (!this.isHotelOwnerOf(this.hotel.hotel_owner)) {
      this.infoMsg = "Plus d'informations";
    } else {
      this.infoMsg = "Modifier informations"
    }
    this.setHotelOwner();
  }
}
</script>
