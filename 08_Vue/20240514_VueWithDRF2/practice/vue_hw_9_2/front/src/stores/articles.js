import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/'
    })
    .then(res => articles.value = res.data)
  }

  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => console.log(res))
  }

  const signUp = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/signup/',
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log('회원가입 완료')
        const payload = {
          username: username,
          password: password1
        }
        logIn(payload)
      })
      .catch(err => console.log(err))
  }

  const router = useRouter()
  const token = ref(null)


  
  const logIn = function (payload) {
    const username = payload.username
    const password = payload.password

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/login/',
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인 성공')
        token.value = res.data.key
        console.log(token.value)
        router.push({name: 'home'})
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

  return { articles, getArticles, createArticle, signUp, logIn, token, isLogin }
}, { persist: true })
