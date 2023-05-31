<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios';
import { getID } from '@/main.ts'

const route = useRoute()

const review = ref('');
const rating = ref(null);
const showSuccessToast = ref(false);

const reviewButton = ref(null)

const successToast = ref(null)
const loginFailureToast = ref(null)
const hotelOwnerFailureToast = ref(null)



let numberOfStars = 5


const isHovered = ref(false)
const starsHovered = ref([true, true, true, true, true])


function mouseenter(index, isHovered) {
    starsHovered.value = starsHovered.value.map(() => false);

    for (let i = 0; i <= index; i++) {
        starsHovered.value.splice(i, true, isHovered);
    }
}
function mouseleave() {
    if (!numberOfStars) {
        starsHovered.value = starsHovered.value.map(() => true);
        return 0
    }

    starsHovered.value = starsHovered.value.map(() => false);

    for (let i = 0; i < numberOfStars; i++) {
        starsHovered.value[i] = true
    }
}
function click() {
    numberOfStars = 0

    for (const star of starsHovered.value) {
        if (star) {
            numberOfStars++
        }
    }
}

function printSuccessToast() {
    const toastTrigger = reviewButton.value
    const toastLiveExample = successToast.value

    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)

    toastBootstrap.show()
}

function printLoginFailureToast() {
    const toastTrigger = reviewButton.value
    const toastLiveExample = loginFailureToast.value

    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)

    toastBootstrap.show()
}

function printHotelOwnerFailureToast() {
    const toastTrigger = reviewButton.value
    const toastLiveExample = hotelOwnerFailureToast.value

    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)

    toastBootstrap.show()
}

function submitForm(event) {
    event.preventDefault();
    let userID = null

    // check if the user is connected and if he is get his user id
    try {
        userID = getID();
    } catch (error) {
        printFailureToast()
        return
    }

    axios.post(`http://localhost:8000/reviews/hotel/${route.params.id}/`, {
        client_id: userID,
        hotel_id: route.params.id,
        review: review.value,
        rating: numberOfStars,
    })
        .then(function (response) {
            review.value = ''
            numberOfStars = 5
            starsHovered.value = starsHovered.value.map(() => true);
            printSuccessToast()
        })
        .catch(function (error) {
            printHotelOwnerFailureToast()
        });
};
</script>

<template>
    <form @submit="submitForm">

        <!-- stars -->
        <div class="mb-3">
            <i v-for="(isHovered, index) in starsHovered" :key="index" :class="{ 'bi': true, 'bi-star-fill': isHovered, 'bi-star': !isHovered, 'text-success': true }" @mouseenter="mouseenter(index, true)" @mouseleave="mouseleave" @click="click"></i>
        </div>

        <!-- text field -->
        <div class="mb-3">
            <label for="review" class="form-label"></label>
            <input type="text" class="form-control" v-model="review" id="review" rows="3" placeholder="Give us your opinion" required>
        </div>

        <!-- submit button -->
        <button type="submit" id="reviewButton" ref="reviewButton" class="btn btn-primary">Submit</button>

        <!-- success toast -->
        <div class="toast-container position-fixed top-0 end-0 p-3">
            <div id="successToast" ref="successToast" class="toast" role="alert" aria-live="assertive" aria-atomic="false">
                <div class="toast-header">
                    <i class="bi bi-check-lg me-2"></i>
                    <strong class="me-auto text-success">Success</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body ">
                    Your comment is posted!
                </div>
            </div>
        </div>

        <!-- login failure toast -->
        <div class="toast-container position-fixed top-0 end-0 p-3">
            <div id="loginFailureToast" ref="loginFailureToast" class="toast" role="alert" aria-live="assertive" aria-atomic="false">
                <div class="toast-header">
                    <i class="bi bi-x me-2"></i>
                    <strong class="me-auto text-danger">Failure</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body ">
                    Please login to post your comment
                </div>
            </div>
        </div>


        <!-- login  as hotel owner failure toast -->
        <div class="toast-container position-fixed top-0 end-0 p-3">
            <div id="hotelOwnerFailureToast" ref="hotelOwnerFailureToast" class="toast" role="alert" aria-live="assertive" aria-atomic="false">
                <div class="toast-header">
                    <i class="bi bi-x me-2"></i>
                    <strong class="me-auto text-danger">Failure</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body ">
                    Hotel owners cannot post comments
                </div>
            </div>
        </div>
    </form>
</template>

