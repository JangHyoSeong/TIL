import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  let id = 1
  const products = ref([
    {id: id++, title: 'title 1', body: 'body 1'},
    {id: id++, title: 'title 2', body: 'body 2'},
    {id: id++, title: 'title 3', body: 'body 3'}
  ])

  return { products }
})
