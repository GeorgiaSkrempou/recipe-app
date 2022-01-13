import { createStore } from 'vuex';
import user from './modules/user';
import recipe from './modules/recipe';

export const store = createStore({
  modules: {
    user,
    recipe,
  },
});
