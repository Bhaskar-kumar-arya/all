import express from 'express'
import { createNote, getAllNotes, deleteNote, updateNote } from '../controller/notesController.js'

const router = express.Router()

export default router

router.get("/",getAllNotes)

router.post("/",createNote)

router.delete("/:id",deleteNote)

router.put("/:id",updateNote)