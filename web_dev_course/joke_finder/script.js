function generateJoke () {
    return fetch('https://official-joke-api.appspot.com/random_joke').then(response => {
    return response.json()
})
}

const generateJoke_btn = document.getElementById('generateJoke_btn') 
generateJoke_btn.addEventListener('click',() => {
    generateJoke().then(data => {
        const joke_txt = document.createElement('div') 
        joke_txt.innerText = data.setup + data.punchline
        document.getElementsByTagName('body')[0].appendChild(joke_txt)
    })
})