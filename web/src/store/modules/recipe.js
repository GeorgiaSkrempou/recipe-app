import axios from 'axios';

const defaultRecipeState = () => {
  return {
    recipes: [],
    recipe: [],
    recipeLoaded: false,
    recipesLoaded: false,
  };
};

const state = defaultRecipeState();

const getters = {
  recipes: (state) => state.recipes,
  recipe: (state) => state.recipe,
  recipeLoaded: (state) => state.recipeLoaded,
  recipesLoaded: (state) => state.recipesLoaded,
};

const mutations = {
  setRecipes: (state, payload) => {
    state.recipes = payload;
  },
  setRecipe: (state, payload) => {
    state.recipe = payload;
    state.recipeLoaded = true;
  },
  setRecipesLoaded: (state, payload) => {
    state.recipesLoaded = payload;
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
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};