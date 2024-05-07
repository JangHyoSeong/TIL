<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ childProp.name }}</p>
    <p>나이 : {{ childProp.age }}</p>
  </div>
</template>

<script setup>
defineProps({
  childProp: Object,
})
</script>

<style scoped>

</style>