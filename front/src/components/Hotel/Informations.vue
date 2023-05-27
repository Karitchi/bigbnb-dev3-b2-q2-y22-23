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

    // console.log(response)
    // hotel_owner.value = await response.json()

    // console.log(hotel.value)
    // console.log(city.value)
    // console.log(hotel_owner.value)

    isLoaded.value = true
})
</script>

<template>
    <div v-if="!isLoaded" class="text-center">
        <div class="spinner-border" role="status"></div>
    </div>

    <div v-else class="pb-3 pt-3 rounded border border-secondary-subtle">

        <h1 class="h1">{{ hotel.name }}</h1>
        <hr class="pb-3">

        <div>
            <h5 class="pt-2 pb-2">{{ hotel.rooms }} rooms left</h5>
            <h5 class="bi bi-geo pt-2 pb-2"> Located in {{ city.name }}, {{ city.country }}</h5>
            <h5 class="bi bi-wallet pt-2 pb-2"> {{ hotel.price }} dollars per night</h5>
        </div>

        <hr class="pb-3">

        <h3>About this hotel</h3>
        <h5 class="pt-2 pb-2">{{ hotel.description }}</h5>

        <hr class="pb-3">

        <div class="row">
            <div class="col">
                <div class="card text-center">
                    <div class="card-body">
                        <h5 class="card-title">Proposed by {{ hotel_owner.name }} {{ hotel_owner.lastname }} from {{ hotel_owner.company }}</h5>
                        <p class="card-text">Contact: {{ hotel_owner.mail }}</p>
                    </div>
                </div>
            </div>
        </div>


        <!-- <p>{{ city.location_x }}</p>
        <p>{{ city.location_y }}</p> -->

    </div>
</template>