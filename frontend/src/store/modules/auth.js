import ApiService from "@/common/services/api";

import { LOGIN, LOGOUT, CHECK_AUTH } from "@/common/types/actions";

import { SET_AUTH, PURGE_AUTH, SET_ERROR } from "@/common/types/mutations";

const state = {
  errors: null,
  user: {},
  isAuthenticated: false,
};

const getters = {
  currentUser(state) {
    return state.user;
  },
  isAuthenticated(state) {
    return state.isAuthenticated;
  },
};

const actions = {
  [LOGIN]({ commit }, credentials) {
    return new Promise((resolve) => {
      ApiService.post("user/login", { user: credentials })
        .then(({ data }) => {
          commit(SET_AUTH, data.user);
          resolve(data);
        })
        .catch(({ response }) => {
          commit(SET_ERROR, response.data.errors);
        });
    });
  },
  [LOGOUT]({ commit }) {
    return new Promise((resolve) => {
      ApiService.post("user/logout").then(() => {
        commit(PURGE_AUTH);
      });
    });
  },
  [CHECK_AUTH]({ commit }) {
    commit(PURGE_AUTH);
    // if (state.isAuthenticated) {
    //   ApiService.get("user")
    //     .then(({ data }) => {
    //       commit("setAuth", data.user);
    //     })
    //     .catch(({ response }) => {
    //       commit("setError", response.data.errors);
    //     });
    // } else {
    //   commit("purgeAuth");
    // }
  },
};

const mutations = {
  [SET_ERROR](state, error) {
    state.errors = error;
  },
  [SET_AUTH](state, user) {
    state.isAuthenticated = true;
    state.user = user;
    state.errors = {};
  },
  [PURGE_AUTH](state) {
    state.isAuthenticated = false;
    state.user = {};
    state.errors = {};
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
