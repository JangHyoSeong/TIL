<template>
  <div>
    <nav>
      <p @click="goHome">Home</p>
      <p @click="goPost">PostList</p>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { useRouter, RouterView } from 'vue-router'

const router = useRouter()

const goHome = function () {
  router.push({name: 'main'})
}

const goPost = function () {
  router.push({name: 'posts'})
}
</script>

<style scoped>
nav {
  background-color: black;
  color: white;
  justify-content: center;
  display: flex;
  width: 100%;
  height: 50px;
  font-weight: bold;
}
nav p {
  margin-right: 10px;
}
</style>