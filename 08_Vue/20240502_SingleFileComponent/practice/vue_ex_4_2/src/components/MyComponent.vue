<template>
  <div>
    <header class="fixed-top text-center bg-primary-subtle">
      <h1>Gallery</h1>
    </header>

    <main class="container pt-5 mt-3">
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3">
        <div v-for="card in numberOfItems" class="card col m-3" style="width: 18rem;">
          <img src="../assets/sample.png" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's
              content.</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const numberOfItems = ref(4)
</script>

<style scoped></style>
