
const All_screen_btn = document.getElementById("All-btn")
const Active_screen_btn = document.getElementById("Active-btn")
const Completed_screen_btn = document.getElementById("Completed-btn")
const All_tasks_container = document.getElementById("All-tasks")
const Active_tasks_container = document.getElementById("Active-tasks")
const addTaskBtn = document.getElementById("addTask-btn")
const addTaskText = document.getElementById("newTask-input")

let currentlyActiveTasksContainer = All_tasks_container
let tasks = JSON.parse(localStorage.getItem("tasks")) || []
// localStorage.setItem("tasks",null)

displayTasks()

All_screen_btn.addEventListener("click" ,()=> {
    currentlyActiveTasksContainer.classList.remove("active")
    All_tasks_container.classList.add("active")
    currentlyActiveTasksContainer = All_tasks_container
    displayTasks()
})

Active_screen_btn.addEventListener("click" ,()=> {
    currentlyActiveTasksContainer.classList.remove("active")
    Active_tasks_container.classList.add("active")
    currentlyActiveTasksContainer = Active_tasks_container
    displayTasks()
})

addTaskBtn.addEventListener("click",()=> {
    tasks.push({
        text : addTaskText.value ,
        status : false
    })
    addTaskText.value = ""
    localStorage.setItem("tasks",JSON.stringify(tasks))
    displayTasks()
})

function displayTasks() {
    tasksToDisplay = []
    switch (currentlyActiveTasksContainer) {
        case All_tasks_container:
            tasksToDisplay = tasks
            break;
    
        case Active_tasks_container :
            tasksToDisplay = tasks.filter((task)=> task.status === false)
            break;
        }
        currentlyActiveTasksContainer.getElementsByTagName("ul")[0].innerHTML = ""
        tasksToDisplay.forEach(task => {
            child = createTaskChild(task)
            currentlyActiveTasksContainer.getElementsByTagName("ul")[0].appendChild(child)
        });
}

function createTaskChild(task) {
    const child = document.createElement("li");
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.status;
    checkbox.addEventListener("change", () => {
        markAsComplete(task);
    });

    const textNode = document.createTextNode(task.text);
    child.appendChild(checkbox);
    child.appendChild(textNode);
    return child;
}

function markAsComplete(_task) {
    const task = tasks.find(task => task.text === _task.text);
    if (task) {
        task.status = !task.status;
        localStorage.setItem("tasks", JSON.stringify(tasks));
        displayTasks();
    }
}
