from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List

from ..orm.messages import MessageModel

class MessageRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List:
        '''выгружает все сообщения из бд'''
        return self.session.execute(
            select(MessageModel)
        ).scalars().all()
    
    def add_message(self, message: MessageModel) -> MessageModel:
        '''добавляет сообщение в бд'''
        self.session.add(message)
        self.session.commit()
        return message