<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">클릭</button>
    <button @click="emitArgs">추가 인자 전달</button>
    <ParentGrandChild :my-msg="myMsg" @update-name="updateName"/>
    <!-- v-bind를 사용한 동적 props -->
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue';

// defineProps(['myMsg'])
defineProps({
  myMsg: String,
  dynamicProps: String,
})

const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

const buttonClick = function () {
  emit('someEvent')
}

const emitArgs = function (){
  emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
  emit('updateName')
}

// const props = defineProps({myMsg:String})
// console.log(props) // {myMsg: 'message'}
// console.log(props.myMsg) // 'message'
</script>