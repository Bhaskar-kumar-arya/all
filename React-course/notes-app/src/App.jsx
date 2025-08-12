import { useEffect, useState } from 'react'
import './App.css'
import Sidebar from  './components/Sidebar/Sidebar'
import NodeEditor from './components/NoteEditor/NoteEditor'

function App() {

  const [ActiveNoteId,setActiveNoteId] = useState(1)

  const [notes,setNotes] = useState([
    {
      id : 1,
      title:"t1",
      text:"text for this note hehe haha......",
    },
    {
      id : 2 ,
      title:"t2",
      text:"text for the second note hehe haha......",
    }
  ])
  
  const activeNote = notes.find(note=>note.id === ActiveNoteId)

    function updateNote(updatedNote) {
    setNotes(prevNotes =>
      prevNotes.map(note => (note.id === updatedNote.id ? updatedNote : note))
    );
  }

  return (
    <>
      <div className="main-container">
        <Sidebar ActiveNoteId = {ActiveNoteId} notes={notes} onSelectNote = {setActiveNoteId}/>
        <div className="editor">
          <NodeEditor note = {activeNote} onUpdateNote = {updateNote}/>
        </div>
      </div>
    </>
  )
}

export default App
