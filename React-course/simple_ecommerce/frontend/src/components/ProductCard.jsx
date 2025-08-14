import { toaster } from '@/src/components/ui/toaster';
import useProductStore from '@/store/product';
import { Box, Heading, HStack, Icon, IconButton, Image } from '@chakra-ui/react'
import React from 'react'
import { MdEdit, MdDelete } from "react-icons/md";


export default function ProductCard({product}) {

    const {deleteProduct} = useProductStore()


    async function handleDeleteProduct() {
        const {success,message} = await deleteProduct(product._id)
        if (!success) {
            toaster.create({title: "Error", description: message, status: "error"})
        } else {
            toaster.create({title: "Success", description: message, status: "success"})
        }
    }
  return (
    <Box>
        <Image src={product.image} alt={product.name} h={48} w='full' objectFit='cover'/> 
        
        <Box p={4}>
            <Heading as={"h3"}>
                {product.name}
            </Heading>
            <p>${product.price}</p>
            <HStack spacing={2}>
                <IconButton>
                    <MdEdit />
                </IconButton>
                <IconButton onClick={handleDeleteProduct}>
                    <MdDelete />
                </IconButton>
            </HStack>
            
        </Box>
    </Box>
  )
}
