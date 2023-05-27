<template>
  <div class="form-row">
    <div class="form-group col-md-2">
      <label for="register-society">Nom de la société</label>
      <input
          type="text"
          id="register-society"
          class="form-control"
          :class="this.society !== '' ? (this.society.length <= this.MAX_CHARS ? 'is-valid' : 'is-invalid') : ''"
          v-model="this.society"
          @input="this.onInput"
          :maxlength="this.MAX_CHARS"
          placeholder="Ibis"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "Society",
  emits: ['input'],

  data() {
    return {
      society: '',
      MAX_CHARS: 50
    }
  },

  methods: {
    onInput() {
      this.$emit('input', {
        'society': this.society,
        'isValid': this.society !== '' && this.society.length <= this.MAX_CHARS
      });
    }
  }
}
</script>

<style scoped>

</style>
