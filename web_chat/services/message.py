from datetime import datetime
from typing import List

from ..repositories.messages import MessageRepository
from ..dto.messages import Message, MessageResponce
from ..orm.messages import MessageModel


class MessageServices:
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    def add_message(self, message: Message):
        '''Создает новое сообщение'''
        message = self.message_repository.add_message(
            MessageModel(
                content = message.content,
                create_time = datetime.utcnow(),
                user_id = message.user_id
            )
        )
        return message
    
    def get_all_messages(self) -> List[MessageResponce]:
        '''Выгружает список сообщений'''
        return [MessageResponce.model_validate(message) for message in self.message_repository.get_all()]