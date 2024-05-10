<template>
  <!-- 영화 목록을 렌더링하는 영역입니다. -->
  <div v-for="movie in store.movieList.results">
    <!-- MovieCard 컴포넌트를 반복하여 표시합니다. -->
    <MovieCard 
      :movie="movie"
      @click="goDetailPage(movie.id)"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import MovieCard from '@/components/MovieCard.vue'; // MovieCard 컴포넌트를 임포트합니다.
import { useMovieStore } from '@/stores/movie'; // useMovieStore를 임포트합니다.
import { useRoute, useRouter } from 'vue-router'; // useRoute와 useRouter를 임포트합니다.

const store = useMovieStore() // 영화 스토어를 사용합니다.
onMounted(() => {
  store.getMovieList() // 페이지가 마운트되면 영화 목록을 가져옵니다.
})

const router = useRouter() // 라우터를 사용합니다.

// 영화 상세 페이지로 이동하는 함수입니다.
const goDetailPage = function(movieId) {
  router.push({name: 'moviedetail', params:{movieId: movieId}}) // 해당 영화의 상세 페이지로 이동합니다.
}
</script>

<style scoped>
</style>
