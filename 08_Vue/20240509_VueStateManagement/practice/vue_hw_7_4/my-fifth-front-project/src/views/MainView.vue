<template>
  <div>
    <h3>메인 페이지</h3>
    <span v-for="balance in store.balances" :key="balance.name">
      <p>이름 : {{ balance.name }}</p>
      <p>잔고 : {{ balance.balance }}</p>
      <button id="update-balance" @click="updateBalance(balance)">updateBalance</button>
      <hr>
    </span>
  </div>
</template>

<script setup>
import { useBalanceStore  } from '@/stores/balance'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useBalanceStore()

const updateBalance = function (balance) {
  return router.push({name: 'update', params:{name: balance.name}})
}
</script>

<style scoped>
#update-balance {
  background-color: black;
  color: white;
  border-radius: 10px;
}
</style>