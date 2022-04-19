import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ApiService from "@/common/services/api";
import "bootstrap/dist/css/bootstrap.css";

Vue.config.productionTip = false;

//Handle Unauthorized Access
//TODO
// router.beforeEach((to, from, next) =>
//   Promise.all([store.dispatch("checkAuth")]).then(next)
// );

// router.beforeEach((to, from, next) => {
//   const isAuthenticated = store.getters["isAuthenticated"];
//   if (!isAuthenticated) {
//     if (to.path !== "/login") {
//       next("login");
//     } else {
//       next();
//     }
//   } else {
//     next();
//   }
// });

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
