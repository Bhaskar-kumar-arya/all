import {create} from 'zustand'

const useItemStore = create((set) => ({
    items : [],
    setItems: (items) => set({items: items}),
    createItem : async (newItem) => {
        if (!newItem.description) {
            console.error("Description is required to create an item.");
            return {success: false, message: "Description is required"};
        }
        const response = await fetch('/api/items',{
            method : "POST",
            headers: {
                "Content-type" : "application/json"
            },
            body : JSON.stringify(newItem)
        })
        const data = await response.json()
        set((state) => ({items: [...state.items,data.data]}))
        return {success: true, message: "Item created successfully", data: data.data}
    },
    fetchItems : async () => {
        const res = await fetch("/api/items")
        const data = await res.json()
        if (!data.success) {
            console.error("Failed to fetch items:", data.message);
            return;
        }
        set({items: data.data})
    },
    deleteItem : async (id) => {
        const res = await fetch(`/api/items/${id}`,{
            method : "DELETE",
        })
        const data = await res.json()
        if (!data.success) return {success: false, message: data.message}
        set(state => ({items: state.items.filter(item => item._id !== id)}))
        return {success: true, message: "Item deleted successfully"}
    },
    updateItem : async (id,item) => {
        const res = await fetch(`/api/items/${id}`,{
            method: "PUT",
            headers : {
                "Content-type" : "application/json"
            },
            body: JSON.stringify(item)
        })
        const data = await res.json()
        if (!data.success) return {success:false,message:data.message}
        set((state)=>({items:state.items.map((i)=> i._id === id ? data.data : i )}))
        return {success:true,message:"Item updated successfully", data: data.data}
    }
}))

export default useItemStore