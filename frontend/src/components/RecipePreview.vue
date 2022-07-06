<template>
  <div class="col">
    <div class="card h-100">
      <img
        src="https://podravkaiovariations.azureedge.net/80ec2a16-638e-11eb-b1a5-0242ac12002d/v/f2b1f6a6-64bc-11eb-b6c2-0242ac130010/1600x1200-f2b21938-64bc-11eb-9498-0242ac130010.webp"
        class="card-img-top"
      />
      <div class="card-body">
        <router-link :to="recipeLink" class="preview-link">
          <h5 v-text="recipe.name" class="card-title" />
          <p v-text="recipe.description" class="card-text" />
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ArticlePreviewElement",
  props: {
    recipe: { type: Object, required: true },
  },
  computed: {
    recipeLink() {
      return {
        name: "recipe",
        params: {
          slug: this.recipe.id,
        },
      };
    },
  },
};
</script>

<style></style>
