<template>
  <div>
    <h3>All Recipes</h3>
    <div v-if="isLoading" class="article-preview">Loading articles...</div>
    <div v-else>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <RecipePreviewElement
          v-for="(recipe, index) in recipes"
          :recipe="recipe"
          :key="recipe.name + index"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import RecipePreviewElement from "./RecipePreview.vue";
import { FETCH_RECIPES } from "@/common/types/actions";
export default {
  name: "RecipeListElement",
  components: {
    RecipePreviewElement,
  },
  computed: {
    ...mapGetters(["recipesCount", "recipes", "isLoading"]),
  },
  mounted() {
    this.fetchRecipes();
  },
  methods: {
    fetchRecipes() {
      this.$store.dispatch(FETCH_RECIPES);
    },
  },
};
</script>

<style></style>
