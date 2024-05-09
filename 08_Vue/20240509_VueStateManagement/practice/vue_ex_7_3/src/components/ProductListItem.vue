<template>
  <li>
    {{ product.id }} - {{ product.title }} - {{ product.body }}
    <button @click="deleteProduct(product.id)">Delete</button>
  </li>
</template>

<script setup>
import { useProductStore } from '@/stores/product'
import axios  from 'axios'

defineProps({
  product: Object
})

const store = useProductStore()

const deleteProduct = function (productId) {
  store.deleteProduct(productId)
}
</script>

<style scoped>

</style>
