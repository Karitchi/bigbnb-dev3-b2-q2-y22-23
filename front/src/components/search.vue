<template>
  <div class="container">
      <div id="searchBox">
        <input id="location" type="text" v-model="location" @input="search" placeholder="Where are you going?">
      </div>
    <!-- <main class="container-fluid p-5" id="all-hotels">
      <div class="hotels-list">
        <div v-if="hotels.length">
          <div v-for="hotel in this.hotels" class="row m-0 hotel">
            <card-hotel :hotel="hotel" />
          </div>
        </div>
        <p v-else>No hotels found.</p>
      </div>
    </main> -->
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
      input: "", // Add the input property
    };
  },
  methods: {
    async search() {
      axios
        .get(`${this.$api}hotels/search`, {
          params: {
            location: this.location,
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
      handler(newValue) {
        this.location = newValue;
        this.search();
      },
      immediate: true,
    },
  },
};

// export default {
//   name: "search",
//   components: { CardHotel },
//   data() {
//     return {
//       hotels: [],
//       input: "",
//     };
//   },
//   methods: {
//     search() {
//       // if (this.location.includes("")){
//       //   axios.get(`${this.$api}hotels/hotels/`).then(response => this.hotels = response.data);
//       console.log(location)
//       //}
//       axios.get(`${this.$api}hotels/search`, {
//           params: {
//             location: this.location,
//           },
//         })
//         .then((response) => {
//           this.hotels = response.data;
//         })
//         .catch((error) => {
//           console.log(error);
//         });
//     },
//   },

//   // mounted() {
//   //   axios.get(`${this.$api}hotels/hotels/`)
//   //   .then(response => this.hotels = response.data);
//   // }
// };
</script>

<style scoped>
  @import '../assets/variables.scss';

#all-hotels {
  text-align: center;
}

.hotel {
  display: inline;
}
/* @import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: "Montserrat", sans-serif;
}

body {
  padding: 20px;
  min-height: 100vh;
  background-color: rgb(234, 242, 255);
}

input.search {
  display: block;
  width: 350px;
  margin: 20px auto;
  padding: 10px 45px;
  background: white url("../assets/search-icon.svg") no-repeat 15px center;
  background-size: 15px 15px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}

.item {
  width: 350px;
  margin: 0 auto 10px auto;
  padding: 10px 20px;
  color: white;
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px 0px,
    rgba(0, 0, 0, 0.06) 0px 1px 2px 0px;
}

.location {
  background-color: rgb(97, 62, 252);
  cursor: pointer;
}

.error {
  background-color: tomato;
} */
</style>