<template>
  <form @submit="this.onSubmit" style="padding: 10px">
    <hotel-name @input="this.setName" />
    <hotel-description @input="this.setDescription" />
    <city @input="this.setCity" />
    <room-quantity @input="this.setRooms" />
    <price @input="this.setPrice" />
    <mail-input @input="this.setMail" />
    <phone-number @input="this.setPhoneNumber" />
    <button
        type="submit"
        class="btn btn-primary"
        :disabled="!this.isFormValid"
    >Ajouter l'hôtel</button>
  </form>
</template>


<script>
import HotelName from "@/components/AddHotel/HotelName.vue";
import HotelDescription from "@/components/AddHotel/HotelDescription.vue";
import City from "@/components/AddHotel/City.vue";
import RoomQuantity from "@/components/AddHotel/RoomQuantity.vue";
import Price from "@/components/AddHotel/Price.vue";
import MailInput from "@/components/Register/MailInput.vue";
import PhoneNumber from "@/components/AddHotel/PhoneNumber.vue";
import axios from "axios";

export default {
  name: "AddHotel",
  components: {PhoneNumber, MailInput, Price, RoomQuantity, City, HotelDescription, HotelName},

  data() {
    return {
      name: '',
      isNameValid: false,
      description: '',
      isDescriptionValid: false,
      city: null,
      isCityValid: false,
      rooms: null,
      isRoomsValid: false,
      price: null,
      isPriceValid: false,
      mail: '',
      isMailValid: false,
      phoneNumber: '',
      isPhoneNumberValid: false,
      isFormValid: false
    }
  },

  methods: {
    onSubmit(e) {
      if (!this.isFormValid)
        return;

      axios.post(`${this.$api}hotels/`, {
        'hotel_owner': this.getID(),
        'name': this.name,
        'description': this.description,
        'city': this.city,
        'rooms': this.rooms,
        'price': this.price,
        'mail': this.mail,
        'phone_number': this.phoneNumber
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
          .then(response => this.onSuccess());
      e.preventDefault();
    },

    setName(data) {
      this.name = data['name'];
      this.isNameValid = data['isValid'];
      this.setFormValid();
    },

    setDescription(data) {
      this.description = data['description'];
      this.isDescriptionValid = data['isValid'];
      this.setFormValid();
    },

    setCity(data) {
      this.city = data['city'];
      this.isCityValid = data['isValid'];
      this.setFormValid();
    },

    setRooms(data) {
      this.rooms = data['rooms'];
      this.isRoomsValid = data['isValid'];
      this.setFormValid();
    },

    setPrice(data) {
      this.price = data['price'];
      this.isPriceValid = data['isValid'];
      this.setFormValid();
    },

    setMail(data) {
      this.mail = data['mail'];
      this.isMailValid = data['isValid'];
      this.setFormValid();
    },

    setPhoneNumber(data) {
      this.phoneNumber = data['phoneNumber'];
      this.isPhoneNumberValid = data['isValid'];
      this.setFormValid();
    },

    setFormValid() {
      this.isFormValid = this.isNameValid && this.isDescriptionValid && this.isCityValid && this.isRoomsValid && this.isPriceValid
          && this.isMailValid && this.isPhoneNumberValid;
    },

    onSuccess() {
      this.$router.push('/my_hotels');
      alert('Votre hôtel a été ajouté avec succès !')
    },
  },

  beforeMount() {
    if (!this.isConnected() || this.getUserType() !== this.$hotelOwnerUserType)
      this.$router.push('/');
  }
}
</script>

<style scoped>

</style>