import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './CreateNotePage.css';
import useItemStore from '../../store/note.js'


const CreateNotePage = () => {
  const [title,setTitle] = useState("")
  const [content,setContent] = useState("")
  const {createNote} = useItemStore()
  const navigate = useNavigate()

  async function handleSubmit(e) {
    e.preventDefault()
    const response = await createNote({title,content})
    navigate("/")
  }

  return (
    <div className="create-note-page">
      <header>
        <h1>Create a New Note</h1>
        <Link to="/" className="back-button">Back to Home</Link>
      </header>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="title">Title</label>
          <input type="text" value={title} onChange={(e)=>{setTitle(e.target.value)}} id="title" name="title" />
        </div>
        <div className="form-group">
          <label htmlFor="content">Content</label>
          <textarea id="content" name="content" rows="10" value={content} onChange={(e)=>{setContent(e.target.value)}}></textarea>
        </div>
        <button type="submit">Create Note</button>
      </form>
    </div>
  );
};

export default CreateNotePage;