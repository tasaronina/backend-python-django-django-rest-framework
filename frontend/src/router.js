import { createRouter, createWebHistory } from "vue-router";

import NewsCreateView from "./views/NewsCreateView.vue";
import NewsImageAttachView from "./views/NewsImageAttachView.vue";
import NewsMaterialCreateView from "./views/NewsMaterialCreateView.vue";

const routes = [
  {
    path: "/",
    redirect: "/news-materials/create"
  },
  {
    path: "/news-materials/create",
    component: NewsMaterialCreateView
  },
  {
    path: "/news/create",
    component: NewsCreateView
  },
  {
    path: "/news-images/attach",
    component: NewsImageAttachView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
