import { ElNotification } from 'element-plus';

const defaultGlobalState = () => {
  return {
    toast: {
      show: false,
      type: '',
      message: '',
    },
  };
};

const state = defaultGlobalState();

const getters = {
  toast: (state) => state.toast,
};

const mutations = {
  dispatchToast: (state, payload) => {
    ElNotification({
      type: payload.type,
      title: payload.title,
      message: payload.message,
      duration: 30000,
    });
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
};