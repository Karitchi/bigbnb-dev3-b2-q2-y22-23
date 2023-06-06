<template>
  <div class="form-row">
    <div class="form-group col-md-3">
      <label for="add-hotel-add-image">Ajouter une/des images</label>
      <input
          id="add-hotel-add-image"
          type="file"
          accept="image/png, image/jpeg"
          class="form-control"
          ref="image"
          @change="this.onInput"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'AddImage',
  emits: ['input'],

  data() {
    return {
      image: null
    }
  },

  methods: {
    onInput() {
      this.image = this.$refs.image.files[0];
      this.$emit('input', {'image': this.image, 'isValid': true});
    }
  }
}
</script>

<style scoped>

</style>