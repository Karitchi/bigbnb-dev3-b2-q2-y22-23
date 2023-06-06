<template>
  <div class="form-row">
    <div class="form-group col-md-2">
      <label for="add-hotel-description">Description</label>
      <textarea
          id="add-hotel-description"
          class="form-control"
          :class="this.description !== '' ? (this.isValid ? 'is-valid' : 'is-invalid'): ''"
          v-model="this.description"
          placeholder="Votre hôtel en quelques mots"
          maxlength="2000"
          rows="3"
          @input="this.onInput"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'HotelDescription',
  emits: ['input'],

  data() {
    return {
      description: '',
      isValid: ''
    }
  },

  methods: {
    onInput() {
      this.isValid = this.description !== '' && this.description.length <= 2000;
      this.$emit('input', {'isValid': this.isValid, 'description': this.description});
    }
  }
}
</script>

<style scoped>

</style>