<template>
  <header>
    <nav>
      <RouterLink :to="{name: 'TodoView'}">할 일 목록 </RouterLink> 
      <RouterLink :to="{name: ''}">회원가입 </RouterLink>
      <RouterLink :to="{name: ''}">로그인</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
