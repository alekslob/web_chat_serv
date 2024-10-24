from sqlalchemy.orm import Session
from sqlalchemy import select
from ..orm.users import UserModel
from typing import Optional

class UserRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_user_by_name(self, username: str) -> Optional[UserModel]:
        '''Получение пользователя из бд по имени'''
        user = self.session.execute(
            select(UserModel).where(UserModel.username == username)
        ).scalars().one_or_none()
        return user
    
    def get_user_by_id(self, id: int) -> Optional[UserModel]:
        '''Получение пользователя из бд по id'''
        user = self.session.execute(
            select(UserModel).where(UserModel.id == id)
        ).scalars().one_or_none()
        return user
    
    def add_user(self, user: UserModel) -> UserModel:
        '''Добавление в бд нового пользователя'''
        self.session.add(user)
        self.session.commit()
        return user