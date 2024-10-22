from flask import Blueprint, Response
from typing_extensions import Annotated
from .utils import json_response
from ..dto.info_schemas import AppInfoSchema
from ..services.info_services import InfoServices
from ..dependencies.info_dependencies import extract_info_services

info = Blueprint("info", __name__, url_prefix="/info/")




@info.route('app/', methods=["GET"])
@json_response
def app_info(services: InfoServices = extract_info_services()) -> AppInfoSchema:
    return services.get_app_info()

