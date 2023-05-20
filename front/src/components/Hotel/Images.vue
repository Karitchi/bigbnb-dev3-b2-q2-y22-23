<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router';

const route = useRoute()

const urls = ref([])

const isLoaded = ref(false)
let firstImage

onMounted(async () => {
    let images = []
    let response

    response = await fetch(`http://127.0.0.1:8000/hotels/${route.params.id}/images`)
    images.value = await response.json()



    for (const image of images.value) {
        urls.value.push(`http://127.0.0.1:8000${image.url}`)
    }

    firstImage = urls.value[0]
    urls.value.shift()

    isLoaded.value = true
})
</script>

<template>
    <div v-if="!isLoaded" class="text-center">
        <div class="spinner-border" role="status"></div>
    </div>
    <div v-else class="container-fluid p-5">
        <div class="row p-1 bg-light  rounded border m-0 ">
            <div class="col p-1 big-col">
                <img :src="firstImage" class="img-fluid rounded big" alt="">
            </div>

            <div class="col p-0">
                <div class="row row-cols-2 m-0">
                    <div v-for="url in urls" class="col p-1 little-col">
                        <img :src="url" class="img-fluid rounded little" alt="">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.big-col {
    height: 30vw;
}

.little-col {
    height: 15vw;
}

.big {
    width: 100%;
    height: 100%;
    object-fit: cover
}

.little {
    width: 100%;
    height: 100%;
    object-fit: cover
}
</style>