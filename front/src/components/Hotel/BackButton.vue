<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();


function goBack() {
    router.back();
}

</script>

<template>
    <div>
        <button type="button" class="btn btn-primary" @click="goBack">Go Back</button>
    </div>
</template>