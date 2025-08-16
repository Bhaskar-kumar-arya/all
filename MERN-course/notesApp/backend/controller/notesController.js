import Note from '../models/note.model.js'

export const getAllNotes = async (req,res)=> {
    const response = await Note.find({})
    res.status(200).json({success:true,data:response})
}


export const createNote = async (req,res) => {
    const newItem  = new Note(req.body)
    const response = await newItem.save()
    res.status(201).json({success:true,data:response})
}

export const deleteNote = async (req,res)=> {
    const {id} = req.params
    const response = await Note.findByIdAndDelete(id)
    res.json({success: true,response:response})
}

export const updateNote = async (req,res) => {
    const {id} = req.params
    const response = await Note.findByIdAndUpdate(id,req.body, {new: true})
    if(!response) {
        return res.status(404).json({success: false, message: 'Note not found'})
    }
    res.status(200).json({success: true, data: response})
}