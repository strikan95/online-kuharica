<template>
  <div id="app">
    <div class="container">
      <NavBar></NavBar>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavigationBar.vue";
import { CHECK_AUTH } from "@/common/types/actions";

export default {
  name: "app",
  components: {
    NavBar,
  },
  methods: {
    checkAuth() {
      this.$store.dispatch(CHECK_AUTH);
    },
  },
  mounted() {
    this.checkAuth();
  },
};
</script>

<style></style>
