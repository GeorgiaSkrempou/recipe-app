import { createStore } from 'vuex';
import user from './modules/user';
import recipe from './modules/recipe';
import global from './modules/global';

export const store = createStore({
  modules: {
    user,
    recipe,
    global,
  },
});
