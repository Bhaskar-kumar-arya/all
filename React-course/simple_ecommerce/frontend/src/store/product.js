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
    }  
}))

export default useProductStore;

