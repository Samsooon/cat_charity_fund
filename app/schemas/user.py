import datetime
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    first_name: str
    birthdate: Optional[datetime.date]


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    birthdate: Optional[datetime.date]


class UserUpdate(schemas.BaseUserUpdate):
    first_name: Optional[str]
    birthdate: Optional[datetime.date]
