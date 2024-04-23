/* 
  아래에 코드를 작성해주세요.
*/
const API_KEY = ''
const API_URI = ' http://ws.audioscrobbler.com/2.0/'

const searchBtn = document.querySelector('.search-box__button')


const fetchAlbums = function (page=1, limit=10) {
  alert('확인!')
  
  const keyword = document.querySelector('.search-box__input').value
  axios({
    method: 'get',
    url : API_URI,

    params:{
      method: 'album.search',
      api_key : API_KEY,
      album : keyword,
      format: 'json',
    }
  })
    .then((response) => {
      let albums = []
      for (album of response.data.results.albummatches.album){
        albums.push(album)
      }
      console.log(albums)
      return albums
    })
    .then((albums) => {
      const searchResult = document.querySelector('.search-result')
      for (album of albums){

        const card = document.createElement('div')
        card.classList.add('search-result__card')
        searchResult.appendChild(card)

        const cardImg = document.createElement('img')
        cardImg.src = album.image[1]['#text']

        card.appendChild(cardImg)

        const cardText = document.createElement('div')
        cardText.classList.add('search-result__text')

        card.appendChild(cardText)
        
        const artistName = document.createElement('h2')
        artistName.textContent = album.artist

        const albumName = document.createElement('p')
        albumName.textContent = album.name
        
        cardText.appendChild(artistName)
        cardText.appendChild(albumName)

        
      }
    })
    .catch((error) => {
      alert('잠시 후 다시 시도해주세요.')
    })
}

searchBtn.addEventListener('click', fetchAlbums)