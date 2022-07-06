<template>
  <div class="container-md">
    <form @submit.prevent="onSubmit(name, description)">
      <h3 class="h3 mb-3 fw-normal">Add New Recipe</h3>

      <div class="form-floating">
        <textarea
          class="form-control"
          placeholder="Name"
          id="floatingTextarea"
          v-model="name"
        ></textarea>
        <label for="floatingTextarea">Recipe Name</label>
      </div>

      <div class="form-floating">
        <textarea
          class="form-control"
          placeholder="Description"
          id="floatingTextarea2"
          style="height: 100px"
          v-model="description"
        ></textarea>
        <label for="floatingTextarea2">Recipe Description</label>
      </div>

      <button class="w-100 btn btn-lg btn-primary" type="submit">
        Save Recipe
      </button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";
import { POST_RECIPE } from "@/common/types/actions";

export default {
  name: "newRecipePageView",
  data() {
    return {
      name: null,
      description: null,
    };
  },
  methods: {
    onSubmit(name, description) {
      this.$store
        .dispatch(POST_RECIPE, { name, description })
        .then(() => this.$router.push({ name: "home" }));
    },
  },
  computed: {
    ...mapState({
      errors: (state) => state.auth.errors,
    }),
  },
};
</script>

<style></style>
