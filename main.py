from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Task API",
    version="1.0",
    description="A simple CRUD API for managing tasks."
)

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health_check():
    return {"status": "ok"}

class Task(BaseModel):
    title: str
    done: bool = False

class TaskResponse(Task):
    id: int

tasks_db = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Finish FlyRank assignment", "done": False},
    {"id": 3, "title": "Read a book", "done": True}
]
next_id = 4

@app.get("/tasks", response_model=List[TaskResponse])
def get_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: Task):
    global next_id
    if not task.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")
        
    new_task = {"id": next_id, "title": task.title, "done": task.done}
    tasks_db.append(new_task)
    next_id += 1
    return new_task

@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: Task):
    for t in tasks_db:
        if t["id"] == task_id:
            if not task.title.strip():
                raise HTTPException(status_code=400, detail="Title cannot be empty")
            t["title"] = task.title
            t["done"] = task.done
            return t
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for i, t in enumerate(tasks_db):
        if t["id"] == task_id:
            del tasks_db[i]
            return
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
