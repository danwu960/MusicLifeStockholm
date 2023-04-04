from typing import Any

from pydantic import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.sql.type_api import TypeEngine

from database.connection import Base


# User model in the database
class User(Base):
    __tablename__ = "users"
    user: Column[TypeEngine[Any] | Any] | Column = Column(String, primary_key=True, index=True)
    pw = Column(String, index=False)

    def __rep__(self):
        return "<User(user='%s', password='%s')>" % (
            self.user,
            self.pw,
        )


class UserReq(BaseModel):
    username: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "user": "some user name",
            }
        }
