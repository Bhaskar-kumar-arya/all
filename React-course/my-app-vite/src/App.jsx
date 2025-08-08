import './App.css'
import ProductList from './components/products'

const App = () => {
  return (
    <div>
      <ProductList items = {["p1","p2","p3"]} />
    </div>
  )
}

export default App
