import axios from 'axios';

const defaultRecipeState = () => {
  return {
    recipes: [],
    ownRecipes: [],
    recipe: [],
    recipeLoaded: false,
    ownRecipesLoaded: false,
  };
};

const state = defaultRecipeState();

const getters = {
  recipes: (state) => state.recipes,
  ownRecipes: (state) => state.ownRecipes,
  recipe: (state) => state.recipe,
  recipeLoaded: (state) => state.recipeLoaded,
  recipesLoaded: (state) => state.recipesLoaded,
  ownRecipesLoaded: (state) => state.ownRecipesLoaded,
};

const mutations = {
  setRecipes: (state, payload) => {
    state.recipes = payload;
  },
  setOwnRecipes: (state, payload) => {
    state.ownRecipes = payload;
  },
  setRecipe: (state, payload) => {
    state.recipe = payload;
    state.recipeLoaded = true;
  },
  setRecipesLoaded: (state, payload) => {
    state.recipesLoaded = payload;
  },
  setOwnRecipesLoaded: (state, payload) => {
    state.ownRecipesLoaded = payload;
  },
  resetRecipeStore: (state) => {
    Object.assign(state, defaultRecipeState());
  },
};

const actions = {
  getAll: ({ commit }) => {
    return new Promise((resolve, reject) => {
      axios({
        url: `/api/recipes`,
        method: 'GET',
      })
        .then((response) => {
          commit('setRecipes', response.data);
          commit('setRecipesLoaded', true);

          resolve(response);
        })
        .catch(error => reject(error.response.data));
    });
  },
  getOwn: ({ commit }) => {
    return new Promise((resolve, reject) => {
      axios({
        url: `/api/user/recipes`,
        method: 'GET',
      })
        .then((response) => {
          commit('setOwnRecipes', response.data);
          commit('setOwnRecipesLoaded', true);

          resolve(response);
        })
        .catch(error => reject(error.response.data));
    });
  },
  addToAccount: ({ commit }, { recipe }) => {
    return new Promise((resolve, reject) => {
      axios({
        url: `/api/user/recipes/${recipe}`,
        method: 'POST',
      })
        .then((response) => {
          resolve(response);
        })
        .catch(error => reject(error.response.data));
    });
  },
  getRecipe: ({ commit }, { recipe }) => {
    return new Promise((resolve, reject) => {
      axios({
        url: `/api/user/recipes/${recipe}`,
        method: 'POST',
      })
        .then((response) => {
          resolve(response);
        })
        .catch(error => reject(error.response.data));
    });
  },
  add: ({ commit }, recipe) => {
    return new Promise((resolve, reject) => {
      axios({
        url: `/api/recipes`,
        method: 'POST',
        data: { ...recipe },
      })
        .then((response) => {
          resolve(response);
        })
        .catch(error => reject(error.response.data));
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