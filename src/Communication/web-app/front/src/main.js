import {createApp} from 'vue';
import './style.css';
import {library} from '@fortawesome/fontawesome-svg-core';
import {faChevronLeft, faChevronRight, fas} from '@fortawesome/free-solid-svg-icons';
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome';
import Datepicker from '@vuepic/vue-datepicker';
import {createVuetify} from 'vuetify'
import '@mdi/font/css/materialdesignicons.css';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import App from './App.vue';
import store from './store';
import router from './routes/index';
import '@vuepic/vue-datepicker/dist/main.css';
// Vuetify
import 'vuetify/styles';

library.add(faChevronLeft, faChevronRight)

const vuetify = createVuetify({
    components,
    directives,
});
library.add(fas);

const app = createApp(App);
app.use(vuetify);
app.use(store);
app.use(router);
app.component('FontAwesomeIcon', FontAwesomeIcon);
app.component('Datepicker', Datepicker);
app.mount('#app');
