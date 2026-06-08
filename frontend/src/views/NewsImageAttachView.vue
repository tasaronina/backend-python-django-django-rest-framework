<template>
  <section class="page">
    <div class="page-header">
      <h2>Прикрепление изображения</h2>
      <div v-if="successMessage" class="message success">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="message error">
        {{ errorMessage }}
      </div>
    </div>

    <form class="form" @submit.prevent="attachImage">
      <div class="grid-two">
        <div class="field full">
          <label for="news_id">Новость</label>
          <select id="news_id" v-model="form.news_id">
            <option value="">Выберите новость</option>
            <option v-for="newsItem in news" :key="newsItem.id" :value="newsItem.id">
              {{ newsItem.title }}
            </option>
          </select>
        </div>

        <div class="field full">
          <label for="image">Файл изображения</label>
          <input
            id="image"
            ref="imageInput"
            accept=".jpeg,.jpg,.png,image/jpeg,image/png"
            type="file"
            @change="setImage"
          />
        </div>
      </div>

      <div class="actions">
        <button type="submit" :disabled="isSubmitting">
          Прикрепить изображение
        </button>
      </div>
    </form>
  </section>
</template>

<script>
const API_URL = "http://localhost:8000/api";
const ALLOWED_EXTENSIONS = ["jpeg", "jpg", "png"];

export default {
  name: "NewsImageAttachView",
  data() {
    return {
      news: [],
      form: {
        news_id: "",
        image: null
      },
      successMessage: "",
      errorMessage: "",
      isSubmitting: false
    };
  },
  mounted() {
    this.loadNews();
  },
  methods: {
    async loadNews() {
      try {
        const response = await fetch(`${API_URL}/news/`);
        if (!response.ok) {
          throw new Error("Не удалось загрузить новости.");
        }
        this.news = await response.json();
      } catch (error) {
        this.errorMessage = error.message;
      }
    },
    setImage(event) {
      this.resetMessages();
      const file = event.target.files[0];

      if (!file) {
        this.form.image = null;
        return;
      }

      const extension = file.name.split(".").pop().toLowerCase();
      if (!ALLOWED_EXTENSIONS.includes(extension)) {
        this.form.image = null;
        this.errorMessage = "Формат изображения должен быть JPEG, JPG или PNG.";
        event.target.value = "";
        return;
      }

      this.form.image = file;
    },
    validateForm() {
      if (!this.form.news_id) {
        return false;
      }
      return Boolean(this.form.image);
    },
    resetMessages() {
      this.successMessage = "";
      this.errorMessage = "";
    },
    resetForm() {
      this.form = {
        news_id: "",
        image: null
      };
      if (this.$refs.imageInput) {
        this.$refs.imageInput.value = "";
      }
    },
    async attachImage() {
      this.resetMessages();

      if (!this.validateForm()) {
        this.errorMessage = "Выберите новость и файл изображения.";
        return;
      }

      const formData = new FormData();
      formData.append("news_id", this.form.news_id);
      formData.append("image", this.form.image);

      this.isSubmitting = true;

      try {
        const response = await fetch(`${API_URL}/news-images/`, {
          method: "POST",
          body: formData
        });

        if (!response.ok) {
          throw new Error("Ошибка прикрепления изображения.");
        }

        this.successMessage = "Изображение прикреплено к новости";
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
