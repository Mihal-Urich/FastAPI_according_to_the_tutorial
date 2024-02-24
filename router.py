from fastapi import APIRouter, Depends
from typing import Annotated
from repository import TaskRepository
from schemas import STaskAdd, STaskGet, STaskId

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("")
async def add_tasks(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"Ok" : True, "task_id" : task_id}


@router.get("")
async def get_tasks() -> list[STaskGet]:
    tasks = await TaskRepository.find_all()
    return tasks