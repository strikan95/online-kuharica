<template>
  <div
    class="container square-box d-flex justify-content-center align-items-center text-center"
  >
    <form>
      <h3 class="h3 mb-3 fw-normal">Register</h3>

      <div class="form-floating">
        <input
          type="username"
          class="form-control"
          id="floatingUsername"
          placeholder="username"
          autocomplete="off"
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
export default {
  name: "registerPageView",
};
</script>

<style></style>
