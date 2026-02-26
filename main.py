from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    completed: bool

tasks = [
    # {"id": 1, "title": "Learn FastAPI", "completed": False},
    # {"id": 2, "title": "Build AI API", "completed": False}
]

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task.model_dump())
    return {"message": "Task created", "task": task}


@app.get("/")
def home():
    return {"message": "Task Manager API"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}

@app.get("/tasks/filter")
def filter_tasks(completed: bool):
    filtered = [task for task in tasks if task["completed"] == completed]
    return {"filtered_tasks": filtered}

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