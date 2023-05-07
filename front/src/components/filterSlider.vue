<template>
  <div>
    <div>
      <input type="range" min="0" max="1000" v-model="minPrice" @input="fetchHotels" />
      <label>Min Price: {{ minPrice }}</label>
    </div>
    <div>
      <input type="range" min="0" max="10" step="1" v-model="minRating" @input="fetchHotels" />
      <label>Min Rating: {{ minRating }}</label>
    </div>
    <div v-if="isLoading">Loading...</div>
    <ul v-else>
      <li v-for="hotel in hotels" :key="hotel.id">{{ hotel.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      minPrice: 100,
      maxPrice: 200,
      minRating: 3,
      maxRating: 4,
      isLoading: false,
      hotels: [],
    };
  },
  methods: {
    fetchHotels() {
      this.isLoading = true;

      axios
        .get('http://192.168.1.16:8000/filter_hotels', {
          params: {
            min_price: this.minPrice,
            max_price: this.maxPrice,
            min_rating: this.minRating,
            max_rating: this.maxRating,
          },
        })
        .then((response) => {
          console.log(response);
          this.hotels = response.data;
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
  },
};
</script>
