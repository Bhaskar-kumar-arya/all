const balanceEl = document.getElementById("balance");
const incomeAmountEl = document.getElementById("income-amount");
const expenseAmountEl = document.getElementById("expense-amount");
const transactionListEl = document.getElementById("transaction-list");
const transactionFormEl = document.getElementById("transaction-form");
const descriptionEl = document.getElementById("description");
const amountEl = document.getElementById("amount");

// localStorage.setItem("transactions",JSON.stringify([]))
let transactions =  JSON.parse(localStorage.getItem("transactions")) || []
transactionFormEl.addEventListener("submit",addTransaction) 
updateTransactionList()
updateSummary()
function addTransaction(e) {
    e.preventDefault()
    const description = descriptionEl.value.trim()
    const amount = parseFloat(amountEl.value)
    console.log(description,amount)
    transactions.push({
        id : Date.now(),
        description,
        amount
    })
    localStorage.setItem("transactions",JSON.stringify(transactions))
    console.log(transactions)
    updateTransactionList()
    updateSummary()
    transactionFormEl.reset()
}  

function updateTransactionList() {
    transactionListEl.innerHTML = ""

    const sortedTransactions = [...transactions].reverse()

    sortedTransactions.forEach((transaction)=> {
       const transactionEl =  createTransactionElement(transaction)
       transactionListEl.appendChild(transactionEl)
    })
}

function createTransactionElement(transaction) {
    const li = document.createElement("li")
    li.classList.add("transaction")
    li.classList.add(transaction.amount > 0 ? "income" : "expense")

    li.innerHTML = `
    <span>${transaction.description} </span>
    <span>${formatCurrency(transaction.amount)} 
        <button class = "delete-btn" onclick = "removeTransaction(${transaction.id})">X</button>
    </span>
    `
    return li
}

function updateSummary() {
    const balance = transactions.reduce((a,b)=> a + b.amount,0)
    const income = transactions.filter(transaction => transaction.amount > 0 ).reduce((a,b)=> a + b.amount ,0)
    const expense = transactions.filter(transaction => transaction.amount < 0 ).reduce((a,b)=> a + b.amount ,0)

    balanceEl.textContent = formatCurrency(balance)
    incomeAmountEl.textContent = formatCurrency(income)
    expenseAmountEl.textContent = formatCurrency(expense)
}

function formatCurrency (number) {
    return new Intl.NumberFormat("en-US",{
        style : "currency",
        currency : "USD"
    }).format(number)
}

function removeTransaction (id) {
    transactions = transactions.filter(transaction => transaction.id !== id)
    localStorage.setItem("transactions",JSON.stringify(transactions))
    updateTransactionList()
    updateSummary()
}