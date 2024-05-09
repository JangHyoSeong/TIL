<template>
  <div>
    <RouterLink :to="{name: 'main'}">main</RouterLink>
    <h1>Pinia + Router 연습하기</h1>
    <MainPage />
  </div>
</template>

<script setup>
import MainPage from './components/MainPage.vue'
import { RouterLink } from 'vue-router'

</script>

<style scoped>

</style>