<script setup lang="ts">
import Images from '@/components/Hotel/Images.vue';
import Informations from '@/components/Hotel/Informations.vue';
import ReviewForm from '@/components/Hotel/ReviewForm.vue'
import ReviewsList from '@/components/Hotel/ReviewsList.vue'
import BackButton from '@/components/Hotel/BackButton.vue'

</script>

<template>
    <div class="container ps-5 pe-5">
        <BackButton />
        <Images />
        <Informations />
        <ReviewForm />
        <ReviewsList />
    </div>
</template>


<style scoped></style>


