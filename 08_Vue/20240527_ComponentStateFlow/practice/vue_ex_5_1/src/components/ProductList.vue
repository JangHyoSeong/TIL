<template>
  <li>{{ productProp.name }} - {{ productProp.price }}원</li>
</template>

<script setup>
defineProps({
  productProp: Object
})
</script>