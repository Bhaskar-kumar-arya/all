import { Container, Heading, Input, VStack, Box } from '@chakra-ui/react'
import React, { useState } from 'react'
import  useProductStore  from '../store/product.js'

export default function CreatePage() {

    const [newProduct,setNewProduct] = useState({
        name:"",
        price:"",
        image:""
    })

    const {createProduct} = useProductStore()

    async function handleAddProduct() {
        console.log("Product Created:", newProduct);
        const {success,message,data} = await createProduct(newProduct)
        console.log("Response:", {success, message, data});
        setNewProduct({ name: "", price: "", image: "" }); // Reset form after submission
    }

  return (
    <Container maxW={"sm"}>
        <VStack>
            <Heading>Create Product</Heading>
            <Box w={"full"}>
                <VStack>
                    <Input placeholder='product name' name='name' value={newProduct.name} onChange={(e)=>setNewProduct({...newProduct,name:e.target.value})}/>
                    <Input placeholder='product price' name='price' value={newProduct.price} onChange={(e)=>setNewProduct({...newProduct,price:e.target.value})}/>
                    <Input placeholder='product image' name='image' value={newProduct.image} onChange={(e)=>setNewProduct({...newProduct,image:e.target.value})}/>
                    <Input type='submit' value='Create Product' onClick={handleAddProduct}/>
                </VStack>
            </Box>
        </VStack>
    </Container>
  )
}
