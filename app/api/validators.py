from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from pydantic import PositiveInt

from app.crud.charity_project import charity_project_crud


async def check_charity_proj_exists(
        project_id: int,
        session: AsyncSession
):
    charity_proj = await charity_project_crud.get(
        project_id, session
    )
    if not charity_proj:
        raise HTTPException(
            status_code=404,
            detail='Данного проекта не существует'
        )
    return charity_proj


async def check_project_name_dup(
        project_name: str,
        session: AsyncSession
):
    charity_project_id = await (
        charity_project_crud.get_project_id_by_name(
            project_name=project_name, session=session
        )
    )
    if charity_project_id is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!'
        )


async def get_project_invested_amount(
        session: AsyncSession,
        project_id: int
):
    charity_project = await charity_project_crud.get(
        project_id,
        session
    )
    if charity_project.invested_amount != 0:
        raise HTTPException(
            status_code=400,
            detail='Проект нельзя удалить, так как были внесены средства'
        )


async def check_proj_was_invested(
        project_id: int,
        session: AsyncSession
):
    project = await(
        charity_project_crud.get(project_id, session)
    )
    if project.invested_amount:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!'
        )


async def check_project_was_closed(
    project_id: int,
    session: AsyncSession
):
    project_close_date = await (
        charity_project_crud.get_charity_project_close_date(
            project_id, session
        )
    )
    if project_close_date:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!'
        )


async def check_project_closed_or_exists(
        project_id: int,
        session: AsyncSession,
        deletion: bool = False
):
    charity_project = await charity_project_crud.get(
        project_id,
        session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден.'
        )
    if charity_project.fully_invested:
        message = 'Проект нельзя удалить, так как были внесены средства'
        if deletion:
            message = 'Закрытый проект нельзя редактировать!'
        raise HTTPException(
            status_code=400,
            detail=message
        )


async def check_correct_full_amount_for_update(
    project_id: int,
    session: AsyncSession,
    full_amount_to_update: PositiveInt
):
    db_project_invested_amount = await (
        charity_project_crud.get_charity_project_invested_amount(
            project_id, session
        )
    )
    if db_project_invested_amount > full_amount_to_update:
        raise HTTPException(
            status_code=422,
            detail=f'Новая требуемая сумма должна быть больше уже внесенной в проект суммы - {db_project_invested_amount}'
        )
