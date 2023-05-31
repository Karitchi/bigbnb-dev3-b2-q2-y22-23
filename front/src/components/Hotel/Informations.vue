<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'

const route = useRoute()

const hotel = ref(null)
const city = ref(null)
const hotel_owner = ref(null)

const isLoaded = ref(false)

onMounted(async () => {
    let response

    response = await fetch(`http://127.0.0.1:8000/hotels/${route.params.id}`)
    hotel.value = await response.json()

    response = await fetch(`http://127.0.0.1:8000/cities/${hotel.value.city}`)
    city.value = await response.json()

    // response = await fetch(`http://127.0.0.1:8000/hotel_owners/${hotel.value.hotel_owner}`)
    await axios.get(`http://127.0.0.1:8000/hotel_owners/${hotel.value.hotel_owner}/`).then(response => hotel_owner.value = response.data);

    isLoaded.value = true
})
</script>

<template>
    <div v-if="!isLoaded" class="text-center">
        <div class="spinner-border" role="status"></div>
    </div>

    <div v-else>

        <!-- hotel name -->
        <h1 class="h1">{{ hotel.name }}</h1>
        <hr class="pb-3">

        <!-- location -->
        <h5 class="bi bi-geo pt-2 pb-2"> Located in {{ city.name }}, {{ city.country }}</h5>

        <!-- rooms left -->
        <h5 class="pt-2 pb-2">
            <i class="fa fa-bed"></i>
            {{ hotel.rooms }} rooms left
        </h5>

        <hr class="pb-3">

        <!-- abbout -->
        <h3>About this hotel</h3>
        <p class="pt-2 pb-2" style="height: 100px; overflow: auto;">{{ hotel.description }}</p>

        <hr class="pb-3">

        <div class="row">
            <div class="col">
                <h5 class="mb-3">Proposed by {{ hotel_owner.company }}</h5>
                <ul class="list-group">
                    <li class="list-group-item m-0">Mail: {{ hotel.mail }}</li>
                    <li class="list-group-item m-0">Phone number: {{ hotel.phone_number }}</li>
                </ul>
            </div>
        </div>
    </div>
</template>