from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from .utils import json_response
from ..dto import AppInfoResponse, UserResponce
from ..services import InfoServices, UserService

from ..dependencies.info_dependencies import extract_info_services
from ..dependencies.user_dependencies import extract_user_services


info = Blueprint("info", __name__, url_prefix="/info/")

@info.route('app/', methods=["GET"])
@json_response
def app_info(services: InfoServices = extract_info_services()) -> AppInfoResponse:
    '''возвращает интформацию о приложении'''
    return services.get_app_info()

@info.route('user/', methods=["GET"])
@json_response
@jwt_required()
def user_info(services: UserService = extract_user_services()) -> UserResponce:
    '''возвращает интформацию об авторизованном пользователе'''
    id = get_jwt_identity()
    return services.get_user_info_by_id(id)