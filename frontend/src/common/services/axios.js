import axios from "axios";
import store from "@/store";
import router from "@/router";

import { PURGE_AUTH } from "../types/mutations";

const API_URL = "http://localhost:5000/api/v1/";

const instance = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 3000,
  withCredentials: true,
  xsrfCookieName: "csrf_access_token",
});

instance.interceptors.response.use(
  function (response) {
    return response;
  },

  async function (error) {
    if (typeof error.response === "undefined") {
      return Promise.reject(error);
    }

    if (error.response.status !== 401) {
      return Promise.reject(error);
    }

    const originalRequest = error.config;
    console.debug("Server responded 401 when accessing: ", originalRequest.url);

    if (originalRequest.url.includes("/user/refresh")) {
      console.log("Failed to refresh token");
      router.push("/login");
      return Promise.reject(error);
    }

    console.log("Trying to refresh tokens");
    await instance.post("/user/refresh").catch((error) => {
      console.log("Need to authenticated");
      store.commit(PURGE_AUTH);
      return Promise.reject(error);
    });

    console.log("Replaying original request to: " + originalRequest.url);
    return await instance(originalRequest).catch((error) => {
      console.log("replaying request to: " + originalRequest.url + " failed");
      return Promise.reject(error);
    });
  }
);

export default instance;
