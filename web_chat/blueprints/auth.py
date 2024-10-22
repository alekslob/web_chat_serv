from flask import Blueprint
from .utils import json_response, validate

from ..dto.auth_schemas import AuthSchema
from ..dto.user import User
from ..services.auth_services import AuthServices
from ..dependencies.auth_dependencies import extract_auth_services

auth = Blueprint("auth", __name__, url_prefix='/')

@auth.route('auth/', methods=['POST'])
@json_response
@validate(AuthSchema)
def user_auth(authschema: AuthSchema, services: AuthServices = extract_auth_services()) -> User:
    return services.auth(authschema)

@auth.route('login/', methods=['POST'])
@json_response
@validate(AuthSchema)
def user_login(authschema: AuthSchema, services: AuthServices = extract_auth_services()) -> User:
    return services.login(authschema)
