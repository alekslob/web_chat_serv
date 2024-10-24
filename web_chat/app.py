from flask import Flask, send_from_directory
from flask_jwt_extended import JWTManager   
import datetime

from .config import config
from .blueprints import api_blueprints


app = Flask(__name__, static_url_path='', static_folder='../static')

app.config["JWT_SECRET_KEY"] = "PekvHCqYpCYvNpJ44qSDfQlNuBqWKBut"  #  Замените  на  настоящий  секретный  ключ
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=30)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(days=30)
jwt = JWTManager(app)

from loguru import logger
@app.route('/', defaults={'path': ''})
@app.route('/static/<path:path>')
def index(path):
    logger.debug(path)
    if path!='':
        logger.debug("Пытается вернуть по адресу")
        return send_from_directory('../static', path)
    return send_from_directory('../static', 'index.html')


def run_server():
   app.register_blueprint(api_blueprints)
   app.run(
       host=config.server_settings.host,
       port=config.server_settings.port)