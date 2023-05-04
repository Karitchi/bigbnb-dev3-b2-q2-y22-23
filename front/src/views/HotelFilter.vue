<template>
  <div>
    <h1>Hotel Filtering</h1>

    <div class="filters">
      <label>Price Range:</label>
      <input type="number" v-model="minPrice" placeholder="Min Price">
      <input type="number" v-model="maxPrice" placeholder="Max Price">
    </div>

    <div class="filters">
      <label>Rating:</label>
      <select v-model="selectedRating">
        <option value="">All</option>
        <option value="5">5 Stars</option>
        <option value="4">4 Stars</option>
        <option value="3">3 Stars</option>
      </select>
    </div>

    <ul>
      <li v-for="hotel in filteredHotels" :key="hotel.id">
        <h3>{{ hotel.name }}</h3>
        <p>Price: {{ hotel.price }}</p>
        <p>Rating: {{ hotel.rating }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hotels: [
        { id: 1, name: 'Hotel A', price: 100, rating: 4 },
        { id: 2, name: 'Hotel B', price: 200, rating: 5 },
        { id: 3, name: 'Hotel C', price: 150, rating: 3 },
        // Add more hotels as needed
      ],
      minPrice: null,
      maxPrice: null,
      selectedRating: '',
    };
  },
  computed: {
    filteredHotels() {
      return this.hotels.filter((hotel) => {
        const matchesPrice =
          (this.minPrice === null || hotel.price >= this.minPrice) &&
          (this.maxPrice === null || hotel.price <= this.maxPrice);

        const matchesRating =
          this.selectedRating === '' || hotel.rating === parseInt(this.selectedRating);

        return matchesPrice && matchesRating;
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
