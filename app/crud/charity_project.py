from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession
    ):
        project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return project_id.scalars().first()

    async def get_charity_project_invested_amount(
            self,
            project_id: int,
            session: AsyncSession
    ):
        project_invested_amount = await session.execute(
            select(CharityProject.invested_amount).where(
                CharityProject.id == project_id
            )
        )
        return project_invested_amount.scalars().first()

    async def get_charity_project_close_date(
            self,
            project_id: int,
            session: AsyncSession
    ):
        project_close_date = await session.execute(
            select(CharityProject.close_date).where(
                CharityProject.id == project_id
            )
        )
        return project_close_date.scalars().first()

    async def update(
        self,
        db_object,
        object_in,
        session: AsyncSession
    ):
        obj_data = jsonable_encoder(db_object)
        update_data = object_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_object, field, update_data[field])

        # if db_object.full_amount == db_object.invested_ammount:
        #     db_object.fully_invested = True
        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        return db_object

    async def remove(
            self,
            db_object,
            session: AsyncSession
    ):
        await session.delete(db_object)
        await session.commit()
        return db_object


charity_project_crud = CRUDCharityProject(CharityProject)
