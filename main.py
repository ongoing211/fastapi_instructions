from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id = int

@app.get("/tasks")
def get_tasks():
    task = Task(name="Постирать вещи")
    return {"data": task}

