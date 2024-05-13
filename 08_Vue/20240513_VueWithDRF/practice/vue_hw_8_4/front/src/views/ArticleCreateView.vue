<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="title">
      <br>
      <label for="content">내용 : </label>
      <input type="text" id="content" v-model="content">
      <br>
      <input type="submit" value="create">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const title = ref(null)
const content = ref(null)

const createArticle = function () {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    }
  })
    .then(() => {
      router.push({name: 'home'})
    })
    .catch((err) => console.log(err))
}

</script>

<style scoped>

</style>