<template>
  <header>
    <h1>Quiz</h1>
    <p>여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해 보세요</p>
  </header>
  <RouterLink :to="{name: 'home'}">Home</RouterLink>
  <RouterView />

</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
header {
  border: 2px solid black;
}
</style>