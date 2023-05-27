<template>
  <div class="form-row">
    <div class="form-group col-md-2">
      <label for="register-password">Mot de passe</label>
      <input
          :type="this.checkBoxValue ? 'text' : 'password'"
          id="register-password"
          class="form-control"
          :class="this.password !== '' ? (
              this.hasEnoughChars && this.hasNotToManyChars && containsUppercase && this.containsSpecialChars ? 'is-valid' : 'is-invalid'
              ) : ''"
          :maxlength="this.MAX_CHARS"
          v-model="this.password"
          @input="this.onInputPassword"
          placeholder="Mot de passe"
          required
      />

      <div v-if="this.password !== ''">
        <div v-if="this.password !== ''">
          <div :class="this.getClassOfPasswordRequirements(this.hasEnoughChars)">
            Min {{ this.MIN_CHARS }} caractères
          </div>

          <div :class="this.getClassOfPasswordRequirements(this.hasNotToManyChars)">
            Max {{ this.MAX_CHARS }} caractères
          </div>

          <div :class="this.getClassOfPasswordRequirements(this.containsUppercase)">
            Contient au moins 1 maj.
          </div>

          <div :class="this.getClassOfPasswordRequirements(this.containsNumber)">
            Contient au moins 1 chiffre
          </div>

          <div :class="this.getClassOfPasswordRequirements(this.containsSpecialChars)">
            Contient au moins un caract. spécial
          </div>
        </div>
      </div>
    </div>

    <div class="form-group col-md-2">
      <label for="register-password-confirm">Confirmer le mot de passe</label>
      <input
          :type="this.checkBoxValue ? 'text' : 'password'"
          id="register-password-confirm"
          class="form-control"
          :class="this.confirmPassword !== '' ? (this.password === this.confirmPassword ? 'is-valid' : 'is-invalid') : ''"
          :maxlength="this.MAX_CHARS"
          v-model="this.confirmPassword"
          @input="this.onInputPassword"
          placeholder="Confirmer le mot de passe"
          required
      />

      <div v-if="this.confirmPassword !== ''">
        <div class="valid-input" v-if="this.password === this.confirmPassword">
          Mot de passe identique
        </div>
        <div class="invalid-input" v-else>
          Mot de passe identique
        </div>
      </div>
    </div>
  </div>

  <div>
    <div class="form-switch form-group">
      <input
          class="form-check-input"
          type="checkbox"
          id="register-show-password"
          v-model="this.checkBoxValue"
      />
      <label class="form-check-label" for="register-show-password">Afficher le mot de passe</label>
    </div>
  </div>

</template>

<script>
export default {
  name: "Password",
  emits: ['input'],

  data() {
    return {
      password: '',
      confirmPassword: '',
      hasEnoughChars: false,
      hasNotToManyChars: false,
      containsUppercase: false,
      containsNumber: false,
      containsSpecialChars: false,
      checkBoxValue: false,
      checkBoxText: '',
      MIN_CHARS: 7,
      MAX_CHARS: 20
    }
  },

  methods: {
    onInputPassword() {
      this.hasEnoughChars = this.password.length >= this.MIN_CHARS;
      this.hasNotToManyChars = this.password.length <= this.MAX_CHARS;
      this.containsUppercase = this.password.toLowerCase() !== this.password;
      this.containsNumber = /\d/.test(this.password);
      this.containsSpecialChars = /[@!#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(this.password);
      this.$emit('input', {
        'password': this.password,
        'isValid': this.isValid()
      });
    },

    isValid() {
      return this.hasEnoughChars &&
          this.hasNotToManyChars &&
          this.containsUppercase &&
          this.containsNumber &&
          this.containsSpecialChars &&
          this.password === this.confirmPassword;
    },

    getClassOfPasswordRequirements(condition) {
      return condition ? 'valid-input' : 'invalid-input';
    }
  }
}
</script>

<style scoped>

</style>
