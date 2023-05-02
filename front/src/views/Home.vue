<template>
  <div class="container-fluid p-5">
    <div class="row m-0">
      <card />
      <card />
      <card />
      <card />
      <card />
      <card />
      <card />
      <card />
      <card />
      <card />
      <card />
      <card />
      <card />
      <card />
    </div>
  </div>
</template>

<style scoped>
  @import '../assets/variables.scss'
</style>


<script lang="ts">
import Card from '../components/Card.vue'

export default {
    name: 'App',
    components: {
        Card,
    }
}
</script>
