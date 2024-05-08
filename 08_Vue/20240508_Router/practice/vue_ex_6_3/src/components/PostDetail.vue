<template>
  <p>번호 : {{ posts[postIndex].id }}</p>
  <p>제목 : {{ posts[postIndex].title }}</p>
  <p>내용 : {{ posts[postIndex].content }}</p>
</template>

<script setup>
import {ref} from 'vue'
import {useRoute, onBeforeRouteUpdate} from 'vue-router'

const router = useRoute()

const postIndex = ref(router.params.id -1)

let postId = 0
const posts = ref([
  {id: ++postId, title: `Post${postId}`, content: `Content${postId}`},
  {id: ++postId, title: `Post${postId}`, content: `Content${postId}`},
  {id: ++postId, title: `Post${postId}`, content: `Content${postId}`},
])

onBeforeRouteUpdate((to, from) => {
  postIndex.value = to.params.id - 1
})
</script>

<style scoped>

</style>