import React, { useEffect, useState } from "react";
import { Link, useParams, useNavigate } from "react-router-dom";
import "./NoteDetailPage.css";
import useNoteStore from "../../store/note";

const NoteDetailPage = () => {
  const { id } = useParams();
  const { notes,updateNote } = useNoteStore();
  const note = notes.filter((item) => item._id === id)[0];
  const [_note, set_Note] = useState(note);
  const navigate = useNavigate()


  async function handleSave() {
    const response = await updateNote(_note._id,_note)
    console.log(response)
    navigate("/")
  }

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    set_Note((prev) => ({ ...prev, [name]: value }));
  };

  return (
    <div className="note-detail-page">
      <header>
        <input
          name="title"
          className="note-title-input"
          value={_note.title}
          onChange={handleInputChange}
        />
        <Link to="/" className="back-button">
          Back to Home
        </Link>
      </header>
      <main>
        <textarea
          name="content"
          className="note-content-input"
          value={_note.content}
          onChange={handleInputChange}
        />
      </main>
      <footer>
        <span>Created on: 2023-10-27</span>
        <div className="buttons">
          <button onClick={handleSave}>Save</button>
          <button>Delete</button>
        </div>
      </footer>
    </div>
  );
};

export default NoteDetailPage;
