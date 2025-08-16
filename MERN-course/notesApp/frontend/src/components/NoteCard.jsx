import React from 'react'
import { Link } from 'react-router-dom'
import useNoteStore from '../store/note'


export default function NoteCard({note}) {

  const {deleteNote} = useNoteStore()
  async function handleDelete() {
    const response = await deleteNote(note._id)
  }

  return (
    <div className="note-card">
        <h3>{note.title}</h3>
        <p>{note.content}</p>
        <footer>
            <span>day/date</span>
            <div className="buttons">
                <Link to={`/note/${note._id}`}><button>Edit</button></Link>
                <button onClick={handleDelete}>Delete</button>
            </div>
        </footer>
    </div>
  )
}
