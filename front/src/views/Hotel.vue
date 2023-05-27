<script setup lang="ts">
import Images from '@/components/Hotel/Images.vue';
import Informations from '@/components/Hotel/Informations.vue';
import ReviewForm from '@/components/Hotel/ReviewForm.vue'
import ReviewsList from '@/components/Hotel/ReviewsList.vue'
import BackButton from '@/components/Hotel/BackButton.vue'
import Booking from '@/components/Hotel/Booking.vue'

</script>

<template>
    <div class="container ps-5 pe-5">
        <BackButton />
        <Images />
        <div class="row row-cols-1 row-cols-md-2">
            <Informations class="col" />
            <Booking class="col" />
        </div>
        <ReviewForm />
        <ReviewsList />
    </div>
</template>


<style scoped></style>


