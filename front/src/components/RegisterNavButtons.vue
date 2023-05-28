<template>
  <div class="btn-group btn-group-toggle" data-toogle="buttons" style="padding: 10px" v-if="this.isClient">
    <label class="btn btn-secondary active">
        <input type="radio" name="register" autocomplete="off" checked>Je suis un client
    </label>
    <label class="btn btn-secondary">
      <input type="radio" name="register" autocomplete="off" @click="this.goTo">Je suis un hôtelier
    </label>
  </div>

  <div class="btn-group btn-group-toggle" data-toogle="buttons" style="padding: 10px" v-else>
    <label class="btn btn-secondary">
      <input type="radio" name="register" autocomplete="off" @click="this.goTo">Je suis un client
    </label>
    <label class="btn btn-secondary active">
      <input type="radio" name="register" autocomplete="off" checked>Je suis un hôtelier
    </label>
  </div>
</template>

<script>
export default {
  name: "RegisterNavButtons",
  props: ['isClient'],

  methods: {
    goTo() {
      if (this.isClient) {
        this.$router.push('/register_hotel_owner');
      } else {
        this.$router.push('/register_client');
      }
    },

    tryRegister() {

    }
  }
}
</script>

<style scoped>

</style>
