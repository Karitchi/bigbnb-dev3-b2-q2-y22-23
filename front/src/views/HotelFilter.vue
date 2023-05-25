<template>
  <div class="container">
    <aside class="sidebar">
      <div class="filter_input">
        <label>Price :</label>
        <input id="min_price" type="number" v-model="priceRange[0]" @input="fetchHotels">
        <input id="max_price" type="number" v-model="priceRange[1]" @inpute="fetchHotels">

        <label>Room quantity:</label>
        <input id="min_room" type="number" v-model="roomRange[0]" @input="fetchHotels">
        <input id="max_room" type="number" v-model="roomRange[1]" @input="fetchHotels">
      </div>
    </aside>
    <main class="main-content">
      <div class="hotels-list">
        <ul v-if="hotels.length">
          <li v-for="hotel in hotels" :key="hotel.id">
            <card-hotel :hotel="hotel" />
          </li>
        </ul>
        <p v-else>No hotels found.</p>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';
import CardHotel from "@/components/CardHotel";

export default {
  name: "HotelFilter",
  components: { CardHotel },
  data() {
    return {
      hotels: [],
      priceRange: [0, 2000],
      roomRange: [0, 500],
    };
  },
  methods: {
    fetchHotels() {
      if (this.priceRange.includes("") || this.roomRange.includes("")){
        return
      }
      axios.get(`${this.$api}hotels/filter_hotels`, {
          params: {
            min_price: this.priceRange[0],
            max_price: this.priceRange[1],
            min_room: this.roomRange[0],
            max_room: this.roomRange[1],
          },
        })
        .then((response) => {
          this.hotels = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    axios.get(`${this.$api}hotels/filter_hotels`, {
      params: {
        min_price: this.priceRange[0],
        max_price: this.priceRange[1],
        min_room: this.roomRange[0],
        max_room: this.roomRange[1],
      }
    })
    .then(response => this.hotels = response.data);
  }
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

.filter_input {
  display: flex;
  align-items: center;
}

.filter_input label {
  margin: 1rem;
  font-weight: bold;
}

.filter_input input {
  border: 1px solid #ccc;
  border-radius: 0.25rem;
  padding: 0.5rem;
  font-size: 0.75rem;
  margin-bottom: 0.5rem;
}

.filter_input input[type="number"] {
  -moz-appearance: textfield;
  width: 75px;
  height: 24px;
  padding: 4px;
  font-size: 12px;
  margin: 0.25rem;
}

.min-max-input-container input::-webkit-outer-spin-button,
.min-max-input-container input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.min-max-input-container input:disabled {
  opacity: 0.5;
}

.container {
  display: flex;
  flex-direction: column;
}

.sidebar {
  padding: 1rem;
  background-color: #f5f5f5;
}

.main-content {
  padding: 1rem;
}

.hotels-list {
  margin-top: 1rem;
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
