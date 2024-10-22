from ..services.message import MessageServices
from ..repositories.messages import MessageRepository
from .message_repository_dependencies import extract_message_repository

def extract_message_services(
        message_repository: MessageRepository = extract_message_repository()
)-> MessageServices:
    return MessageServices(
        message_repository=message_repository
    )