<template>
  <div class="card shadow">
    <img
        :src="this.image !== null ? this.$api + this.image : this.DEFAULT_IMAGE"
        class="card-img-top"
        alt="hotel image"
    />
    <div class="card-body">
      <h3 class="cart-title">{{ this.hotel.name }}</h3>
      <p class="card-text" style="height: 100px; overflow: auto;">
        <i>{{ this.hotel.description }}</i>
      </p>
      <p class="card-footer">By <i>{{ this.hotelOwner.company }}</i></p>
      <button @click="this.isHotelOwner ? this.$router.push(`/modification/${this.hotel.id}`) : this.$router.push(`/hotels/${this.hotel.id}`)" class="btn btn-primary me-auto" style="margin-bottom: 5px">
        {{ this.isHotelOwner ? 'Modifier informations' : 'Plus d\'informations' }}
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";


export default {
  name: 'Card',
  props: ['hotel'],
  data() {
    return {
      hotelOwner: {},
      infoMsg: "",
      isHotelOwner: null,
      image: null,
      DEFAULT_IMAGE: "https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
    }
  },

  methods: {
    setHotelOwner() {
      axios.get(`${this.$api}hotel_owners/${this.hotel.hotel_owner}`)
        .then(response => this.hotelOwner = response.data);
    },

    fetchImages() {
      axios.get(`${this.$api}hotels/${this.hotel.id}/images/`)
          .then(response => this.setImages(response.data))
          .catch(error => this.image = null);
    },

    setImages(responseData) {
      if (responseData.length > 0) {
        this.image = responseData[0].url;
      } else {
        this.image = null;
      }
    }
  },

  mounted() {
    this.setHotelOwner();
    this.isHotelOwner = this.isHotelOwnerOf(this.hotel.hotel_owner);
    this.fetchImages();
  }
}
</script>
