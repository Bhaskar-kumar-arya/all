import React, { useState } from 'react'

export default function ToDoForm({setTasks}) {
  const [task,setTask] = useState("")

  function HandleonClick () {
    setTasks(t=>[...t,{id : t[t.length-1].id + 1,completed : false,text : task}])
    setTask("")
  }

  function handleKeyDown(e) {
    if (e.key === "Enter") {
      HandleonClick()
    }
  }
  return (
    <div className='to-do-form'>
        <input onKeyDown={handleKeyDown} type="text" value={task} onChange={(e)=>{setTask(e.target.value)}} placeholder='add your task from here' />
        <button onClick={HandleonClick}>Add</button>
    </div>
  )
}
