<template>
  <div>
    <h2>부모 컴포넌트</h2>
    <ul>
      <li>familyName : {{ family.familyName }}</li>
      <li>father : {{ family.father }}</li>
      <li>mother : {{ family.mother }}</li>
      <li>children
        <ul>
          <ChildPage 
            v-for="child in family.children" 
            :key="child.name"
            :child="child"  
          />
        </ul>
      </li>
      
    </ul>
  </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue'

defineProps({
  family: Object
})

</script>

<style scoped>

</style>