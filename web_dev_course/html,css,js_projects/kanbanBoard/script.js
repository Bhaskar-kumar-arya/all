const cards = document.querySelectorAll(".card")
const lists = document.querySelectorAll(".list")
for (const card of cards) {
    card.addEventListener("dragstart",dragstart)
    card.addEventListener("dragend",dragend)
}

for (const list of lists) {
    list.addEventListener("dragover",dragover)
    list.addEventListener("drop",drop)
    list.addEventListener("dragenter",dragenter)
    list.addEventListener("dragleave",dragleave)
}

function dragstart(event) {
    event.dataTransfer.setData("text/plain",this.id)
}

function dragend(event) {
    console.log("dragend")
}

function dragover(event) {
    event.preventDefault()
}

function dragenter(event) {
    event.preventDefault()
    this.classList.add("over")
}

function drop(event) {
    const id = event.dataTransfer.getData("text/plain")
    const card = document.getElementById(id)
    this.appendChild(card)
    this.classList.remove("over")

}

function dragleave (event) {
    this.classList.remove("over")
}