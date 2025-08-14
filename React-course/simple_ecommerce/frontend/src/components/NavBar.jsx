import { Button, Container, Flex, HStack, Text } from '@chakra-ui/react'
import React from 'react'
import { Link } from 'react-router-dom'
import { CiSquarePlus } from "react-icons/ci";
import { useColorMode, useColorModeValue } from './ui/color-mode';


export default function NavBar() {

  const {colorMode,toggleColorMode} = useColorMode()

  return (
    <Container maxW={"1200px"} alignItems={"center"} justifyContent={"center"} px={4} bg={useColorModeValue("gray.100","gray.900")}>
      <Flex h={16} alignItems={"center"} justifyContent={"space-between"} flexDir={{base:"column",sm:"row"}}>
        <Link to={"/"}>Product Store</Link>
        <HStack>
          <Link to={"/Create"}>
            <Button>
              <CiSquarePlus/>
            </Button>
          </Link>
          <Button onClick={toggleColorMode}>
            {colorMode === "light"?  "Light" : "Dark"} 
          </Button>
        </HStack>
      </Flex>
    </Container> 
  )
}
