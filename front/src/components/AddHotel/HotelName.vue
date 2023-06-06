<template>
  <div class="form-row">
    <div class="form-group col-md-2">
      <label for="add-hotel-name">Nom de l'hôtel</label>
      <input
          type="text"
          id="add-hotel-name"
          class="form-control"
          :class="this.name !== '' ? (this.isValid ? 'is-valid' : 'is-invalid') : ''"
          v-model="this.name"
          placeholder="Mon Hôtel"
          maxlength="30"
          @input="this.onInput"
      />
    </div>
  </div>
</template>

<script>

export default {
  name: "HotelName",
  emits: ['input'],

  data() {
    return {
      name: '',
      isValid: false
    }
  },

  methods: {
    onInput() {
      this.isValid = this.name !== '' && this.name.length <= 30;
      this.$emit('input', {'name': this.name, 'isValid': this.isValid});
    }
  }
}
</script>
