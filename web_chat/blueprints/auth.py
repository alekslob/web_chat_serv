from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, set_access_cookies
from .utils import json_response, validate

from ..dto.auth import AuthSchema, AuthResponse
from ..services.auth import AuthServices
from ..dependencies.auth_dependencies import extract_auth_services


auth = Blueprint("auth", __name__, url_prefix='/')

@auth.route('auth/', methods=['POST'])
@json_response
@validate(AuthSchema)
def user_auth(authschema: AuthSchema, services: AuthServices = extract_auth_services()) -> AuthResponse:
    '''Регистрация пользователя'''
    return services.auth(authschema)

@auth.route('login/', methods=['POST'])
@json_response
@validate(AuthSchema)
def user_login(authschema: AuthSchema, services: AuthServices = extract_auth_services()) -> AuthResponse:
    '''Авторизация пользователя'''
    return services.login(authschema)

@auth.route('refresh/', methods=['POST'])
@json_response
@jwt_required(refresh=True)
def refresh(services: AuthServices = extract_auth_services()):
    '''Обновление токена'''
    id = get_jwt_identity()
    return services.check_token(id)
