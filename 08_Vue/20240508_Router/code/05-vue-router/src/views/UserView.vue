<template>
  <div>
    <RouterLink :to="{ name: 'user-profile' }">Profile</RouterLink>
    <RouterLink :to="{ name: 'user-posts' }">Posts</RouterLink>
    <button @click="goHome">홈으로!</button>
    <h1>UserView</h1>
    <h2>{{ $route.params.id }}번 User 페이지</h2>
    <h2>{{ userId }}번 User 페이지</h2>
    <button @click="routeUpdate">100번 유저 페이지</button>
    <RouterView />
  </div>
</template>

<script setup>
import {ref} from 'vue'
import {useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate} from 'vue-router'

onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false
  }
})

const route = useRoute()
const router = useRouter()
const userId = ref(route.params.id)
const goHome = function () {
  router.push({name: 'home'})
}

const routeUpdate = function () {
  router.push({ name: 'user', params: {id:100}})
}

// onBeforeRouteUpdate((to, from) => {
//   userId.value= to.params.id
// })
</script>

<style scoped>

</style>