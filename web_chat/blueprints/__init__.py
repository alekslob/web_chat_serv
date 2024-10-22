from flask import Blueprint
from .info import info
from .auth import auth
from .messages import messages

api_blueprints = Blueprint("api_blueprints", __name__, url_prefix="")
api_blueprints.register_blueprint(info)
api_blueprints.register_blueprint(auth)
api_blueprints.register_blueprint(messages)
