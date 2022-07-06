import instance from "./axios";

const ApiService = {
  query(resource, params) {
    return instance.get(resource, params).catch((error) => {
      return Promise.reject(`[ApiService] ${error}`);
    });
  },

  get(resource, slug = "") {
    return instance.get(`${resource}/${slug}`).catch((error) => {
      return Promise.reject(`[ApiService] ${error}`);
    });
  },

  post(resource, params) {
    return instance.post(`${resource}`, params);
  },

  update(resource, slug, params) {
    return instance.put(`${resource}/${slug}`, params);
  },

  put(resource, params) {
    return instance.put(`${resource}`, params);
  },

  delete(resource) {
    return instance.delete(resource).catch((error) => {
      return Promise.reject(`[ApiService] ${error}`);
    });
  },
};

export default ApiService;

export const RecipesService = {
  query() {
    console.log("Fetching all articles");
    return ApiService.get("recipes");
  },
  get(slug) {
    return ApiService.get("recipes", slug);
  },
  create(params) {
    return ApiService.post("recipes", { recipes: params });
  },
  update(slug, params) {
    return ApiService.update("recipes", slug, { recipes: params });
  },
  destroy(slug) {
    return ApiService.delete(`recipes/${slug}`);
  },
};
