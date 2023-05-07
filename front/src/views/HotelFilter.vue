<template>
  <div>
    <div>
      <vue-slider v-model="priceRange" :min="0" :max="2000" @drag-end="fetchHotels" />
      <label>Price Range: {{ priceRange }}</label>
    </div>
    <div>
      <vue-slider v-model="ratingRange" :min="0" :max="5" :step="1" @drag-end="fetchHotels" />
      <label>Rating Range: {{ ratingRange }}</label>
    </div>
    <div v-if="isLoading">Loading...</div>
    <ul v-else>
      <li v-for="hotel in hotels" :key="hotel.id">{{ hotel.name }}</li>
    </ul>
  </div>
</template>

<script>
import VueSlider from 'vue-slider-component';
import 'vue-slider-component/theme/default.css';
import axios from 'axios';

export default {
  components: {
    VueSlider,
  },
  data() {
    return {
      priceRange: [0, 2000],
      ratingRange: [0, 5],
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
            min_price: this.priceRange[0],
            max_price: this.priceRange[1],
            min_rating: this.ratingRange[0],
            max_rating: this.ratingRange[1],
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
<style>
.filters {
  margin-bottom: 1rem;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  padding: 1rem;
}
</style>
<style>
.filters {
  margin-bottom: 1rem;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  padding: 1rem;
}
</style>
