import useNoteStore from '../../store/note'
import NoteCard from '../../components/NoteCard'
import './HomePage.css'
import { Link } from 'react-router-dom'

export default function HomePage() {

    const {notes} = useNoteStore()

  return (
    <div className="home-page">
        <header>
            <h2>Think Board</h2>
            <Link to={"/create-note"}><button>Create Note</button></Link>
        </header>
        <div className="grid">
            {notes.map((note)=> <NoteCard note={note}/>)}
        </div>
    </div>
  )
}
