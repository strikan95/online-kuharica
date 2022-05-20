<template>
  <div class="user-profile">
    <h1>Profile Page</h1>
    <p>Hello, {{ username }}.</p>
    <p v-if="email">Your email is: {{ email }}</p>
  </div>
</template>

<script>
import { FETCH_PROFILE } from "@/common/types/actions";

export default {
  name: "profilePageView",
  data() {
    return {
      username: "",
      email: "",
    };
  },
  methods: {
    fetchUserProfileData() {
      this.$store
        .dispatch(FETCH_PROFILE, this.$route.params.username)
        .then((response) => {
          this.username = response.username;
          this.email = response.email;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.fetchUserProfileData();
  },
  created() {
    this.$watch(
      () => this.$route.params,
      (to, from) => {
        this.fetchUserProfileData();
      }
    );
  },
};
</script>

<style></style>
