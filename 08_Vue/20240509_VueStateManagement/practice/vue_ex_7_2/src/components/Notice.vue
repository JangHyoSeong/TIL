<template>
  <div>
    <h4>남은 제품 개수 : {{ store.productCount }}</h4>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'

const store = useProductStore()
</script>