import { useEffect, useState } from 'react'
import './App.css'
import Header from './Components/Header'
import ToDoForm from './Components/ToDoForm'
import Footer from './Components/footer'
import ToDoList from './Components/ToDoList'
import useItemStore from './store/item'

function App() {

  const {items,fetchItems,updateItem,createItem} = useItemStore()

  useEffect(()=>{
    fetchItems()
  },[fetchItems])

  const [Tasks,setTasks] = useState([

    {
      id : 1 ,
      completed : false,
      text : "task 01 is speaking"
    },
    {
      id : 2 ,
      completed : false,
      text : "task 02 is speaking"
    },
    {
      id : 3 ,
      completed : true,
      text : "task 03 is speaking"
    }

  ])
  // useEffect(()=>{
  //   console.log(Tasks)
  // },[Tasks])
  return (
    <>
      <Header/>
      <ToDoForm createItem={createItem}/>
      <ToDoList Tasks = {items} updateItem={updateItem} />
      <Footer/>
    </>
  )
}

export default App
