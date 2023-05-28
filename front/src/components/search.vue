<template>
  <div class="container">
    <div id="searchBox">
      <input class="search" type="text" v-model="location" @input="search" placeholder="Where are you going?">
    </div>
    <div class="filter_input">
      <label>Price :</label>
        <input id="min_price" type="number" v-model="priceRange[0]" @input="search" placeholder="Minimum price">
        <input id="max_price" type="number" v-model="priceRange[1]" @input="search" placeholder="Maximum price price">

      <label>Room quantity:</label>
        <input id="min_room" type="number" v-model="roomRange[0]" @input="search" placeholder="Minimum room">
        <input id="max_room" type="number" v-model="roomRange[1]" @input="search" placeholder="Maximum room">
    </div>
    <main class="container-fluid p-5" id="all-hotels">
      <div class="hotels-list">
        <div v-if="hotels.length">
          <div v-for="hotel in this.hotels" class="row m-0 hotel">
            <card-hotel :hotel="hotel" />
          </div>
        </div>
        <p v-else>No hotels found.</p>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios';
import CardHotel from "@/components/CardHotel";

export default {
  name: "search",
  components: { CardHotel },
  data() {
    return {
      hotels: [],
      input: "",
      priceRange: [0, 2000],
      roomRange: [0, 500],
    };
  },
  methods: {
    async search() {
      axios
        .get(`${this.$api}hotels/search`, {
          params: {
            location: this.location,
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
  watch: {
  input: {
    handler(newValues) {
      this.location = newValues[0];
      this.min_price = newValues[1];
      this.max_price = newValues[2];
      this.min_room = newValues[3];
      this.max_room = newValues[4];
      this.search();
    },
    immediate: true,
    deep: true,
  },
},
};

</script>

<style scoped>
  @import '../assets/variables.scss';
  
  /* .filters {
    margin-bottom: 1rem;
  } */
  
  .filter_input {
    display: block;
    text-align: center;
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

  .hotels-list {
    margin-top: 1rem;
  }

#all-hotels {
  text-align: center;
}

.hotel {
  display: inline;
}
@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");


body {
  padding: 20px;
  min-height: 100vh;
  background-color: rgb(234, 242, 255);
}

input.search {
  display: block;
  width: 600px;
  margin: 40px auto 20px auto;
  padding: 15px 45px;
  background: white url("../assets/search-icon.svg") no-repeat 15px center;
  background-size: 15px 15px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}

input.filter_input {
  display: block;
  width: 600px;
  margin: 40px auto 20px auto;
  padding: 15px 45px;
  background: white url("../assets/search-icon.svg") no-repeat 15px center;
  background-size: 15px 15px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}
</style>