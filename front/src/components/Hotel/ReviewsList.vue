<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute()

const reviews = ref([])
const clients = ref([])

const isLoaded = ref(false)


async function fetchReviews() {
    // fetch all reviews of the hotel and store them in reviews array 

    let response = await fetch(`http://localhost:8000/reviews/hotel/${route.params.id}`)
    let reviews = await response.json()

    return reviews
}
async function fetchClients() {
    // fetch the client of each review and store them in clients array

    let clients = []

    for (let review of reviews.value) {
        let response = await fetch(`http://localhost:8000/clients/${review.client_id}`)
        let client = await response.json()
        clients.push(client)
    }

    return clients
}
function changeDateFormat() {
    // change the date format of the review 

    for (let review of reviews.value) {
        const dateObj = new Date(review.date);

        review.date = dateObj.toLocaleDateString('fr-FR', {
            day: 'numeric',
            month: 'long',
            year: 'numeric',
            timeZone: 'Europe/Brussels' // Adjust the time zone as per your requirement
        });
    }
}

onMounted(async () => {
    reviews.value = await fetchReviews()
    clients.value = await fetchClients()
    changeDateFormat()

    isLoaded.value = true
})
</script>

<template>
    <!-- loading spinner -->
    <div v-if="!isLoaded" class="text-center">
        <div class="spinner-border" role="status"></div>
    </div>

    <!-- reviews -->
    <div class="row m-0">
        <div v-for="(item, index) in reviews" class="col-lg-6 p-2  mb-3">

            <!-- client name -->
            <h5>{{ clients[index]?.info?.name }}</h5>

            <!-- date and start -->
            <p class="text-secondary">
                <span>{{ item.date }}</span>
                <span v-for="star of item.rating" class="bi bi-star-fill text-success"></span>
            </p>

            <!-- review text -->
            <p style="max-height: 100px; overflow: auto;">{{ item.review }}</p>
        </div>
    </div>
</template>