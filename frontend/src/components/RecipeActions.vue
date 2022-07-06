<template>
  <div>
    <h1>Recipe Actions</h1>
    <span v-if="canModify">
      <span>&nbsp;&nbsp;</span>
      <button class="btn btn-outline-danger btn-sm" @click="deleteRecipe">
        <i class="ion-trash-a"></i> <span>&nbsp;Delete Article</span>
      </button>
    </span>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { DELETE_RECIPE } from "@/common/types/actions";
export default {
  name: "RecipeActionsElement",
  props: {
    recipe: {
      type: Object,
      required: true,
    },
    canModify: {
      type: Boolean,
      required: true,
    },
  },
  computed: {
    ...mapGetters(["profile", "isAuthenticated"]),
  },
  methods: {
    async deleteRecipe() {
      try {
        await this.$store.dispatch(DELETE_RECIPE, this.recipe.id);
        this.$router.push("/");
      } catch (err) {
        console.error(err);
      }
    },
  },
};
</script>

<style></style>
