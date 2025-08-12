import { useState } from 'react'
import Home from "./pages/Home"
import About from "./pages/About"
import Users from "./pages/Users"
import UserDetails from "./pages/UserDetails"
import UsersLayout from "./pages/UsersLayout"
import UsersList from "./pages/UsersList"
import NotFound from "./pages/NotFound"
import { BrowserRouter, Routes, Route, Link } from "react-router-dom"
import './App.css'

function App() {

  

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element = {<Home/>}/>
        <Route path='/about' element = {<About/>}/>
        <Route path='/users' element = {<UsersLayout/>}>   
          <Route index element={<UsersList/>}/>     
          <Route path=':id' element = {<UserDetails/>}/>
        </Route>
        <Route path='*' element = {<NotFound/>}/>
      </Routes>   

      <nav>
        <Link to={'/'}>Home</Link>
        <Link to={'/about'}>About</Link>
        <Link to={'/users'}>Users</Link>
      </nav>

    </BrowserRouter>
  )
}

export default App
