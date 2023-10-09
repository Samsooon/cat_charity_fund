from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.core.db import get_async_session
from app.schemas.charity_project import (
    CharityProjectCreate, CharityProjectUpdate, CharityProjectDB
)
from app.api.validators import check_project_name_dup, check_project_was_closed, check_correct_full_amount_for_update, check_charity_proj_exists, check_proj_was_invested
from app.core.user import current_superuser
from app.process.investment import execute_investment_process

router = APIRouter(prefix='/charity_project', tags=['charity projects'])


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_projects(
        session: AsyncSession = Depends(get_async_session)
):
    return await charity_project_crud.get_multi(session)


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser), ]

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
    await execute_investment_process(new_project, session)
    await session.refresh(new_project)
    return new_project


@router.delete(
    '/{project_id}',
    deprecated=True,
    dependencies=[Depends(current_superuser), ]
)
async def delete_projects(
        project_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    charity_proj = await check_charity_proj_exists(
        project_id,
        session
    )
    await check_proj_was_invested(project_id, session)
    charity_proj = await(
        charity_project_crud.remove(
            charity_proj, session
        )
    )
    return charity_proj


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)]
)
async def partially_update_charity_project(
    project_id: int,
    object_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    charity_project = await check_charity_proj_exists(
        project_id, session
    )
    await check_project_was_closed(project_id, session)

    if object_in.full_amount is not None:
        await check_correct_full_amount_for_update(
            project_id, session, object_in.full_amount
        )

    if object_in.name is not None:
        await check_project_name_dup(
            object_in.name, session
        )

    charity_project = await charity_project_crud.update(
        charity_project, object_in, session
    )
    return charity_project
