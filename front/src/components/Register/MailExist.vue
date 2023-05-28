<template>
  <div v-if="this.isMailExist" class="alert alert-danger" role="alert">
    Un utilisateur avec cette adresse email existe déjà !
  </div>
</template>

<script>
export default {
  name: "MailExist",
  props: ['isMailExist']
}
</script>

<style scoped>

</style>
