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
bash
curl -i http://localhost:8000/tasks
HTTP/1.1 200 OK
server: uvicorn
content-length: 154
content-type: application/json

[{"title":"Buy milk","done":false,"id":1},{"title":"Finish FlyRank assignment","done":false,"id":2},{"title":"Read a book","done":true,"id":3}]
