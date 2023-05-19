import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/variables.scss'
import VueJwtDecode from 'vue-jwt-decode'

const app = createApp(App);
app.use(router).mount('#app')
app.config.globalProperties.$api = 'http://localhost:8000/'

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
        }
    }
})
