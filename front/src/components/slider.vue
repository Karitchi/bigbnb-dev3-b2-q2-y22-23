<template>
  <div @mousemove="doDrag" class="outercontainer">
    <div class="slider-container">
      <input type="text" v-model="min" @keyup="setMin" />
      <input type="text" v-model="max" @keyup="setMax" />
      <p>{{ numberLeft }}</p>
      <p>{{ numberRight }}</p>
    </div>
  </div>
</template>
