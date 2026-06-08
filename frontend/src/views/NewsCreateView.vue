<template>
  <section class="page">
    <div class="page-header">
      <h2>Создание новости</h2>
      <div v-if="successMessage" class="message success">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="message error">
        {{ errorMessage }}
      </div>
    </div>

    <form class="form" @submit.prevent="saveNews">
      <div class="grid-two">
        <div class="field full">
          <label for="news_material_id">Новостной материал</label>
          <select id="news_material_id" v-model="form.news_material_id">
            <option value="">Выберите новостной материал</option>
            <option
              v-for="material in newsMaterials"
              :key="material.id"
              :value="material.id"
            >
              {{ material.event_description }}
            </option>
          </select>
        </div>

        <div class="field full">
          <label for="title">Заголовок</label>
          <input id="title" v-model="form.title" type="text" />
        </div>

        <div class="field full">
          <label for="text">Текст</label>
          <textarea id="text" v-model="form.text"></textarea>
        </div>

        <div class="field">
          <label for="author">Автор</label>
          <input id="author" v-model="form.author" type="text" />
        </div>

        <div class="field">
          <label for="tag">Тег</label>
          <input id="tag" v-model="form.tag" type="text" />
        </div>

        <div class="field">
          <label for="category">Категория</label>
          <input id="category" v-model="form.category" type="text" />
        </div>

        <div class="field">
          <label for="territory">Территория</label>
          <input id="territory" v-model="form.territory" type="text" />
        </div>
      </div>

      <div class="actions">
        <button type="submit" :disabled="isSubmitting">Сохранить новость</button>
      </div>
    </form>
  </section>
</template>

<script>
const API_URL = "http://localhost:8000/api";

export default {
  name: "NewsCreateView",
  data() {
    return {
      newsMaterials: [],
      form: {
        news_material_id: "",
        title: "",
        text: "",
        author: "",
        category: "",
        territory: "",
        tag: ""
      },
      successMessage: "",
      errorMessage: "",
      isSubmitting: false
    };
  },
  mounted() {
    this.loadNewsMaterials();
  },
  methods: {
    async loadNewsMaterials() {
      try {
        const response = await fetch(`${API_URL}/news-materials/`);
        if (!response.ok) {
          throw new Error("Не удалось загрузить новостные материалы.");
        }
        this.newsMaterials = await response.json();
      } catch (error) {
        this.errorMessage = error.message;
      }
    },
    validateForm() {
      const requiredFields = [
        "news_material_id",
        "title",
        "text",
        "author",
        "category",
        "territory"
      ];
      return requiredFields.every((field) => String(this.form[field]).trim() !== "");
    },
    resetMessages() {
      this.successMessage = "";
      this.errorMessage = "";
    },
    resetForm() {
      this.form = {
        news_material_id: "",
        title: "",
        text: "",
        author: "",
        category: "",
        territory: "",
        tag: ""
      };
    },
    async saveNews() {
      this.resetMessages();

      if (!this.validateForm()) {
        this.errorMessage = "Заполните обязательные поля.";
        return;
      }

      this.isSubmitting = true;

      try {
        const response = await fetch(`${API_URL}/news/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(this.form)
        });

        if (!response.ok) {
          throw new Error("Ошибка сохранения новости.");
        }

        this.successMessage = "Новость сохранена";
        this.resetForm();
      } catch (error) {
        this.errorMessage = error.message;
      } finally {
        this.isSubmitting = false;
      }
    }
  }
};
</script>
