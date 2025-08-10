import React from 'react'

export default function TasksLists({tasks,removeTask}) {
  return (
    <ul>
        {
          tasks.map((task,index)=><li key={index}>{task} <button onClick={()=>{removeTask(index)}}>Remove</button></li>)
        }
      </ul>
  )
}
