<script setup lang="ts">
defineProps([
  "id",
  "name",
  "description",
  "hotel_owner",
])
</script>

<template>
  <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3 col-xl-2 p-3" id="hotel-card">
    <div class="card m-auto">
      <img src="https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" class="card-img-top" alt="...">
      <div class="card-body">
        <h3 class="cart-title">{{ name }}</h3>
        <p class="card-text"> <i>{{ description }}</i></p>
        <router-link :to="'/hotels/' + id" class="btn btn-outline-primary">Plus d'informations</router-link>
        <p class="card-footer">By <i>{{ hotel_owner }}</i></p>
      </div>
    </div>
  </div>
</template>

<style scoped>
#hotel-card {
  display: inline-block;
}
</style>
