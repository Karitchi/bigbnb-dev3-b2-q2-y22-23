<script setup lang="ts">
defineProps([
    "name",
    "hotel_owner",
    "image",
    "description",
    "city",
    "rooms",
    "price",
])

</script>

<template>
    <div class="container-fluid p-5">
        <div class="container-fluid">
            <h1>{{ name }}</h1>
            <hr class="hr" />

            <div class="row">
                <div class="col">


                    <div class="row">
                        <div class="col">
                            <div class="card bg-light">
                                <div class="card-body">
                                    <div class="card-title">
                                        <h5>Hotelier: {{ hotel_owner }}</h5>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="col">
                            <div class="card bg-light">
                                <div class="card-body">
                                    <div class="card-title">
                                        <h5>Dans la ville de {{ city }}</h5>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="col">
                            <div class="card bg-light">
                                <div class="card-body">
                                    <div class="card-title">
                                        <h5>Il reste {{ rooms }} chambre</h5>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <hr class="hr" />
                    <div class="row">
                        <div class="col">
                            <div class="card bg-light">
                                <div class="card-body">
                                    <div class="card-title">
                                        <h5> {{ description }}</h5>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card bg-light">
                        <div class="card-body">
                            <div class="card-title">
                                <h5> {{ price }}</h5>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- <h1>{{ price }}</h1>
            <h1>{{ image }}</h1> -->
    </div>
</template>