import Vue from "vue";
import VueRouter from "vue-router";
import HelloVue from "../components/HelloVue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/hellovue",
    name: "HelloVue",
    component: HelloVue,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
