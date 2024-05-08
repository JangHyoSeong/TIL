<template>
  <div>
    <h1>User Profile</h1>
    <p>Username : {{ userName }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const userName = ref(route.params.username)
</script>

<style scoped>

</style>