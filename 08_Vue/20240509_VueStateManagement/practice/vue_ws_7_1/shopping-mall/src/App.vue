<template>
    <navbar>
      <RouterLink :to="{name: 'home'}">Home</RouterLink>
      <RouterLink :to="{name: 'products'}">Products</RouterLink>
      <RouterLink :to="{name: 'favorite'}">Favorite</RouterLink>
    </navbar>
    <RouterView/>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
navbar {
  color: white;
  background-color: black;
}
</style>