<script setup>
import { ref } from 'vue'
import BusinessCard from '@/components/BusinessCard.vue'

const businessCards = ref([
    {name: '일론 머스크', title: '테슬라 테크노 킹'},
    {name: '래리 엘리슨', title: '오라클 창업주'},
    {name: '빌 게이츠', title: '마이크로소프트 공동창업주'},
    {name: '래리 페이지', title: '구글 공동창업주'},
    {name: '세르게이 브린', title: '구글 공동창업주'},
])

</script>

<template>
  <header>
    <h1>명함 관리 페이지</h1>
  </header>
  <main>
    <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
  </main>
  <article>
    <h3>보유 명함 목록</h3>
    <BusinessCard :businessCards="businessCards"/>
  </article>
  <footer>
    <p>푸터</p>
  </footer>
</template>

<style scoped>
header {
  background-color: blue;
  color: white;
  text-align: center;
}

footer {
  position: absolute;
  bottom: 0;
  width: 100%;
  text-align: center;
}
</style>
