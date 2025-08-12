import React, { useState } from 'react'
import './NoteEditor.css'

export default function NoteEditor({note,onUpdateNote}) {

  function handleTitleChange(e) {
    onUpdateNote({ ...note, title: e.target.value });
  }

  function handleBodyChange(e) {
    onUpdateNote({ ...note, text: e.target.value });
  }

  return (
    <div className='editor'>
        <h1>Note Editor</h1>
        <textarea value={note.text} onChange={handleBodyChange}/>
    </div>
  )
}
