<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router';

import Gallery from './CarousselGallery/Gallery.vue'
import Caroussel from './CarousselGallery/Caroussel.vue'


const route = useRoute()

const urls = ref([])
const isLoaded = ref(false)

onMounted(async () => {
    let imageTable = []
    let response

    // fetch the image table of the current hotel
    response = await fetch(`http://127.0.0.1:8000/hotels/${route.params.id}/images`)
    imageTable.value = await response.json()

    // push all images urls inside into urls array 
    for (const image of imageTable.value) {
        urls.value.push(`http://127.0.0.1:8000${image.url}`)
    }

    isLoaded.value = true
})
</script>


<template>
    <div v-if="!isLoaded" class="text-center">
        <div class="spinner-border" role="status"></div>
    </div>

    <div v-else>
        <Gallery class="d-none d-lg-flex p-1 m-0" :urls="urls" />
        <Caroussel class="d-lg-none" :urls="urls" />
    </div>
</template>