import React from 'react'

export default function TaskInput({new_task,handleInputChange,addTask}) {
  return (
    <form onSubmit={addTask}>
        <input type="text" value={new_task} onChange={handleInputChange} />
        <button type="submit">Add</button>
    </form>
  )
}
