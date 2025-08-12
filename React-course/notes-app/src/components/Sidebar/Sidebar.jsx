    import React from 'react'
    import NoteListItem from '../NoteListItem/NoteListItem'
    import './Sidebar.css'
    
    export default function Sidebar({ notes, ActiveNoteId: ActiveNoteId, onSelectNote }) {
      return (
        <div className='side-bar'>
            <h1>Notes</h1>
            <div className="note-items">
              {notes.map(note => (
              <NoteListItem
                key={note.id}
                note={note}
                isActive={note.id === ActiveNoteId}
                onClick={() => onSelectNote(note.id)}
              />
              ))}
            </div>
        </div>
      )
    }
    