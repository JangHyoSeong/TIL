<template>
    <li>{{ child.name }}</li>
</template>

<script setup>
defineProps({
  child: Object
})
</script>

<style scoped>

</style>