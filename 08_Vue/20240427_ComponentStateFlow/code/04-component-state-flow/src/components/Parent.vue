<template>
  <div>
    <!-- <ParentChild @some-event="someCallback" my-msg="message" :dynamic-props="name"/> -->
  </div>
  <div>

    <ParentItem 
    v-for="item in items"
    :key="item.id"
    :my-prop="item"
    />
    <hr>
    <ParentChild 
      @some-event="someCallback"
      @emit-args="getNumbers"
      my-msg="message"
      :dynamic-props="name"
      @update-name="updateName"/>

    <!-- <ParentChild @update-name="updateName" /> -->
  </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue'
import ParentItem from './ParentItem.vue';

import {ref} from 'vue'

const items = ref([
  {id: 1, name: '사과'},
  {id: 2, name: '바나나'},
  {id: 3, name: '딸기'},
])

const someCallback = function () {
  console.log('ParentChild가 발신한 이벤트를 수신했어요.')
}

const getNumbers = function (...args) {
  console.log(args)
  console.log(`ParentChild가 전달한 추가인자 ${args}를 수신했어요.`)
}

const updateName = function () {
  name.value = 'Bella'
}

const name = ref('Alice')
</script>