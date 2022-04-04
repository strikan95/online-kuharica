<template>
  <div>
    <p>{{ msg }}</p>
    <button type="button" class="btn btn-primary" />
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SingleRecipe",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    getResponse() {
      const path = "http://localhost:5000/api/v1/recipes";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.msg = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getResponse();
  },
};
</script>
