import React, { useEffect, useState } from 'react'

export default function ToDoList({Tasks,updateItem}) {

    function handleChecker(task) {
        updateItem(task._id,{completed : !task.completed})
    }
    const [currentScreen,setCurrentScreen] = useState(1)

    useEffect(()=>{
        if (currentScreen === 3) {
            setCurrentScreen(2)
        }
    },[Tasks])

  return (
    <div className='ToDoList'> 
        <div className="categories">
            <div onClick={()=>{setCurrentScreen(1)}} className={currentScreen === 1 ? "category active" : "category"}>All</div>
            <div onClick={()=>{setCurrentScreen(2)}} className={currentScreen === 2 ? "category active" : "category"}>Active</div>
            <div onClick={()=>{setCurrentScreen(3)}} className={currentScreen === 3 ? "category active" : "category"}>Completed</div>
        </div>

        <ul className= {currentScreen === 1 ? "items active" : "items"} id='All'>
            {
                Tasks.map((task)=><li key={task._id}><input onChange={()=>{handleChecker(task)}} checked = {task.completed === true ? true : false} type="checkbox"/> {task.description}</li>)
            }
        </ul>

        <ul className= {currentScreen === 2 ? "items active" : "items"} id='Active'>
            {
                Tasks.filter(task=>task.completed === false).map(task=><li key={task._id}><input onChange={()=>{handleChecker(task)}} checked = {task.completed === true ? true : false} type="checkbox"/> {task.description}</li>)
            }
        </ul>

        <ul className= {currentScreen === 3 ? "items active" : "items"} id='Completed'>
            {
                Tasks.filter(task=>task.completed !== false).map(task=><li key={task._id}><input onChange={()=>{handleChecker(task)}} checked = {task.completed === true ? true : false} type="checkbox"/> {task.description}</li>)
            }
        </ul>
    </div>
  )
}
