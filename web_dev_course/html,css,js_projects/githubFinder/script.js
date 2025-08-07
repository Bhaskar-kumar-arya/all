const searchInput = document.getElementById("search") 
const searchBTN = document.getElementById("search-btn")
const avatarImg = document.getElementById("avatar")
const username = document.getElementById("username")


const BASE_URL =  "https://api.github.com/users/"

async function getUserData(user) {
    const response = await fetch(BASE_URL+user,{
        headers : {
            Authorization : `token ${token}`
        },
    })
    if (!response.ok) {
        console.error("Error:", response.status, await response.text());
        return;
    }
    const data = await response.json()
    return data
}

searchBTN.addEventListener("click",onSearch)
searchInput.addEventListener("keydown",function(event) {
    if (event.key === "Enter") {
        onSearch()
    }
})

async function onSearch () {
    data = await getUserData(searchInput.value)
    console.log(data)
    const avatar_url = data.avatar_url
    const created_at = data.created_at
    const followers = data.followers
    const following = data.following
    const public_repos = data.public_repos
    const repos_response = await fetch(BASE_URL + searchInput.value + "/repos",{
        headers : {
            Authorization : `token ${token}`
        },
    })
    const repos_list = await repos_response.json()
    console.log(repos_list)
    avatarImg.setAttribute("src",avatar_url)
    username.textContent = data.login
}
