# Task API - FlyRank W2

A simple CRUD API for managing tasks built with FastAPI.

## Run Instructions
1. Install dependencies: `pip install fastapi uvicorn`
2. Start the server: `uvicorn main:app --reload`
3. View the interactive Swagger UI at: `http://localhost:8000/docs`

## Endpoints
| Operation | Method | Endpoint | Meaning |
|---|---|---|---|
| Create | POST | `/tasks` | Add a new task |
| Read | GET | `/tasks` | List all tasks |
| Read | GET | `/tasks/{task_id}` | Get a specific task |
| Update | PUT | `/tasks/{task_id}` | Change a task |
| Delete | DELETE | `/tasks/{task_id}` | Remove a task |

## Curl Test Output
