<template>
  <div>
    <li>{{ product.id}} - {{ product.title }} - {{ product.body }}</li>
  </div>
</template>

<script setup>
defineProps({
  product:Object
})
</script>

<style scoped>

</style>