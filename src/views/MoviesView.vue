<script setup>

import { ref, onMounted } from "vue";

let movies = ref([]);

const fetchMovies = async () => {
  try {
    const response = await fetch("/api/v1/movies");
    const data = await response.json();
    movies.value = data.movies;
    console.log(data.movies)
  } catch (error) {
    console.error("Error fetching movies:", error);
  }
};

onMounted(() => {
  fetchMovies();
});
</script>

<template>
    <div class="movies-view">
      <h1>Movies</h1>
      <div class="movies-list">
        <div v-for="movie in movies" :key="movie.id" class="movie-card">
          <img :src="movie.poster" :alt="movie.title" class="movie-poster" />          <h2>{{ movie.title }}</h2>
          <p>{{ movie.description }}</p>
        </div>
      </div>
    </div>
</template>

<style scoped>
.movies-view {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.movies-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.movie-card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  width: 100%;
  max-width: 300px;
  text-align: center;
}

.movie-poster {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
}
</style>
  