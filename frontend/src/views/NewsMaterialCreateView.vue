<template>
  <section class="page">
    <div class="page-header">
      <h2>Создание новостного материала</h2>
      <div v-if="successMessage" class="message success">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="message error">
        {{ errorMessage }}
      </div>
    </div>

    <form class="form" @submit.prevent="saveNewsMaterial">
      <div class="grid-two">
        <div class="field full">
          <label for="event_description">Описание события</label>
          <textarea
            id="event_description"
            v-model="form.event_description"
          ></textarea>
        </div>

        <div class="field">
          <label for="source">Источник сведений</label>
          <input id="source" v-model="form.source" type="text" />
        </div>

        <div class="field">
          <label for="received_at">Дата получения</label>
          <input id="received_at" v-model="form.received_at" type="datetime-local" />
        </div>

        <div class="field">
          <label for="event_place">Место события</label>
          <input id="event_place" v-model="form.event_place" type="text" />
        </div>

        <div class="field">
          <label for="material_author">Автор материала</label>
          <input id="material_author" v-model="form.material_author" type="text" />
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
        <button type="submit" :disabled="isSubmitting">
          Сохранить новостной материал
        </button>
      </div>
    </form>
  </section>
</template>

<script>
const API_URL = "http://localhost:8000/api";

export default {
  name: "NewsMaterialCreateView",
  data() {
    return {
      form: {
        event_description: "",
        source: "",
        received_at: "",
        event_place: "",
        material_author: "",
        category: "",
        territory: ""
      },
      successMessage: "",
      errorMessage: "",
      isSubmitting: false
    };
  },
  methods: {
    validateForm() {
      const requiredFields = [
        "event_description",
        "source",
        "material_author",
        "category",
        "territory"
      ];
      return requiredFields.every((field) => this.form[field].trim() !== "");
    },
    resetMessages() {
      this.successMessage = "";
      this.errorMessage = "";
    },
    resetForm() {
      this.form = {
        event_description: "",
        source: "",
        received_at: "",
        event_place: "",
        material_author: "",
        category: "",
        territory: ""
      };
    },
    buildPayload() {
      return {
        ...this.form,
        received_at: this.form.received_at || null
      };
    },
    async saveNewsMaterial() {
      this.resetMessages();

      if (!this.validateForm()) {
        this.errorMessage = "Заполните обязательные поля.";
        return;
      }

      this.isSubmitting = true;

      try {
        const response = await fetch(`${API_URL}/news-materials/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(this.buildPayload())
        });

        if (!response.ok) {
          throw new Error("Ошибка сохранения новостного материала.");
        }

        this.successMessage = "Новостной материал сохранён";
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
