const promiseObject = fetch('data.json')

promiseObject.then((response)=> {
    return response.json()
}).then(finalData => {
    console.log(finalData)
})