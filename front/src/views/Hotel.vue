<script setup lang="ts">
import Images from '@/components/Hotel/Images.vue';
import Informations from '@/components/Hotel/Informations.vue';
import ReviewForm from '@/components/Hotel/ReviewForm.vue'
import ReviewsList from '@/components/Hotel/ReviewsList.vue'
import BackButton from '@/components/Hotel/BackButton.vue'
import Booking from '@/components/Hotel/Booking.vue'

</script>

<template>
    <div class="container ps-sm-5 pe-sm-5">
        <BackButton class="mt-3 mb-3" />
        <Images class="mb-5  rounded border shadow" />
        <div class="row m-0 p-1 d-none d-lg-flex">
            <Informations class="col me-2 pb-3 pt-3 shadow border rounded" style="width: 60%;"/>
            <Booking class="col ms-2 pb-3 pt-3 shadow border rounded h-100 position-sticky" style="top: 2rem;" />
        </div>

        <div class="m-0 p-1 d-lg-none">
            <Informations class="mb-4 p-3 shadow border rounded" />
            <Booking class="mt-2 p-3 shadow border rounded" />
        </div>
        
        <ReviewForm class="pb-5 pt-5" />
        <ReviewsList />
    </div>
</template>

<style scoped></style>


