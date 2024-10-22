from flask import Blueprint
from .utils import json_response, validate
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..exceptions import WebChatError
from ..dto.messages import Message, MessageResponce
from ..services.message import MessageServices
from ..dependencies.messages_dependencies import extract_message_services
messages = Blueprint("messages", __name__, url_prefix='/messages/')

@messages.route('/', methods=['GET'])
@json_response
@jwt_required()
def all_messages(services: MessageServices=extract_message_services()):
    messages = services.get_all_messages()
    return [MessageResponce.model_validate(message) for message in messages]

@messages.route('/', methods=['POST'])
@json_response
@jwt_required()
@validate(Message)
def send_message(message: Message, services: MessageServices=extract_message_services()):
    user_id = get_jwt_identity()
    if user_id == message.user_id:
        message = services.add_message(message=message)
        return MessageResponce.model_validate(message)
    else:
        raise WebChatError("Проблема с токеном")