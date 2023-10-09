from typing import Optional
from datetime import datetime

from pydantic import (
    BaseModel, Field,
    PositiveInt, Extra,
    validator, root_validator
)


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100
    )
    description: Optional[str] = Field(
        None,
        min_length=1
    )
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
    )
    description: str = Field(
        ...,
        min_length=1
    )
    full_amount: PositiveInt = Field(
        ...,
        title='Ожидаемая сумма',
        description='Какая сумма необходима на данный проект'
    )

    class Config:
        @validator('name')
        def name_validator(self, value: str):
            if len(value) > 100:
                raise ValueError(
                    'Имя не может быть больше 100 символов'
                )
            if value.isnumeric():
                raise ValueError(
                    'Имя не может быть числом'
                )
            return value

        class CharityProjectUpdate(CharityProjectBase):
            pass

        @root_validator(skip_on_failure=True)
        def check_empty_fields(self, values):
            if values is None:
                raise ValueError(
                    'Поля не могут быть пустыми'
                )
            return values


class CharityProjectUpdate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
