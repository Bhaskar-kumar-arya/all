import ProductItem from "./components/product-item"
import './style.css'

const dummData = ["p1","p2","p3"]
  

function ProductList ({items}) {
    return (
    <div>
        <h1 className="title">E-commerce project</h1>   
        <ul>
            { 
                items.map((item,index)=><ProductItem item={item} key={index} />)
            }          
        </ul>
    </div>
    )
}


export default ProductList 