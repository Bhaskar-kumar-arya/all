import express from 'express'
import dotenv from 'dotenv'
import { connectDB } from './config/db.js'
import Item from './models/item.model.js'
import mongoose from 'mongoose'

dotenv.config()

const app = express()

app.use(express.json()) // Middleware to parse JSON bodies

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.get('/api/items', async (req, res) => {
    const items = await Item.find({})
    res.status(200).json({success:true,data:items})
})

app.post('/api/items', async (req,res) => {
    const {description} = req.body
    if (!description) {
        return res.status(400).json({success:false,message:"Description is required"})
    }
    const newItem = new Item({description})
    try {
        await newItem.save()
        res.status(201).json({success:true,data:newItem})
    } catch (error) {
        res.status(500).json({success:false,message:"Internal server error"})
    }
})

app.put('/api/items/:id', async (req,res)=>{
    const {id} = req.params
    if (!mongoose.Types.ObjectId.isValid(id)) {
        return res.status(404).json({success:false,message:"Item not found"})
    }
    try {
        const updatedItem = await Item.findByIdAndUpdate(id,req.body,{new:true})
        res.status(200).json({success:true,data:updatedItem})
    } catch (error) {
        res.status(500).json({success:false,message:"Internal server error"})
    }
})

app.delete('/api/items/:id', async (req,res) => {
    const {id} = req.params
    if (!mongoose.Model.ObjectId.isValid(id)) return res.status(404).json({success:false,message:"Item not found"})
    try {
        const res = await Item.findByIdAndDelete(id)
        res.status(200).json({success:true,message:"Item deleted successfully"})
    } catch (error) {
        res.status(500).json({success:false,message:"Internal server error"})
    }
})

app.listen(5000,()=>{
    connectDB()
    console.log(`server running at http://localhost:5000`)
})