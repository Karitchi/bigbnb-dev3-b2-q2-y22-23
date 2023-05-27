<script setup>
defineProps({
    urls: Array
})
</script>

<template>
        <div class="row ">

            <!-- first image -->
            <div class="col p-1 big-col">
                <img :src="urls[0]" class="img-fluid rounded big" alt="">
            </div>

            <!-- other images -->
            <div class="col p-0">
                <div class="row row-cols-2 m-0">
                    <div v-for="(url, index) in urls.slice(1)" :key="index" class="col p-1 little-col">
                        <img :src="url" class="img-fluid rounded little" alt="">
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