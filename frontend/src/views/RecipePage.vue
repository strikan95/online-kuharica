<template>
  <div class="recipe-container">
    <RecipeMetaElement :recipe="recipe" :actions="true" />
    <h1 v-text="recipe.name" />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import store from "@/store";
import { FETCH_RECIPE } from "@/common/types/actions";
import RecipeMetaElement from "@/components/RecipeMeta";
export default {
  name: "recipePage",
  components: {
    RecipeMetaElement,
  },
  props: {
    slug: {
      type: Number,
      required: true,
    },
  },
  beforeRouteEnter(to, from, next) {
    Promise.all([store.dispatch(FETCH_RECIPE, to.params.slug)]).then(() => {
      next();
    });
  },
  computed: {
    ...mapGetters(["recipe", "currentUser", "isAuthenticated"]),
  },
};
</script>

<style></style>
