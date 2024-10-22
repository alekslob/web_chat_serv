from datetime import datetime

from ..repositories.messages import MessageRepository
from ..dto.messages import Message
from ..orm.messages import MessageModel


class MessageServices:
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    def add_message(self, message: Message):
        message = self.message_repository.add_message(
            MessageModel(
                content = message.content,
                create_time = datetime.now(),
                user_id = message.user_id
            )
        )
        return message
    
    def get_all_messages(self):
        return self.message_repository.get_all()