<template>
  <div>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password">password : </label>
      <input type="text" id="password" v-model="password"><br>

      <input type="submit" value="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '../stores/articles'

const store = useArticleStore()

const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<style scoped>

</style>