<template>
  <div>
    <input type="text" v-model="searchTarget">
    <button @click="searchYT">검색</button>

    <div v-for="video in videos.items" :key="video.id.videoId" class="video-container">
      <div @click="openModal(video)">
        <div class="img-container">
          <img :src="video.snippet.thumbnails.default.url" alt="">
        </div>
        <div class="text-container">
          <p>{{ video.snippet.title }}</p>
          <p>{{ video.snippet.description }}</p>
        </div>
        <hr>
      </div>
    </div>
    
    <YoutubeReviewModal :video="selectedVideo" :modalOn="modalOn" @modalOff="offModal" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import YoutubeReviewModal from '@/components/YoutubeReviewModal.vue'

const searchTarget = ref('')
const videos = ref('')
const selectedVideo = ref(null)
const modalOn = ref(false)

const searchYT = function() {
  const API_KEY = import.meta.env.VITE_YT_API_KEY

  axios({
    method: 'get',
    url: `https://www.googleapis.com/youtube/v3/search?key=${API_KEY}`,
    params: {
      part: 'snippet',
      q: searchTarget.value,
      maxResults: 10,
      type: 'video',
    }
  })
    .then((response) => {
      videos.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
}

const openModal = function (video) {
  selectedVideo.value = video
  modalOn.value = true
}

const offModal = function (){
  modalOn.value = false
}

</script>

<style scoped>
.video-container{
  display: flex;
  align-items: center;
}
.img-container{
  flex: 0 0 auto;
  margin-right: 20px;
}

.text-container{
  flex: 1;
}
hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 20px 0;
}
</style>
