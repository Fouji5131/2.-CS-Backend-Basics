from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    complete: bool = False

class Task(TaskCreate):
    id: int

tasks = [
    # {"id": 1, "title": "Learn FastAPI", "completed": False},
    # {"id": 2, "title": "Build AI API", "completed": False}
]

@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        **task.model_dump()
    }
    tasks.append(new_task)
    return {"message": "Task created", "task": new_task}


@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskCreate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["completed"] = updated_task.completed
            return task
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}



@app.get("/")
def home():
    return {"message": "Task Manager API"}

# @app.get("/tasks/{task_id}")
# def get_task(task_id: int):
#     for task in tasks:
#         if task["id"] == task_id:
#             return task
#     return {"error": "Task not found"}

# @app.get("/tasks/filter")
# def filter_tasks(completed: bool):
#     filtered = [task for task in tasks if task["completed"] == completed]
#     return {"filtered_tasks": filtered}

# @app.get("/")
# def home():
#     return {
#         "message": "Hello, AI backend world!"
#     }

# @app.get("/about")
# def about():
#     return {
#         "name": "Abdullah",
#         "goal": "AI Engineer"
#     }

# @app.get("/square/{number}")
# def square(number: int):
#     return {
#         "number": number,
#         "square": number * number
#     }