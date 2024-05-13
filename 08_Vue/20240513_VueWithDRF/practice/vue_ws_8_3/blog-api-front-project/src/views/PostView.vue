<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <PostList :postList="postList"/>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import PostList from '@/components/PostList.vue'

const postList = ref(null)
onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/posts/'
  })
    .then(res => {
      postList.value = res.data
      console.log(postList.value)
    })
    .catch(err => console.log(err))
})
</script>

<style scoped>

</style>