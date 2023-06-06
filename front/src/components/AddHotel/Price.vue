<template>
  <div class="form-row">
    <div class="form-group col-md-2">
      <label for="add-hotel-price">Prix de l'hôtel</label>
      <input
          id="add-hotel-price"
          type="number"
          class="form-control"
          :class="this.price !== null ? (this.isValid ? 'is-valid' : 'is-invalid') : ''"
          @input="this.onInput"
          v-model="this.price"
          min="1"
          :max="this.MAX_PRICE"
          placeholder="10€"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Price',
  emits: ['input'],

  data() {
    return {
      price: null,
      isValid: false,
      MAX_PRICE: 999999
    }
  },

  methods: {
    onInput() {
      this.isValid = this.price !== null && this.price > 0 && this.price <= this.MAX_PRICE;
      this.$emit('input', {'price': Number(this.price).toFixed(2), 'isValid': this.isValid});
    }
  }
}
</script>