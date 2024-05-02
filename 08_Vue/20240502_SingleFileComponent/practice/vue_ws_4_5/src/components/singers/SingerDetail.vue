<template>
  <card class="singer-detail center">
    <h1>가수 이름</h1>
    <img class="singer-image" src="@/assets/singer.jpg" alt="singer" width="200">
    <p>가수 소개글</p>
    <div class="album-wrapper">
      <SingerAlbum/>
      <SingerAlbum/>
    </div>
  </card>
</template>

<script setup>
import SingerAlbum from './SingerAlbum.vue';


</script>

<style scoped>
.singer-detail {
  border: 2px solid black;
}
.singer-image {
  border-radius: 50%;
}
card{
  display: inline-block;
  width: 40%;
  margin: 20px;
}
card img {
  max-width: 100%;
  height: auto;
}
.album-wrapper{
  display: flex;
  justify-content: space-around;
  margin-bottom: 10px;
}
</style>