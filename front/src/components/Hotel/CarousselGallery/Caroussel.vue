<script setup>
defineProps({
    urls: Array
})
</script>

<template>
    <!-- caroussel -->
    <div id="carouselExampleIndicators" class="carousel slide">
        <div class="carousel-inner">

            <!-- images -->
            <div v-for="(url, index) in urls" :class="{ 'carousel-item': true, 'active': index === 0 }">
                <img :src="url" class="d-block w-100" alt="">
            </div>

            <!-- indicators -->
            <div class="carousel-indicators">
                <button v-for="(url, index) in urls" type="button" data-bs-target="#carouselExampleIndicators" :data-bs-slide-to="index" :aria-label="'Slide ' + (index + 1)" :class="{ 'active': index === 0 }" :aria-current="index === 0"></button>
            </div>
        </div>

        <!-- previous button -->
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>

        <!-- next button -->
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>

    </div>
</template>