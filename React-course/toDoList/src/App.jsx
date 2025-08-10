import { useState } from "react"
import TaskInput from "./components/TaskInput"
import { add } from "lodash"
import TasksLists from "./components/TasksLists"


function App() {

  const [new_task,setTask] = useState("")

  const [tasks,setTasks] = useState(['t1','t2'])

  function handleInputChange(e) {
    setTask(e.target.value)
  }

  function addTask (e) {
    e.preventDefault()
    setTasks(t=>[...t,new_task])
    setTask("")
  }

  function removeTask(index) {
    setTasks(t=>t.filter((task,i)=>i !== index))
  }

  return (
    <>
      <TaskInput new_task={new_task} handleInputChange={handleInputChange} addTask={addTask}/>
      <TasksLists tasks={tasks} removeTask={removeTask}/>
    </>
  )
}    

export default App
