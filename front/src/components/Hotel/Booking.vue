<script setup>
import { onMounted, watch, ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'
import { getID } from '@/main.ts'


const route = useRoute()

const arrivalDate = ref(getTodayDate())
const departureDate = ref(getTomorrowDate())
const numberRoomsWanted = ref(1)


const isDateValid = ref(true)
const isNumberRoomsValid = ref(true)

let hotelPrice = null
let numberAvailableRooms = null

const bookButton = ref(null)
const successToast = ref(null)
const failureToast = ref(null)

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

function printSuccessToast() {
    const toastTrigger = bookButton.value
    const toastLiveExample = successToast.value

    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)

    toastBootstrap.show()
}

function printFailureToast() {
    const toastTrigger = bookButton.value
    const toastLiveExample = failureToast.value

    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)

    toastBootstrap.show()
}

async function book() {
    let userID = null

    // check if the user is connected and if he is get his user id
    try {
        userID = getID();
    } catch (error) {
        printFailureToast()
        return
    }

    // add booking
    axios.post(`http://localhost:8000/bookings/`, {
        client_id: userID,
        hotel_id: 1,
        start_date: arrivalDate.value,
        end_date: departureDate.value,
        booked_rooms: numberRoomsWanted.value,
        total_price: 500.00,
        payment_method: "paypal",
    })
        .then(function (response) {
            // reset book form value
            arrivalDate.value = getTodayDate()
            departureDate.value = getTomorrowDate()
            numberRoomsWanted.value = 1
            printSuccessToast()
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
    if (numberRoomsWanted < 1) {
        isNumberRoomsValid.value = false
    } else if (numberRoomsWanted > 1) {
        isNumberRoomsValid.value = true
    } else if (numberRoomsWanted > numberAvailableRooms) {
        isNumberRoomsValid.value = false
    } else {
        isNumberRoomsValid.value = true
    }

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

        <!-- hotel price -->
        <h1> {{ hotelPrice }}<i class="bi bi-currency-dollar"></i> <span class="text-secondary">per night</span> </h1>


        <form @submit="submitForm" class="needs-validation" novalidate>

            <!-- dates labels -->
            <div class="row">
                <div class="col">
                    <label for="departureDate" class="form-label text-secondary"> departureDate</label>
                </div>
                <div class="col">
                    <label for="arrivalDate" class="form-label text-secondary">arrivalDate</label>
                </div>
            </div>

            <!-- dates -->
            <div class="input-group mb-3">
                <input type="date" id="arrivalDate" class="form-control" :class="{ 'is-valid': isDateValid, 'is-invalid': !isDateValid }" v-model="arrivalDate" required>
                <input type="date" id="departureDate" class="form-control" :class="{ 'is-valid': isDateValid, 'is-invalid': !isDateValid }" v-model="departureDate" required>
            </div>
            <div class="invalid-feedback">
                please enter valid dates
            </div>

            <!-- number of wanted rooms -->
            <div class="mb-3">
                <label for="rooms" class="form-label text-secondary">wanted rooms</label>
                <input type="number" class="form-control" min="1" :max="numberAvailableRooms" id="rooms" v-model="numberRoomsWanted" :class="{ 'is-valid': isNumberRoomsValid, 'is-invalid': !isNumberRoomsValid }" required>

                <div class="invalid-feedback">
                    please book between 1 and {{ numberAvailableRooms }} rooms
                </div>
            </div>

            <!-- submit button -->
            <button id="bookButton" ref="bookButton" type="submit" class="btn btn-primary">book</button>

            <!-- success toast -->
            <div class="toast-container position-fixed top-0 end-0 p-3">
                <div id="successToast" ref="successToast" class="toast" role="alert" aria-live="assertive" aria-atomic="false">
                    <div class="toast-header">
                        <i class="bi bi-check-lg me-2"></i>
                        <strong class="me-auto text-success">Success</strong>
                        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                    </div>
                    <div class="toast-body ">
                        The hotel is booked
                    </div>
                </div>
            </div>

            <!-- failure toast -->
            <div class="toast-container position-fixed top-0 end-0 p-3">
                <div id="failureToast" ref="failureToast" class="toast" role="alert" aria-live="assertive" aria-atomic="false">
                    <div class="toast-header">
                        <i class="bi bi-x me-2"></i>
                        <strong class="me-auto text-danger">Failure</strong>
                        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                    </div>
                    <div class="toast-body ">
                        Please login to book an hotel
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>