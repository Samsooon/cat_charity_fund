from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from sqlalchemy import Column, DateTime, String

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    first_name = Column(String, nullable=False)
    birthdate = Column(DateTime)
