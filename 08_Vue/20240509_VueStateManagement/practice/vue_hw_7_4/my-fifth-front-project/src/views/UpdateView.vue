<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름 : {{ balance.name }}</p>
    <p>잔고 : {{ balance.balance }}</p>
    <button @click="updateBalance(balance)">+</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const route = useRoute()
const store = useBalanceStore()

const name = ref(route.params.name)
const balance = store.getBalanceByName(name.value)

const updateBalance = function(balance) {
  balance.balance += 1000
}
</script>

<style scoped>

</style>