import { createApp } from 'vue';
import './style.css';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import Datepicker from '@vuepic/vue-datepicker';
import App from './App.vue';
import store from './store';
import router from './routes/index';
import '@vuepic/vue-datepicker/dist/main.css';

library.add(fas);

const app = createApp(App);
app.use(store);
app.use(router);
app.component('FontAwesomeIcon', FontAwesomeIcon);
app.component('Datepicker', Datepicker);
app.mount('#app');
