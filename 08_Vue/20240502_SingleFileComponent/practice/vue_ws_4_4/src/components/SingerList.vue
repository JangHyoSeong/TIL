<template>
  <h1 class="center">가수 목록</h1>
  <SingerDetail />
  <SingerDetail />
</template>

<script setup>
import SingerDetail from './singers/SingerDetail.vue';


</script>

<style scoped>
.center {
  text-align: center;
}
card{
  display: inline-block;
  width: 40%;
  margin: 20px;
}
h1{
  color: orangered;
}
</style>