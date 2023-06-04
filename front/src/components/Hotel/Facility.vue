<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'

const route = useRoute()
const facilities = ref([])
const isLoaded = ref(false)

onMounted(async () => {

    await axios.get(`http://127.0.0.1:8000/facilities/${route.params.id}/`)
        .then(response => facilities.value = response.data);

    isLoaded.value = true
})
</script>

<template>
    <div v-if="!isLoaded" class="text-center">
        <div class="spinner-border" role="status"></div>
    </div>

    <div v-else>
        <div class="row flex-nowrap overflow-auto">
            <div v-for="facility in facilities" class="card mx-3 col-md-4 overflow-auto" style="width: 18rem; height: 8rem;">
                <div class="card-body">
                    <h5 class="card-title">{{ facility.name }}</h5>
                    <p class="card-text">{{ facility.description }}</p>
                </div>
            </div>
        </div>
    </div>
</template>