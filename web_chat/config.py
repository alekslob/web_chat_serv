# from .ext.parametrica.parametrica import Parametrica, Field, Fieldset
# from .ext.parametrica.parametrica.predefined.network import PortField, AnyHostField
# from .ext.parametrica.parametrica.io import YAMLFileConfigIO, VirtualYAMLFileConfigIO
import os
from .consts import SETTINGS_FILE_NAME

class ServerSettings():
    host = "0.0.0.0"
    port = os.environ.get('PORT', 8000)
    access_token_lifetime = os.environ.get('TOCKEN_LIFETIME', 30)

class DBSettings():
    # host = AnyHostField("0.0.0.0").label("Адрес сервера")
    # port = PortField(8000).label("Порт сервера")
    # user = Field[str]('user').label("Пользователь")
    # password = Field[str]('pwd').label("Пароль")

    database = os.environ.get('DB_NAME', 'webchat')

    @property
    def connection_string(self) -> str:
        return f'sqlite:///{DBSettings.database}.db'


class DebugSettings():
    level = 3

class Config():
    server_settings = ServerSettings()
    db_settings = DBSettings()

config = Config()

# class DevConfig(Parametrica):
#     dev_env = Field[bool](False).label('Окружение разработки')
#     node_url = Field[str]('127.0.0.1:8080').label('УРЛ на ноду')
#     stdout_logs = Field[bool](True).label("Логи в stdout")


# dev_config = DevConfig(VirtualYAMLFileConfigIO('dev.env'))