import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useTodoStore = defineStore('todo', () => {

  const todos = ref([])
  const BASE_URL = 'http://127.0.0.1:8000'

  const getTodos = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/api/v1/todos/`
    })
      .then(res => {
        todos.value = res.data
      })
      .catch(err => console.log(err))
  }

  return { todos, getTodos }
}, { persist: true })
