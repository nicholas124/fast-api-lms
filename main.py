from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Nicholas",
        "email": "nmuchelemba@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)

users = []

class User(BaseModel):
    email: str
    is_active : bool


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="The ID of the user you want to retrieve.", gt=2),
    q: str = Query(None, max_length=5)
):
    return { "user": users[id], "query": q }