<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'

const route = useRoute()

const arrivalDate = ref('')
const departureDate = ref('')
const numberOfRooms = ref(0)
const hotelPrice = ref(null)

const isLoaded = ref(false)


onMounted(async () => {
    let response
    let hotel

    response = await fetch(`http://127.0.0.1:8000/hotels/${route.params.id}`)
    hotel = await response.json()

    hotelPrice.value = hotel.price

    isLoaded.value = true
})

function submitForm(event) {
    event.preventDefault();

    axios.post(`http://localhost:8000/bookings/`, {
        client_id: 2,
        hotel_id: 1,
        start_date: arrivalDate.value,
        end_date: departureDate.value,
        booked_rooms: numberOfRooms.value,
        total_price: 500.00,
        payment_method: "paypal",
    })
        .then(function (response) {
            console.log(response)
        })
        .catch(function (error) {
            console.log(error);
        });
};
</script>

<template>
    <div v-if="!isLoaded" class="text-center">
        <div v-if="!isLoaded" class="spinner-border" role="status"></div>
    </div>


    <div v-else class="pb-3 pt-3 col rounded border border-secondary-subtle">
        <h5> {{ hotelPrice }} per nights</h5>
        <form class="" @submit="submitForm">

            <div class="input-group mb-3">
                <input type="date" id="arrival" class="form-control" v-model="arrivalDate">
                <input type="date" id="departure" class="form-control" v-model="departureDate">
            </div>

            <div class="mb-3">
                <label for="rooms" class="form-label">rooms</label>
                <input type="number" class="form-control" id="rooms" v-model="numberOfRooms">
            </div>

            <button type="submit" class="btn btn-primary">Submit</button>
        </form>

    </div>
</template>