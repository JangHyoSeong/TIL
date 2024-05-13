<template>
  <div>
    <div v-for="post in postList" :key="post.pk">
      <p>{{ post.title }}</p>
      <p>{{ post.category }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  postList: Array
})
</script>

<style scoped>

</style>