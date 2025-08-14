import Product from '../models/product.model.js'
import mongoose from 'mongoose'

export const getProducts = async (req,res)=> {
    try {
        const products = await Product.find({})
        res.status(200).json({success:true,data:products})
    } catch (error) {
        console.error(error)
        res.status(500).json({success:false,message:"Internal server error"})
    }
}

export const createProduct = async (req,res)=>{
    const product = req.body

    if (!product.name || !product.price || !product.image) {
        return res.status(400).json({success:false,message:"Please fill all the fields"})
    }

    const newProduct = new Product(product)

    try {
        await newProduct.save()
        return res.status(201).json({success:true,message:"Product created successfully",data:newProduct})
    } catch (error) {
        console.error(error)
        return res.status(500).json({success:false,message:"Internal server error"})
    }
}

export const updateProduct = async (req,res)=>{
    const {id} = req.params

    const product = req.body

    if (!mongoose.Types.ObjectId.isValid(id)) {
        return res.status(404).json({success:false,message:"product not found"})
    }

    try {
        const updatedProduct = await Product.findByIdAndUpdate(id,product,{new:true})
        res.status(200).json({success:true,message:"updated product..",data:updatedProduct})
    } catch (error) {
        res.status(500).json({success:true,message:error})
    }
}

export const deleteProduct = async (req,res)=> {
    const {id} = req.params

    if (!mongoose.Types.ObjectId.isValid(id)) {
        return res.status(404).json({success:false,message:"product not found"})
    }

    try {
        await Product.findByIdAndDelete(id)
        res.status(200).json({success:true,message:"Product deleted successfully"})
    } catch (error) {
        res.status(500).json({success:false,message:"server error: " + error})
    }
}