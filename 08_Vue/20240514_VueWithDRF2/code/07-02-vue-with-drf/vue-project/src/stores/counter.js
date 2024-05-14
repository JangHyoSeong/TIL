import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const signUp = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    // const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log('회원가입이 완료되었습니다.')
        const password = password1
        logIn({username, password})
      })
      .catch(err => console.log(err))
  }

  const token = ref(null)

  const logIn = function (payload) {
    const username = payload.username
    const password = payload.password

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인이 완료되었습니다.')
        token.value = res.data.key
        router.push({name: 'ArticleView'})
      })
      .catch(err => console.log(err))
  }

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  
  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
}, { persist: true })
