<template>
  <div>
    <h1>학생 상세 정보 페이지입니다.</h1>
    <p v-for="student in students" :key="student.name" @click="goToStudentDetail(student)">{{ student.name }} 학생 정보 보기</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const router = useRouter()

const students = ref([
  {name: '김하나'},
  {name: '김두리'},
  {name: '김서이'},
])

const goToStudentDetail = function (student) {
  router.push({name: 'student-detail', params: {name: student.name}})
}


</script>

<style scoped>

</style>