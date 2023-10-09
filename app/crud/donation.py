from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.user import User
from app.models.donation import Donation


class CRUDDonation(CRUDBase):

    async def get_donations_by_user(
            self,
            session: AsyncSession,
            user: User,
    ) -> list[Donation]:
        user_donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return user_donations.scalars().all()


donation_crud = CRUDDonation(Donation)
