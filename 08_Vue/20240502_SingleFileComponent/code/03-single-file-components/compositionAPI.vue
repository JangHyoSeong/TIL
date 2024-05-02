<template>
  <button @click="increment">{{ count }}</button>
</template>

<script setup>
import {ref, onMounted} from 'vue'

const count = ref(0)

function increment() {
  count.value++
}

onMounted(() => {
  console.log(`숫자 세기의 초기 값은 ${count.value}`)
})
</script>
