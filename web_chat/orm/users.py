from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from typing import List

from . import Base

class UserModel(Base):
    __tablename__ = 'users'
    username: Mapped[str] = mapped_column(unique=True)
    hash_password: Mapped[str]

    messages: Mapped[List["MessageModel"]] = relationship(
        back_populates="user"
    )

from .messages import MessageModel