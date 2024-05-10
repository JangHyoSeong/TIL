import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

// 영화 목록을 관리하는 Pinia 스토어를 정의합니다.
export const useMovieStore = defineStore('movie', () => {
  // 영화 목록을 저장할 ref 변수를 생성합니다.
  const movieList = ref([])

  const getMovieList = function() {
    // 환경 변수에서 TMDB API 키를 가져옵니다.
    const API_KEY = import.meta.env.VITE_TMDB_API_KEY
    
    // TMDB API를 사용하여 최고 평점 영화 목록을 가져옵니다.
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}`,
      params: {
        language: 'ko-KR'
      }
    })
    .then((response) => {
      // API 요청에 성공하면 응답 데이터를 영화 목록에 할당합니다.
      movieList.value = response.data
    })
    .catch((error) => {
      console.log(error);
    })
  }
  
  // 영화 목록과 가져오는 함수를 외부에서 사용할 수 있도록 반환합니다.
  return { getMovieList, movieList }
})
