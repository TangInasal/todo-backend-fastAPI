# To-Do Application with React and FastAPI

---

## Setup installaion

#### Clone repository
'git clone https://github.com/TangInasal/todo-backend-fastAPI.git'

#### Install requirements
'pip install -r requirements.txt'

#### Run dev server
'uvicorn main:app --host 0.0.0.0 --port 8000'

---

## API Endpoints
FastAPI endpoints for managing managing backend:



| Method | Endpoint                                      | Description                |
|--------|----------------------------------------------|----------------------------|
| GET    | `/todos/`                            | Fetch all tasks            |
| POST   | `/todos/`                            | Create a new task          |
| PUT    | `/todos/<id>/` (e.g., `/todos/2/`) | Update a task by ID        |
| DELETE | `/todos/<id>/` (e.g., `/todos/2/`) | Delete a task by ID        |

- **Base URL**: `https://todo-backend-fastapiuvicorn-main-app.onrender.com/` }`.

---

## Live Deployed Links
- **Frontend**: [https://todo-frontend-fastapi.onrender.com/](https://todo-frontend-fastapi.onrender.com/)
- **Backend**: [https://todo-backend-fastapiuvicorn-main-app.onrender.com/docs](https://todo-backend-fastapiuvicorn-main-app.onrender.com/docs)
