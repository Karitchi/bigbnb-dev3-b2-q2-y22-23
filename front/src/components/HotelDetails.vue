<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router';

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

    response = await fetch(`http://127.0.0.1:8000/hotel_owners/${hotel.value.hotel_owner}`)
    hotel_owner.value = await response.json()

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

    <div v-else class="container-fluid p-5">


        <h1 class="h1">{{ hotel.name }}</h1>
        <h3>{{ hotel.description }}</h3>
        <hr>



        <div class="row">
            <div class="col">
                <div class="card text-center bg-secondary-subtle">
                    <div class="card-body">
                        <h5 class="card-title">{{ hotel.rooms }} rooms left</h5>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card text-center bg-secondary-subtle">
                    <div class="card-body">
                        <h5 class="card-title">Located in {{ city.name }}, {{ city.country }}</h5>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card text-center bg-secondary-subtle">
                    <div class="card-body">
                        <h5 class="card-title">For {{ hotel.price }} dollars</h5>
                    </div>
                </div>
            </div>
        </div>

        <hr>
        <div class="row">
            <div class="col">
                <div class="card text-center bg-secondary-subtle">
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