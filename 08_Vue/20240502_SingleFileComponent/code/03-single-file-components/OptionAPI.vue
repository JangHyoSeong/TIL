<template>
  <button @click="increment">{{ count }}</button>
</template>

<script>
export default {
  data () {
    return{
      count: 0
    }
  },

  methods: {
    increment(){
      this.count++
    }
  },

  mounted() {
    console.log(`숫자 세기의 초기값은 ${this.count}`)
  }
}
</script>