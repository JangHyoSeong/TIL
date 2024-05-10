<template>
  <div class="outImg">
    <div class="MovieImg">
      <img :src="imgSrc" >
      <p>{{ movie.title }}</p>
      <p>{{ movie.overview }}</p>
    </div>
  </div>
</template>

<script setup>
// Vue Composition API의 ref를 가져옵니다.
import { ref } from 'vue'

// 부모 컴포넌트로부터 영화 객체를 받는 props를 정의합니다.
const props = defineProps({
  movie: Object
})

// API로부터 받은 영화 포스터 이미지 주소를 동적으로 설정합니다.
const imgSrc = ref(`https://image.tmdb.org/t/p/w500/${props.movie.poster_path}`)
</script>

<style scoped>
.outImg {
  display: flex;
  justify-content: center;
}
.MovieImg {
  text-align: center;
  margin: 2%;
  width: 500px;
  height: 1000px;
  border: 1px solid black;
}
</style>