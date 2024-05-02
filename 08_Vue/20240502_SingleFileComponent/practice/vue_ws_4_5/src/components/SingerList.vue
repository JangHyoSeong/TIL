<template>
  <h1 class="center">가수 목록</h1>
  <div class="card-wrapper" v-for="singer in singers">
    <SingerDetail />
  </div>
</template>

<script setup>
import SingerDetail from './singers/SingerDetail.vue';
import {ref} from 'vue'

const singers = ref([
  {
    name: 'adele'
  },
  {
    name: 'maroon 5'
  },
  {
    name: 'Dua Lipa'
  }
])

</script>

<style scoped>
.center {
  text-align: center;
}
.card-wrapper {
  display: inline-block;
  width: 40%;
  margin: 20px;
}
card{
  display: inline-block;
  width: 100%;
  margin: 20px;
}
h1{
  color: orangered;
}
</style>