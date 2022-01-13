import { http } from '@/providers/http';
import axios from 'axios';

const defaultUserState = () => {
  return {
    user: {},
    userLoaded: false,
  };
};

const state = defaultUserState();

const getters = {
  user: (state) => state.user,
  userLoaded: (state) => state.userLoaded,
};

const mutations = {
  setUser: (state, payload) => {
    state.user = payload;
  },
  setUserLoaded: (state, payload) => {
    state.userLoaded = payload;
  },
};

const actions = {
  login: ({ dispatch }, user) => {
    return new Promise((resolve, reject) => {
      axios({
        url: '/api/login',
        method: 'POST',
        data: { ...user },
      })
        .then((response) => {
          localStorage.setItem('token', response.data.access_token);
          http.mount();

          resolve(response);
        })
        .catch(error => reject(error.response));
    });
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
