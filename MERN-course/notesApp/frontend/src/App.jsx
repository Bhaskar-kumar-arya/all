import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Route, Routes } from 'react-router-dom'
import useNoteStore from './store/note.js'
import HomePage from './pages/HomePage/HomePage.jsx'
import NoteDetailPage from './pages/NoteDetailPage/NoteDetailPage.jsx'
import CreateNotePage from './pages/CreateNotePage/CreateNotePage.jsx'

function App() {
  const {fetchNotes,notes} = useNoteStore()

  useEffect(()=>{
    fetchNotes()
  },[fetchNotes])

  return (
    <>
      <Routes>
        <Route path='/' element={<HomePage/>}/>
        <Route path='/note/:id' element={<NoteDetailPage/>}/>
        <Route path='/create-note' element={<CreateNotePage/>}/>
      </Routes>
    </>
  )
}

export default App
