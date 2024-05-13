<template>
  <div>
    <p>{{ todo.work }}</p>
    <p>{{ todo.content }}</p>
    <p>{{ todo.is_completed }}</p>
    <p>{{ todo.created_at }}</p>
    <RouterLink :to="{name: ''}">상세보기</RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  todo: Object
})
</script>

<style scoped>

</style>