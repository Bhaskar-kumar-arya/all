import { set } from "lodash";
import { data } from "react-router-dom";
import { create } from "zustand";

const useProductStore = create((set) => ({
    products:[],
    setProducts: (products) => set({products}),
    createProduct: async (newProduct) => {
        if (!newProduct.name || !newProduct.price || !newProduct.image) {
            console.error("All fields are required to create a product.");
            return {success:false, message:"All fields are required"};
        }
        const response = await fetch('/api/products',{
            method: 'POST',
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify(newProduct)
        })
        const data = await response.json()
        set((state) => ({products: [...state.products,data.data]}))
        return {success: true,message:"Product created successfully", data:data.data}
    },
    fetchProducts : async ()=> {
        const res = await fetch("/api/products")
        const data = await res.json()
        set({products:data.data})
    },
    deleteProduct: async (pid) => {
        const res = await fetch(`/api/products/${pid}`,{
            method : "DELETE",
        })
        const data = await res.json()
        if (!data.success) return {success:false,message: data.message}
        set(state=> ({products:state.products.filter(product=>product._id !== pid)}))
        return {success:true,message:"Product deleted successfully"}
    },
    updateProduct : async (pid,newProduct) => {
        const res = await fetch(`/api/products/${pid}`,{
            method: "PUT",
            headers: {
                "Content-type": "application/json"
            },
            body : JSON.stringify(newProduct)
        })
        const data = await res.json()
        if (!data.success) return {success:false,message: data.message}
        set(state=>({products:[...state.products.filter(p=>p._id !== pid),data.data]}))
        return {success:true,message:data.message,data: data.data}
    }
}))

export default useProductStore;

