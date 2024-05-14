<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useArticleStore } from './stores/articles'

const store = useArticleStore()
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink> | 
        <RouterLink :to="{name: 'signup'}" v-if="!store.isLogin">SignUp | </RouterLink>
        <RouterLink :to="{name: 'signin'}" v-if="!store.isLogin">SignIn</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
