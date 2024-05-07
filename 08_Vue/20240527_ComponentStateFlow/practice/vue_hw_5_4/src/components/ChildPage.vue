<template>
  <h3>자식 페이지입니다.</h3>
  <p>이름 : {{ childProp.name }}</p>
  <p>나이 : {{ childProp.age }}</p>
  <p>용돈 : {{ childProp.balance }}</p>
  <button @click="giveMeAllowance">용돈 주세요</button>
</template>

<script setup>
defineProps({
  childProp: Object,
})

const emit = defineEmits(['giveMeAllowance'])

const giveMeAllowance = function () {
  emit('giveMeAllowance')
}
</script>