
<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'home' }">Home</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'about' }">About</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'user', params: {username: userName } }">User</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

const userName = ref('admin')
</script>

<style scoped>
</style>
