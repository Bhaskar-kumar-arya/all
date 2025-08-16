import { data } from 'react-router-dom'
import {create} from 'zustand'

const useNoteStore = create((set)=>({
    notes : [],
    fetchNotes : async ()=> {
        const response = await fetch("/api/notes")
        const data = await response.json()
        console.log(data.data)
        set({notes:data.data})
    },
    setNotes : (notes) => set({notes:notes}),
    createNote : async (noteData) => {
        const response = await fetch("/api/notes",{
            method: "POST",
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify(noteData)
        })
        const data = await response.json()
        if (!data.success) {
            console.error("Failed to create note:", data.message);
            return {success: false, message: data.message};
        }
        set((state)=> ({notes: [...state.notes, data.data]}))
        return {success: true, message: "Note created successfully", data: data.data}
    },
    updateNote : async (id,updatedData) => {
        const response = await fetch(`/api/notes/${id}`,{
            method:"PUT",
            headers: {
                "Content-type" : "application/json"
            },
            body: JSON.stringify(updatedData)
        })
        const data = await response.json()
        if (!data.success) {
            console.error("Failed to update note:", data.message);
            return {success: false, message: data.message};
        }
        set((state) => ({
            notes: state.notes.map((note) => note._id === id ? data.data : note)
        }))
        return {success: true, message: "Updated", data: data.data}
    },
    deleteNote : async (id) => {
        const response = await fetch(`/api/notes/${id}`,{
            method: "DELETE"
        })
        const data = await response.json()
        if (!data.success) {
            console.error("Failed to delete note:", data.message);
            return {success: false, message: data.message};
        }
        set((state) => ({
            notes: state.notes.filter((note) => note._id !== id)
        }))
        return {success: true, message: "Note deleted successfully"}
    }
}))

export default useNoteStore