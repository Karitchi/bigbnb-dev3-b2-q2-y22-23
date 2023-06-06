<template>
  <div class="form-row">
    <div class="form-group col-md-2">
      <label for="add-hotel-phone-number">Numéro de téléphone</label>
      <input
          id="add-hotel-phone-number"
          type="text"
          class="form-control"
          :class="this.phoneNumber !== '' ? (this.isValid ? 'is-valid': 'is-invalid') : ''"
          v-model="this.phoneNumber"
          @input="this.onInput"
          placeholder="0123456789"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'PhoneNumber',
  emits: ['input'],

  data() {
    return {
      phoneNumber: '',
      isValid: false
    }
  },

  methods: {
    onInput() {
      this.isValid = /^[0-9]{10}$/.test(this.phoneNumber);
      this.$emit('input', {'phoneNumber': this.phoneNumber, 'isValid': this.isValid});
    }
  }
}
</script>