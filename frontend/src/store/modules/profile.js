import ApiService from "@/common/services/api";

import { FETCH_PROFILE } from "@/common/types/actions";

import { SET_PROFILE } from "@/common/types/mutations";

const state = {
  errors: {},
  profile: {},
};

const getters = {
  profile(state) {
    return state.profile;
  },
};

const actions = {
  async [FETCH_PROFILE]({ commit }, payload) {
    const username = payload;
    const response = await ApiService.get("users", username)
      .then(({ data }) => {
        commit(SET_PROFILE, data);
        return data;
      })
      .catch((error) => {
        return Promise.reject(error);
      });
    return response;
  },
};

const mutations = {
  [SET_PROFILE](state, profile) {
    state.profile = profile;
    state.errors = {};
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
