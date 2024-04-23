const player1Img = document.querySelector('#player1-img')
const player2Img = document.querySelector('#player2-img')

const scissorsBtn = document.querySelector('#scissors-button')
const rockBtn = document.querySelector('#rock-button')
const paperBtn = document.querySelector('#paper-button')

const randInt = function (max){
    return Math.floor(Math.random() * max)
}

const changeSelect = function () {
    const select = ['scissors', 'rock', 'paper']
    const randomSelect = select[randInt(3)]
    player2Img.setAttribute('src', `./img/${randomSelect}.png`)
    player2Img.setAttribute('alt', randomSelect)
}

const playGame = function (player1, player2){
    let result = 0
    if (player1 === 'scissors'){
        if (player2 === 'rock'){
            result = 2
        } else if (player2 === 'paper'){
            result = 1
        }
    } else if (player1 === 'rock'){
        if (player2 === 'scissors'){
            result = 1
        } else if(player2 === 'paper'){
            result = 2
        }
    } else if (player1 === 'paper'){
        if (player2 === 'rock'){
            result = 1
        } else if (player2 === 'scissors'){
            result = 2
        }
    }
    const countA = document.querySelector('.countA')
    let count1 = Number(countA.textContent)
    const countB = document.querySelector('.countB')
    let count2 = Number(countB.textContent)
    if (result == 1){
        count1 += 1
        countA.textContent = count1
    } else if(result == 2){
        count2 += 1
        countB.textContent = count2
    }
    return result
}

const buttonClickHandler = function (event) {
    const imgSrc = event.currentTarget.querySelector('img')
    player1Img.setAttribute('src', imgSrc.src)
    player1Img.setAttribute('alt', imgSrc.alt)

    scissorsBtn.disabled = true
    rockBtn.disabled = true
    paperBtn.disabled = true
    
    intevalId = setInterval(changeSelect, 100)

    setTimeout(() => {
        clearInterval(intevalId)
        scissorsBtn.disabled = false
        rockBtn.disabled = false
        paperBtn.disabled = false

        const result = playGame(player1Img.alt, player2Img.alt)
        const modal = document.querySelector('.modal')
        const modalContent = document.querySelector('.modal-content')
        modal.style.display = 'flex'
        
        if (result == 1){
            modalContent.textContent = 'player 1 win'
        } else if (result == 2){
            modalContent.textContent = 'player 2 win'
        } else if (result == 0){
            modalContent.textContent = 'draw'
        }

        setTimeout(() => {
            modal.style.display = 'none'
            modalContent.textContent = ''
        }, 2500)
    }, 3000)

    

}

scissorsBtn.addEventListener('click', buttonClickHandler)
rockBtn.addEventListener('click', buttonClickHandler)
paperBtn.addEventListener('click', buttonClickHandler)