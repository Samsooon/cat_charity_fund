from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_projects import charity_project_crud
from app.core.db import get_async_session
from app.schemas.charity_projects import(
    CharityProjectCreate, CharityProjectUpdate, CharityProjectDB
)
from app.api.validators import check_project_name_dup

router = APIRouter(prefix='/charity_project', tags=['charity projects'])


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True
)
async def get_all_projects(
        session: AsyncSession = Depends(get_async_session)
):
    return await charity_project_crud.get_multi(session)


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def create_projects(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session)
):
    await check_project_name_dup(
        charity_project.name,
        session
    )
    new_project = await charity_project_crud.create(charity_project, session)
    await session.refresh(new_project)


@router.delete(
    '/{project_id}',
    deprecated=True,
)
def delete_projects():
    return {'Hello': 'projects'}


@router.patch(
    '/{project_id}',
    deprecated=True
)
def update_projects():
    return {'Hello': 'projects'}
