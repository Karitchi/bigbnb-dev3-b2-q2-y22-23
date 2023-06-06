<template>
  <form>

    <!-- search bar -->
    <div id="searchBox" class="mt-3 input-group mb-3 w-50 mx-auto">
      <input class="search p-2 form-control" type="text" v-model="location" placeholder="Where are you going?">
      <button type="submit" class="btn btn-primary" @click="this.search" :disabled="this.inResearch">
        <span class="d-none d-sm-inline">
          {{ this.inResearch ? 'Recherche en cours ...' : 'Rechercher' }}
        </span>
        <i class="bi bi-search ms-2"></i>
      </button>
    </div>

    <!-- filters -->
    <div class="d-flex justify-content-center">
      <div class="row row-cols-1 row-cols-sm-2 ms-2 me-2">

        <!-- price -->
        <div class="col mb-3">
          <label for="price">Price: </label>
          <div class="input-group" id="price">
            <input class="form-control" id="min-price" type="number" v-model="priceRange[0]" placeholder="Min">
            <input class="form-control" id="max-price" type="number" v-model="priceRange[1]" placeholder="Max">
          </div>
        </div>

        <!-- rooms -->
        <div class="col mb-3">
          <label for="rooms">Room quantity:</label>
          <div class="input-group" id="rooms">
            <input class="form-control" id="min-rooms" type="number" v-model="roomRange[0]" placeholder="Min">
            <input class="form-control" id="max-rooms" type="number" v-model="roomRange[1]" placeholder="Max">
          </div>
        </div>

      </div>
    </div>

  </form>
</template>

<script>
import axios from 'axios';
import CardHotel from "@/components/CardHotel";

export default {
  name: "search",
  components: { CardHotel },
  emits: ['input'],

  data() {
    return {
      hotels: [],
      input: "",
      location: '',
      priceRange: [0, 2000],
      roomRange: [0, 500],
      inResearch: false,
    };
  },

  methods: {
    search(e) {
      this.inResearch = true;
      axios
        .get(`${this.$api}hotels/search`, {
          params: {
            location: this.location,
            min_price: this.priceRange[0],
            max_price: this.priceRange[1],
            min_room: this.roomRange[0],
            max_room: this.roomRange[1],
          }
        })
        .then(response => this.sendResult(response.data))
        .catch(error => this.onResearchError(error));

      e.preventDefault();
    },

    sendResult(data) {
      this.inResearch = false;
      this.$emit('input', { 'hotels': data });
    },

    onResearchError(error) {
      this.inResearch = false;
      console.log(error);
    },
  },

  mounted() {
    axios.get(`${this.$api}hotels/`)
      .catch(error => console.log(error))
      .then(response => this.$emit('input', { 'hotels': response.data }));
  },
};

</script>