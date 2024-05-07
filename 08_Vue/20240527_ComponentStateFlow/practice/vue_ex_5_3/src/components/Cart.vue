<template>
  <div v-show="carts.length > 0">
    <h2>장바구니</h2>
    <ul>
      <li v-for="cart in carts">
        {{ cart.name }} - {{ cart.price }}원
        <button @click="removeCart(cart)">삭제</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  carts: Array,
})

const emit = defineEmits(['removeCart'])

const removeCart = function (cart) {
  emit('removeCart', cart)
}

</script>