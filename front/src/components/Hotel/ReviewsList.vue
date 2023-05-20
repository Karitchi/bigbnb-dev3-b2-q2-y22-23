<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute()

const reviews = ref([])
const clients = ref([])

const isLoaded = ref(false)


onMounted(async () => {
    let response = null
    let client = null

    response = await fetch(`http://localhost:8000/reviews/hotel/${route.params.id}`)
    reviews.value = await response.json()

    for (let review of reviews.value) {
        response = await fetch(`http://localhost:8000/clients/${review.client_id}`)
        client = await response.json()
        clients.value.push(client)
    }

    for (let review of reviews.value) {
        const dateObj = new Date(review.date);

        review.date = dateObj.toLocaleDateString('fr-FR', {
            day: 'numeric',
            month: 'long',
            year: 'numeric',
            timeZone: 'Europe/Brussels' // Adjust the time zone as per your requirement
        });
    }

    isLoaded.value = true
})
</script>

<template>


    <div v-if="!isLoaded" class="text-center">
        <div class="spinner-border" role="status"></div>
    </div>
    <div v-else class="container-fluid p-5 row">
        <div v-for="(item, index) in reviews" class="col-lg-6">
            <h3>{{ clients[index].name }} {{ clients[index].lastname }}</h3>
            <p class="text-secondary">
                {{ item.date }}
                <i v-for="star of item.rating" class="bi bi-star-fill text-success"></i>
            </p>
            <p>{{ item.review }}</p>
        </div>
    </div>
</template>