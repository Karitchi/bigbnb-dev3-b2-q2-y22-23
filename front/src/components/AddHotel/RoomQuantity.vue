<template>
  <div class="form-row">
    <div class="form-group col-md-2">
      <label for="add-hotel-room-quantity">Nombre de chambres</label>
      <input
          id="add-hotel-room-quantity"
          type="number"
          class="form-control"
          :class="this.rooms !== null ? (this.isValid ? 'is-valid' : 'is-invalid') : ''"
          v-model="this.rooms"
          @input="this.onInput"
          min="1"
          :max="this.MAX_ROOMS"
          placeholder="10"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'RoomQuantity',
  emits: ['input'],

  data() {
    return {
      rooms: null,
      isValid: false,
      MAX_ROOMS: 10000
    }
  },

  methods: {
    onInput() {
      this.isValid = this.rooms !== null && this.rooms > 0 && this.rooms <= this.MAX_ROOMS;
      this.$emit('input', {'rooms': this.rooms, 'isValid': this.isValid});
    }
  }
}
</script>