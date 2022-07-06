import { FETCH_RECIPES } from "@/common/types/actions";
import { FETCH_START, FETCH_END } from "@/common/types/actions";
import { RecipesService } from "@/common/services/api";

const state = {
  recipes: [],
  isLoading: true,
  recipesCount: 0,
};

const getters = {
  recipesCount(state) {
    return state.recipesCount;
  },
  recipes(state) {
    return state.recipes;
  },
  isLoading(state) {
    return state.isLoading;
  },
};

const actions = {
  async [FETCH_RECIPES]({ commit }) {
    commit(FETCH_START);
    const response = await RecipesService.query()
      .then(({ data }) => {
        console.log(data);
        commit(FETCH_END, data);
        return data;
      })
      .catch((error) => {
        return Promise.reject(error);
      });
    return response;
  },
};

const mutations = {
  [FETCH_START](state) {
    state.isLoading = true;
  },
  [FETCH_END](state, { recipes, recipesCount }) {
    state.recipes = recipes;
    state.recipesCount = recipesCount;
    state.isLoading = false;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
