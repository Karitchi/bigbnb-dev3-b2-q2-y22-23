<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router';
import PhotoGalleryHotel from '@/components/PhotoGalleryHotel.vue';
import HotelDetails from '@/components/HotelDetails.vue';

const hotel = ref([])
const route = useRoute()

fetch(`http://127.0.0.1:8000/hotels/${route.params.id}`)
    .then(response => response.json())
    .then(response => hotel.value = response)
</script>

<template>
    <PhotoGalleryHotel />
    <HotelDetails :name="hotel.name" :hotel_owner="hotel.hotel_owner" :image="hotel.image" :description="hotel.description" :city="hotel.city" :rooms="hotel.rooms" :price="hotel.price" />
</template>


<style scoped></style>


