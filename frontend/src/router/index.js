import Vue from "vue";
import VueRouter from "vue-router";
//import SingleRecipe from "../components/SingleRecipe";
import RecipeList from "../components/RecipeList";

Vue.use(VueRouter);

const routes = [
  {
    path: "/recipes",
    name: "RecipeList",
    component: RecipeList,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
