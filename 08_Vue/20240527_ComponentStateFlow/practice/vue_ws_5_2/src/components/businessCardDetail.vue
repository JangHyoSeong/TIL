<template>
<div v-for="card in businessCards" :key="card.name">
    <p>이름 : {{ card.name }}</p>
    <p>직함 : {{ card.title }}</p>
</div>
</template>

<script setup>
defineProps({
    businessCards: Array
})
</script>

<style scoped>
    
</style>