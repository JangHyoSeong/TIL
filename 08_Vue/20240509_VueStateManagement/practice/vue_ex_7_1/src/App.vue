<template>
  <h1>Product List</h1>
  <div>
    <ul>
      <ProductList v-for="product in store.products" :key="product.id" :product="product"/>
    </ul>
  </div>
</template>

<script setup>
import ProductList from '@/components/ProductList.vue'
import { useProductStore } from '@/stores/product'

const store = useProductStore()
</script>

<style scoped>
</style>
