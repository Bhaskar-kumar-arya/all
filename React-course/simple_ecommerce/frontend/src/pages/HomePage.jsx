import ProductCard from '@/components/ProductCard'
import useProductStore from '@/store/product'
import { Button, Container, SimpleGrid, VStack } from '@chakra-ui/react'
import React, { useEffect } from 'react'
import { Link } from 'react-router-dom'

export default function HomePage() {
  const {fetchProducts,products,updateProduct} = useProductStore()
  useEffect(()=>{
    fetchProducts()
  },[fetchProducts])

  console.log(products)
  return (
    <Container maxW='container.x1' py={12}>
      <VStack spacing = {8}>
        <div>Products</div>

        <SimpleGrid columns={{base:1,md:1,lg:3}} spacing={10} w={"full"}>
          {products.map((product)=> <ProductCard key = {product._id} product = {product} />)}
        </SimpleGrid>

        {products.length ===0 ? <div>No Products found! <Link style={{color:"blue"}} to={"/create"}>Click to create one</Link></div> : ""}
      </VStack>
      <Button onClick={async ()=>{
        const res = await updateProduct("689cb6de040843261a9fa104",{name:"newName",price:"00"})
        console.log(res)
      }}>Update</Button>
    </Container>
  )
}
