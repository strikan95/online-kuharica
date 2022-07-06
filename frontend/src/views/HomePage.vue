<template>
  <div class="container">
    <RecipeList></RecipeList>
  </div>
</template>

<script>
import { FETCH_RECIPES } from "@/common/types/actions";
import RecipeList from "@/components/RecipeList.vue";
export default {
  name: "HomPageView",
  components: {
    RecipeList,
  },
};
</script>

<style></style>
