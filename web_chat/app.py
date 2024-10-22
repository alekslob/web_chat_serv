from flask import Flask
from flask_jwt_extended import JWTManager
import datetime

from .config import config
from .blueprints import api_blueprints


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "PekvHCqYpCYvNpJ44qSDfQlNuBqWKBut"  #  Замените  на  настоящий  секретный  ключ
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=30)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(days=30)
jwt = JWTManager(app)

def run_server():
   app.register_blueprint(api_blueprints)
   app.run(
       host=config.server_settings.host,
       port=config.server_settings.port)