<template>
  <div class="modal" v-if="modalOn" @click="ModalClick">
    <div class="modal-content" @click.stop>
      <button @click="modalOff">x</button>
      <div class="modal-title">{{ video.snippet.title }}</div>
      <div class="modal-body">
        <iframe width="560" height="315" :src="videoUrl" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, defineEmits, defineProps } from 'vue'

const emit = defineEmits(['modalOff'])

const props = defineProps({
  video: Object,
  modalOn: Boolean
})

const videoUrl = computed(() => {
  if (props.video) {
    return `https://www.youtube.com/embed/${props.video.id.videoId}`
  }
})

const modalOff = function () {
  emit('modalOff')
}

const ModalClick = function (event) {
  if (event.target.classList.contains('modal')) {
    modalOff()
  }
}
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color:rgba(0, 0, 0, 0.205);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  max-width: 80%;
  max-height: 80%;
  overflow-y: auto; 
}

.modal-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.modal-body {
  font-size: 16px;
}
</style>