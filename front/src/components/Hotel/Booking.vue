<script setup>
import { onMounted, watch, ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'

const route = useRoute()

const arrivalDate = ref(getTodayDate())
const departureDate = ref(getTomorrowDate())
const numberRoomsWanted = ref(1)


const isDateValid = ref(true)
const isNumberRoomsValid = ref(true)

let hotelPrice = null
let numberAvailableRooms = null

const isLoaded = ref(false)


async function getHotel() {
    const response = await fetch(`http://127.0.0.1:8000/hotels/${route.params.id}`)
    const hotel = await response.json()

    return hotel
}

function getTodayDate() {
    const date = new Date();

    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');

    return `${year}-${month}-${day}`;
}

function getTomorrowDate() {
    const date = new Date();
    date.setDate(date.getDate() + 1);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');

    return `${year}-${month}-${day}`;
}

async function book() {
    axios.post(`http://localhost:8000/bookings/`, {
        client_id: 2,
        hotel_id: 1,
        start_date: arrivalDate.value,
        end_date: departureDate.value,
        booked_rooms: numberRoomsWanted.value,
        total_price: 500.00,
        payment_method: "paypal",
    })
        .then(function (response) {
            arrivalDate.value = getTodayDate()
            departureDate.value = getTomorrowDate()
            numberRoomsWanted.value = 1

        })
        .catch(function (error) {
        })

}

onMounted(async () => {
    const hotel = await getHotel()

    hotelPrice = hotel.price
    numberAvailableRooms = hotel.rooms

    isLoaded.value = true
})


// check arrival date validity
watch(arrivalDate, (arrivalDate) => {
    const todayDate = getTodayDate();
    
    arrivalDate < todayDate ? isDateValid.value = false : isDateValid.value = true
})

// check departure date validity
watch(departureDate, (departureDate) => {
    const tomorrowDate = getTomorrowDate();
    
    departureDate < tomorrowDate ? isDateValid.value = false : isDateValid.value = true
})

// check number of booked rooms validity
watch(numberRoomsWanted, (numberRoomsWanted) => {
    numberRoomsWanted < 1 ? isNumberRoomsValid.value = false : isNumberRoomsValid.value = true
    numberRoomsWanted > numberAvailableRooms ? isNumberRoomsValid.value = false : isNumberRoomsValid.value = true
})


async function submitForm(event) {
    event.preventDefault();

    if (isDateValid.value && isNumberRoomsValid.value) {
        await book()
    }
};
</script>

<template>
    <div v-if="!isLoaded" class="text-center">
        <div class="spinner-border" role="status"></div>
    </div>


    <div v-else>
        <h1> {{ hotelPrice }}<i class="bi bi-currency-dollar"></i> per night</h1>


        <form @submit="submitForm" class="needs-validation" novalidate>
            <div class="input-group mb-3">
                <input type="date" id="arrival" class="form-control" :class="{ 'is-valid': isDateValid, 'is-invalid': !isDateValid }" v-model="arrivalDate" required>
                <input type="date" id="departure" class="form-control" :class="{ 'is-valid': isDateValid, 'is-invalid': !isDateValid }" v-model="departureDate" required>
                <div class="invalid-feedback">
                    please enter valid dates
                </div>
            </div>

            <div class="mb-3">
                <label for="rooms" class="form-label">rooms</label>
                <input type="number" class="form-control" min="1" :max="numberAvailableRooms" id="rooms" v-model="numberRoomsWanted" :class="{ 'is-valid': isNumberRoomsValid, 'is-invalid': !isNumberRoomsValid }" required>
                <div class="invalid-feedback">
                    please book between 1 and {{ numberAvailableRooms }} rooms
                </div>
            </div>

            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>