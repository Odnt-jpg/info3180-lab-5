<template>
  <div class="movie-form">
    <h1>Add a Movie</h1>
    <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input
          type="text"
          id="title"
          name="title"
          class="form-control"
          v-model="movie.title"
          required
        />
      </div>
      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea
          id="description"
          name="description"
          class="form-control"
          v-model="movie.description"
          required
        ></textarea>
      </div>
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster</label>
        <input
          type="file"
          id="poster"
          name="poster"
          class="form-control"
          @change="handleFileUpload"
          required
        />
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    <div v-if="message" class="alert alert-success mt-3">
      {{ message }}
    </div>
    <div v-if="errors.length" class="alert alert-danger mt-3">
      <ul>
        <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const movie = ref({
  title: '',
  description: '',
  poster: null,
});

const csrf_token = ref('');
const message = ref('');
const errors = ref([]);

const getCsrfToken = () => {
  fetch('/api/v1/csrf-token')
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    })
    .catch((error) => {
      console.error('Error fetching CSRF token:', error);
    });
};

const handleFileUpload = (event) => {
  movie.value.poster = event.target.files[0];
};

const saveMovie = () => {
  const formData = new FormData();
  formData.append('title', movie.value.title);
  formData.append('description', movie.value.description);
  formData.append('poster', movie.value.poster);

  fetch('/api/v1/movies', {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': csrf_token.value, 
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.errors) {
        errors.value = data.errors;
        message.value = '';
      } else {
        message.value = data.message;
        errors.value = [];
        movie.value = { title: '', description: '', poster: null };
      }
    })
    .catch((error) => {
      console.error('Error saving movie:', error);
    });
};

onMounted(() => {
  getCsrfToken();
});
</script>

<style scoped>
.movieForm {
  max-width: 600px;
  margin: 0 auto;
}
</style>