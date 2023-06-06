<template>
  <div class="form-row">
    <div class="form-group col-md-2">
      <label for="register-name">Nom de famille</label>
      <input
          type="text"
          id="register-name"
          class="form-control"
          :class="this.name !== '' ? (this.name.length <= this.MAX_CHARS ? 'is-valid' : 'is-invalid') : ''"
          v-model="this.name"
          :maxlength="this.MAX_CHARS"
          placeholder="Nom"
          @input="this.onInput"
      />
    </div>
    <div class="form-group col-md-2">
      <label for="register-lastname">Prénom</label>
      <input
          type="text"
          id="register-lastname"
          class="form-control"
          :class="this.lastname !== '' ? (this.lastname.length <= this.MAX_CHARS ? 'is-valid' : 'is-invalid') : ''"
          v-model="this.lastname"
          :maxlength="this.MAX_CHARS"
          placeholder="Prénom"
          @input="this.onInput"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "NameInput",
  emits: ['input'],

  data() {
    return {
      name: '',
      lastname: '',
      MAX_CHARS: 50
    }
  },

  methods: {
    onInput() {
      this.$emit('input', {
        'name': this.name,
        'lastname': this.lastname,
        'isValid': this.name !== '' && this.lastname !== '' && this.name.length <= this.MAX_CHARS && this.lastname.length <= this.MAX_CHARS
      });
    }
  }
}
</script>

<style scoped>

</style>
