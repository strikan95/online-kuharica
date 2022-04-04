<template>
  <div class="row row-cols-1 row-cols-md-3 g-4">
    <div v-for="(recipe, index) in recipes" :key="index">
      <div class="col">
        <div class="card" style="width: 18rem">
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/a/a3/Eq_it-na_pizza-margherita_sep2005_sml.jpg"
            class="card-img-top"
            alt="..."
          />
          <div class="card-body">
            <h5 class="card-title">{{ recipe.name }}</h5>
            <p class="card-text">{{ recipe.description }}</p>
          </div>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">An item</li>
            <li class="list-group-item">A second item</li>
            <li class="list-group-item">A third item</li>
          </ul>
          <div class="card-body">
            <a href="#" class="card-link">Card link</a>
            <a href="#" class="card-link">Another link</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      recipes: [],
    };
  },

  methods: {
    getRecipes() {
      const path = "http://localhost:5000/api/v1/recipes";
      axios
        .get(path)
        .then((res) => {
          this.recipes = res.data.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },

  created() {
    this.getRecipes();
  },
};
</script>
