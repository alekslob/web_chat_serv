from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List
from datetime import datetime

from . import Base

class MessageModel(Base):
    __tablename__ = 'messages'
    content = Mapped[str]
    create_time: Mapped[datetime]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["UserModel"] = relationship(
        back_populates="messages"
    )


from .users import UserModel