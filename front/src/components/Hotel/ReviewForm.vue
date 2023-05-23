<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute()

const review = ref('');
const rating = ref(null);
const showSuccessToast = ref(false);

let numberOfStars = 0


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

function submitForm(event) {
    event.preventDefault();

    axios.post(`http://localhost:8000/reviews/hotel/${route.params.id}/`, {
        client_id: 1,
        hotel_id: route.params.id,
        review: review.value,
        rating: numberOfStars,
    })
        .then(function (response) {
            showSuccessToast.value = true;
            review.value = ''
            numberOfStars = 0
            starsHovered.value = starsHovered.value.map(() => false);
        })
        .catch(function (error) {
            console.log(error);
        });

};
</script>



<template>
    <form class="container-fluid p-5" @submit="submitForm">
        <div class="mb-3">
            <i v-for="(isHovered, index) in starsHovered" :key="index" :class="{ 'bi': true, 'bi-star-fill': isHovered, 'bi-star': !isHovered, 'text-success': true }" @mouseenter="mouseenter(index, true)" @mouseleave="mouseleave" @click="click"></i>
        </div>

        <div class="mb-3">
            <label for="review" class="form-label"></label>
            <input type="text" class="form-control" v-model="review" id="review" rows="3" placeholder="Give us your opinion" required>

        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

