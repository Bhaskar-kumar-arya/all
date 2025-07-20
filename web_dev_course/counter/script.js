const inc_button = document.getElementById('increment-btn')
const dec_button = document.getElementById('decrement-btn')
const count_txt = document.getElementById('count')
let counter = 0

document.getElementsByTagName('body')[0].style.display = 'flex'
document.getElementsByTagName('body')[0].style.flexWrap = 'wrap'

inc_button.addEventListener('click',function () {
    const newElement = document.createElement('div') 
    newElement.setAttribute('data-count',counter)
    newElement.innerHTML = "<b>new element created. count</b> : " + counter
    if (counter % 2 === 0) {
        newElement.style.background = 'red'
    } else {
        newElement.style.background = 'yellow'
    }
    document.getElementsByTagName('body')[0].appendChild(newElement)
    counter += 1
    count_txt.innerText = counter
})

dec_button.addEventListener('click',function(){
    counter -= 1
    count_txt.innerText = counter
    const removeElement = document.querySelector('[data-count="'+counter+'"]')
    if (removeElement) {
        removeElement.remove()
    }
})