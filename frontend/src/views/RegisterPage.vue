<template>
  <div
    class="container square-box d-flex justify-content-center align-items-center text-center"
  >
    <form @submit.prevent="onSubmit(username, email, password)">
      <h3 class="h3 mb-3 fw-normal">Register</h3>

      <div class="form-floating">
        <input
          type="username"
          class="form-control"
          id="floatingUsername"
          placeholder="username"
          autocomplete="off"
          v-model="username"
        />
        <label for="floatingUsername">Username</label>
      </div>

      <div class="form-floating">
        <input
          type="email"
          class="form-control"
          id="floatingInput"
          placeholder="name@example.com"
          autocomplete="off"
          v-model="email"
        />
        <label for="floatingInput">Email address</label>
      </div>

      <div class="form-floating">
        <input
          type="password"
          class="form-control"
          id="floatingPassword"
          placeholder="Password"
          autocomplete="off"
          v-model="password"
        />
        <label for="floatingPassword">Password</label>
      </div>
      <button class="w-100 btn btn-lg btn-primary" type="submit">
        Register
      </button>
    </form>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { REGISTER } from "@/common/types/actions";
export default {
  name: "registerPageView",
  data() {
    return {
      username: "",
      email: "",
      password: "",
    };
  },
  computed: {
    ...mapState({
      errors: (state) => state.auth.errors,
    }),
  },
  methods: {
    onSubmit() {
      this.$store
        .dispatch(REGISTER, {
          username: this.username,
          email: this.email,
          password: this.password,
        })
        .then(() => {
          this.$router.push({ name: "login" });
        });
    },
  },
};
</script>

<style></style>
