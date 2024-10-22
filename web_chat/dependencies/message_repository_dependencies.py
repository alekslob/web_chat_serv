from sqlalchemy.orm import Session
from ..repositories.messages import MessageRepository
from ..orm import session_context

def extract_message_repository(
) -> MessageRepository:
    with session_context() as session:
        return MessageRepository(
            session=session
        )