from flask import Flask, send_from_directory
from flask_jwt_extended import JWTManager   
import datetime
from .consts import SECRET_KEY
from .config import config
from .blueprints import api_blueprints
from .exceptions import ConfigurationException
app = Flask(__name__, static_url_path='', static_folder='../static')
from loguru import logger
# конфигурация для токенов
try:
    if not SECRET_KEY:
        raise ConfigurationException("Не заполнен секретный ключ")
    app.config["JWT_SECRET_KEY"] = SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=int(config.server_settings.access_token_lifetime))
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(days=30)
except ConfigurationException:
    logger.error("Не заполнен секретный ключ")
    exit()
jwt = JWTManager(app)

# загрузка файлов из static
@app.route('/', defaults={'path': ''})
@app.route('/static/<path:path>')
def index(path):
    if path!='':
        return send_from_directory('../static', path)
    return send_from_directory('../static', 'index.html')

# запуск сервера
def run_server():
   
   app.register_blueprint(api_blueprints)
   app.run(
       host=config.server_settings.host,
       port=config.server_settings.port)