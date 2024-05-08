<template>
  <div>
    <h2>{{userName}}이 작성한 게시글</h2>
    <ol>
      <PostListItem v-for="post in posts" :key="post.id" :post="post"/>
    </ol>
    <hr>
    <RouterView />
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useRoute, RouterView } from 'vue-router'
import PostListItem from '@/components/PostListItem.vue'

let postId = 0
const posts = ref([
  {id: ++postId, title: `Post${postId}`, content: `Content${postId}`},
  {id: ++postId, title: `Post${postId}`, content: `Content${postId}`},
  {id: ++postId, title: `Post${postId}`, content: `Content${postId}`},
])

const route = useRoute()
const userName = ref(route.params.username)
</script>

<style scoped>

</style>