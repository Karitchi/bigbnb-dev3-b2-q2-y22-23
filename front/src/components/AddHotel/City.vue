<template>
  <div class="form-row">
    <div class="form-group">
      <label for="add-hotel-city">Où se trouve votre hôtel ?</label>
      <select
          id="add-hotel-city"
          class="form-select"
          :class="this.isValid ? 'is-valid' : 'is-invalid'"
          v-model="this.city"
          @input="this.onInput"
      >
        <option
            v-for="city in this.cities"
            :value="city.id"
        >{{ city.name }}</option>
      </select>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'City',
  emits: ['input'],

  data() {
    return {
      cities: [],
      city: null,
      isValid: true
    }
  },

  methods: {
    onInput() {
      this.$emit('input', {'city': this.city, 'isValid': this.isValid});
    },

    setCities(responseData) {
      this.cities = responseData;
      if (this.cities.length === 0) {
        return;
      }
      this.city = this.cities[0].id;
      this.$emit('input', {'city': this.city, 'isValid': this.isValid});
    }
  },

  mounted() {
    axios.get(`${this.$api}cities/`).then(response => this.setCities(response.data));
  }
}
</script>

<style scoped>
#add-hotel-city {
  width: auto;
}
</style>