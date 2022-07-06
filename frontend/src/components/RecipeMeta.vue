<template>
  <div>
    <h1>Recipe Meta</h1>
    <recipe-actions-element
      v-if="actions"
      :recipe="recipe"
      :canModify="isCurrentUser()"
    ></recipe-actions-element>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import RecipeActionsElement from "@/components/RecipeActions";
export default {
  name: "RecipeMetaElement",
  components: {
    RecipeActionsElement,
  },
  props: {
    recipe: {
      type: Object,
      required: true,
    },
    actions: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  computed: {
    ...mapGetters(["currentUser", "isAuthenticated"]),
  },
  methods: {
    isCurrentUser() {
      console.log("is current user");
      if (this.currentUser.id && this.recipe.user_id) {
        return this.currentUser.id === this.recipe.user_id;
      }
      return false;
    },
  },
};
</script>

<style></style>
