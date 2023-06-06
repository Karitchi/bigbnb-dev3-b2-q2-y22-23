import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/register.css'
import VueJwtDecode from 'vue-jwt-decode'


const app = createApp(App);
app.use(router).mount('#app');
app.config.globalProperties.$api = 'http://localhost:8000/';
app.config.globalProperties.$hotelOwnerUserType = 'hotel_owner';
app.config.globalProperties.$clientUserType = 'client';


export function isConnected(): boolean {
    return localStorage.getItem('access') !== null;
}

export function getID() {
    if (!isConnected())
        throw 'Not Connected'
    return Number(localStorage.getItem('id'));
}

app.mixin({
    methods: {
        storeToken(data: {'access': string, 'refresh': string}) {
            localStorage.setItem('access', data['access']);
            localStorage.setItem('refresh', data['refresh']);
            let jwt = VueJwtDecode.decode(data['access']);
            localStorage.setItem('id', jwt['id']);
            localStorage.setItem('type', jwt['type']);
        },

        forceRedirectionIfConnected(): void {
            if (this.isConnected()) {
                this.$router.push('/');
            }
        },

        isConnected(): boolean {
            return localStorage.getItem('access') !== null;
        },

        disconnect(): void {
            localStorage.clear();
        },

        getAuthenticatedRequestBody(): {'headers': {'Content-type': 'application/json', 'Authorization': string}} {
            if (!this.isConnected())
                throw "Not connected"
            return {
                'headers': {
                    "Content-type": "application/json",
                    'Authorization': String(localStorage.getItem('access'))
                }
            }
        },

        getID() {
          if (!this.isConnected())
              throw 'Not Connected'
            return Number(localStorage.getItem('id'));
        },

        getUserType(): string | null {
            if (!this.isConnected())
                return null;

            return localStorage.getItem('type');
        },

        isHotelOwnerOf(hotelOwnerID: number): boolean {
            if (!this.isConnected())
                return false;
            if (this.getUserType() !== this.$hotelOwnerUserType)
                return false;
            return this.getID() === hotelOwnerID;
        }
    }
})
