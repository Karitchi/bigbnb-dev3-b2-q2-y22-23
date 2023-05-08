<script setup lang="ts">
import { ref } from 'vue'
import CardHotel from '@/components/CardHotel.vue'

const hotels = ref([])

fetch('http://127.0.0.1:8000/hotels/')
  .then(response => response.json())
  .then(response => hotels.value = response)
</script>


<template>
  <CardHotel v-for="hotel in hotels" :key="hotel.id" :id="hotel.id" :name="hotel.name" :description="hotel.description" :hotel_owner="hotel.hotel_owner" />
</template>

<style scoped></style>


