<template>
    <li>
      <RouterLink :to="{name: 'post-detail', params: {username: refUserName, id: post.id}}"> 제목: {{ post.title }} </RouterLink>
    </li>
</template>

<script setup>
import {ref} from 'vue'
import { RouterView, RouterLink, useRoute } from 'vue-router'

const route = useRoute()

const refUserName = ref(route.params.username)

defineProps({
  post: Object,
})
</script>

<style scoped>

</style>