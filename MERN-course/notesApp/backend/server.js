import express from 'express'
import notesRoutes from './routes/notesRoutes.js'
import { connectDB } from './config/db.js'
import dotenv from 'dotenv'

dotenv.config({ path: '../.env' })

const app = express()

app.use(express.json())

app.use("/api/notes",notesRoutes)


app.listen(5000,(req,res)=>{
    connectDB()
    console.log("server running at http://localhost:5000")
})

