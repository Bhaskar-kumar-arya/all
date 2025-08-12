import React, { act } from 'react'
import './NoteListItem.css'

export default function NoteListItem({ note, isActive, onClick }) {

  return (
    <div 
    onClick={()=>{onClick()}} 
    className={isActive === true ? "item active" : "item"}>
        {note.title || "Untitled Note"}
    </div>
  )
}
