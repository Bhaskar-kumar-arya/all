import { timeStamp } from 'console'
import mongoose from 'mongoose'
import { type } from 'os'

const itemSchema = mongoose.Schema({
    description : {
        type: String,
        required: true
    },
    completed: {
        type: Boolean,
        default: false
    }
},{timeStamps: true})

const Item = mongoose.model('Item',itemSchema)

export default Item