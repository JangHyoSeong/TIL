<template>
  <div>
    <nav class="navbar">
      <!-- Named Routes : name 속성 값에 경로에 대한 이름을 지정하는 방법으로 
        경로 연결하려면 RouterLink에 v-bind를 사용해 ‘to’ props 객체로 전달 -->
      <RouterLink :to="{name: 'home'}" class="nav">홈으로</RouterLink>
      <RouterLink :to="{name: 'movies'}" class="nav">영화 조회</RouterLink>
      <RouterLink :to="{name: 'search'}" class="nav">영화검색</RouterLink>
    </nav>
  </div>
  <!-- RouterLink 클릭 시 경로와 일치하는 컴포넌트가 RouterView에서 렌더링 됨 -->
  <RouterView/>
</template>

<script setup>
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: right;
  align-items: center;
  width: 100%;
  height: 50px;
  background-color: gainsboro;
}
.navbar .nav {
  margin: 1%;
  text-decoration: none;
}
</style>