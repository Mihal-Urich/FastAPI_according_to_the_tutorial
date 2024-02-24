from data_base import new_session, TasksORM
from schemas import STaskAdd, STaskGet
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id



    @classmethod
    async def find_all(cls) -> list[STaskGet]:
        async with new_session() as session:
            query = select(TasksORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STaskGet.model_validate(task_model) for task_model in task_models]
            return task_schemas