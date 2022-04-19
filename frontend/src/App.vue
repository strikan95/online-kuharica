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
export default {
  name: "app",
  components: {
    NavBar,
  },
};
</script>

<style></style>
