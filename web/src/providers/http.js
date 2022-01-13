import { router } from '@/router';
import { baseURL } from '../config/config';
import axios from 'axios';

const http = {
  authHandler: null,
  responseHandler: null,
  mount() {
    this.authHandler = axios.interceptors.request.use((config) => {
      const token = localStorage.getItem('token');

      if (token !== null) {
        config.headers.common['Authorization'] = `Bearer ${token}`;
      }
      config.baseURL = baseURL;

      return config;
    });

    this.responseHandler = axios.interceptors.response.use(r => r, (err) => {
      if (err.response && err.response.status === 401) {
        return Promise.reject(router.push({
          name: 'public.login',
          query: {
            redirect: router.currentRoute.fullPath,
          },
          params: {
            alert: {
              type: 'info',
              msg: 'Your session has expired. Please log in again.',
            },
          },
        }));
      }

      return Promise.reject(err);
    });
  },
  unmount() {
    axios.interceptors.request.eject(this.authHandler);
    axios.interceptors.response.eject(this.responseHandler);
  },
};

export {
  http,
};
