
import json
from datetime import datetime
import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ToDoListData.json")
class Task :  
    """A class to represent a task."""
    def __str__(self):
        return f"id : {self.id} {self.description} [{self.completed}]"
    def __repr__(self):
        return f"Task(description={self.description}, completed={self.completed})"
    def __init__(self,Description,id = -1): 
        self.description = Description
        self.completed = False
        self.id = datetime.now().strftime("%Y%m%d%H%M%S%f") if id == -1 else str(id)
    def toDictItem (self) :
        return  {"description" : self.description , "completed" : f"{self.completed}"}

    


def loadData () -> dict :
    try :
        with open(file_path,"r") as file :
            return json.load(file)
    except FileNotFoundError :
            with open(file_path,"w") as file :
                file.write('{"tasks" : {}}')

            return loadData()
    
        
def saveData (data) :
    with open(file_path,"w") as file :
        json.dump(data,file,indent=4)

def AddTask (description) :
    data = loadData()
    task = Task(description)
    data["tasks"][task.id] = task.toDictItem()
    saveData(data)

def updateTaskDataFromId (id: int) :
    tasks = loadData()["tasks"]
    
          
def viewTasks () :
    print(f"toDoList : showing tasks")
    tasks = loadData()["tasks"]
    print(f"toDoList : tasks : {tasks}")
    result = ""
    for id,values in tasks.items() :
        result += (f"id : {id} task : {values['description']} --> {'Completed' if values['completed'] == 'True' else 'Incomplete'}" )
    return result    

def markTaskAsComplete (id : str) :
    data = loadData()
    tasks = data["tasks"]
    tasks[id]["completed"] = "True"
    saveData(data)
    

# def main() :
#     while True :    
#         print("Options:")
#         print("1. view task")
#         print("2. create task")
#         print("3. mark task as complete")
#         response = input("What do you want to do ?\n")
#         if response == "1" :
#             viewTasks()
#         elif response == "2" :
#             AddTask(input("describe the task : "))   
#         elif response == "3" :
#             markTaskAsComplete(input("enter ID : "))    
#         else :
#             print("Invalid option, please try again.")
    

# if __name__ == "__main__":
#     main()