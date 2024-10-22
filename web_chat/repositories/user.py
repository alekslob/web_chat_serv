from sqlalchemy.orm import Session
from sqlalchemy import select
from ..orm.users import UserModel
from ..dto.user import User
from typing import Optional

class UserRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_user_by_name(self, username: str) -> Optional[UserModel]:
        user = self.session.scalars(
            select(UserModel).where(UserModel.username == username)
        ).one_or_none()
        return user
    
    def add_user(self, data: User) -> UserModel:
        user = UserModel(
            username = data.username,
            hash_password = data.hash_password
        )
        self.session.add(user)
        self.session.commit()
        return user