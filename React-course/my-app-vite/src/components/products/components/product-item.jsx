
function Button() {
    return <div>
        <button>Click</button>
    </div>
}

function ProductItem ({item,key}){
    return <div key={key}>
        <li>{item}</li>
        <Button/>
    </div>
}

export default ProductItem