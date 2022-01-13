import 'element-plus/dist/index.css';

import { createApp } from 'vue';
import App from './App.vue';
import { http } from './providers/http';

import { store } from './store';
import { router } from './router';

import './assets/scss/app.scss';
import { ElLoading } from 'element-plus';

http.mount();

const app = createApp(App);

app.use(store);
app.use(router);

app.use(ElLoading);

app.mount('#app');
