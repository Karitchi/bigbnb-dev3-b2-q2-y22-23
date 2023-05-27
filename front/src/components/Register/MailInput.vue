<template>
  <div class="form-row">
    <div class="form-group col-md-2">
      <label for="register-client-email">Adresse email</label>
      <input
          type="email"
          id="register-client-email"
          class="form-control"
          :class="(this.mail !== '') ? ((this.isValid) ? 'is-valid' : 'is-invalid') : ''"
          v-model="this.mail"
          placeholder="exemple@bnb.com"
          @input="this.onInput"
      />

      <div v-if="this.mail !== ''">
        <div class="valid-input" v-if="this.isValid">
          Email valide
        </div>
        <div class="invalid-input" v-else>
          Email invalide
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "MailInput",
  emits: ['input-mail'],

  data() {
    return {
      isValid: false,
      mail: ''
    }
  },

  methods: {
    onInput() {
      this.isValid =
          /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.mail);
      this.$emit('input-mail', {
        'mail': this.mail,
        'isValid': this.isValid
      });
    }
  }
}
</script>

<style scoped>

</style>
