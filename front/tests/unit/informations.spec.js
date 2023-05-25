import { mount } from '@vue/test-utils';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

jest.mock('vue-router', () => ({
    useRoute: jest.fn()
}));

describe('HotelDetails', () => {
    it('fetches and displays hotel details on mount', async () => {
        // Mock the route params
        const routeParams = {
            value: { params: { id: '123' } }
        };
        (useRoute as jest.Mock).mockReturnValue(routeParams);

        // Mock the response data
        const hotelData = {
            name: 'Sample Hotel',
            rooms: 5,
            city: 'city123',
            price: 100,
            description: 'Sample hotel description',
            hotel_owner: 'owner123'
        };
        const cityData = {
            name: 'Sample City',
            country: 'Sample Country'
        };
        const ownerData = {
            name: 'John',
            lastname: 'Doe',
            company: 'Sample Company',
            mail: 'john.doe@example.com'
        };
        global.fetch = jest.fn().mockImplementation((url) => {
            if (url.includes(`/hotels/${routeParams.value.params.id}`)) {
                return Promise.resolve({
                    json: () => Promise.resolve(hotelData)
                });
            } else if (url.includes(`/cities/${hotelData.city}`)) {
                return Promise.resolve({
                    json: () => Promise.resolve(cityData)
                });
            } else if (url.includes(`/hotel_owners/${hotelData.hotel_owner}`)) {
                return Promise.resolve({
                    json: () => Promise.resolve(ownerData)
                });
            }
        });

        const wrapper = mount({
            setup() {
                const route = useRoute();
                const hotel = ref(null);
                const city = ref(null);
                const hotel_owner = ref(null);
                const isLoaded = ref(false);

                onMounted(async () => {
                    let response;

                    response = await fetch(`http://127.0.0.1:8000/hotels/${route.value.params.id}`);
                    hotel.value = await response.json();

                    response = await fetch(`http://127.0.0.1:8000/cities/${hotel.value.city}`);
                    city.value = await response.json();

                    response = await fetch(`http://127.0.0.1:8000/hotel_owners/${hotel.value.hotel_owner}`);
                    hotel_owner.value = await response.json();

                    isLoaded.value = true;
                });

                return { hotel, city, hotel_owner, isLoaded };
            },
            template: `
        <div>
          <div v-if="!isLoaded" class="text-center">
            <div class="spinner-border
