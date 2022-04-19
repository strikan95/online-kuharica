import Vue from "vue";
import Vuex from "vuex";
import Auth from "@/store/modules/auth";
import Profile from "@/store/modules/profile";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

// store = Vuex.Store({
//   modules: {
//     Auth,
//     Profile,
//   },
//   plugins: [createPersistedState()],
// });

export default new Vuex.Store({
  modules: {
    Auth,
    Profile,
  },
  plugins: [createPersistedState()],
});

// export default store;
