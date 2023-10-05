from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.crud.charity_projects import charity_project_crud
from app.models.charity_projects import CharityProject


async def check_project_name_dup(
        project_name: str,
        session: AsyncSession
):
    project_id = charity_project_crud.get_project_id_by_name(
        project_name,
        session
    )
    if project_id is not None:
        raise HTTPException(
            status_code=404,
            detail='Проект с таким именем уже существует!'
        )