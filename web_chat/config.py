from .ext.parametrica.parametrica import Parametrica, Field, Fieldset
from .ext.parametrica.parametrica.predefined.network import PortField, AnyHostField
from .ext.parametrica.parametrica.io import YAMLFileConfigIO, VirtualYAMLFileConfigIO
from .consts import SETTINGS_FILE_NAME

class ServerSettings(Fieldset):
    host = AnyHostField("0.0.0.0").label("Адрес сервера").secret()
    port = PortField(8000).label("Порт сервера")
    access_token_lifetime = Field[int](30).label('Время жизни токена (в минутах)')

class DBSettings(Fieldset):
    # host = AnyHostField("0.0.0.0").label("Адрес сервера")
    # port = PortField(8000).label("Порт сервера")
    # user = Field[str]('user').label("Пользователь")
    # password = Field[str]('pwd').label("Пароль")

    database = Field[str]('webchat').label("Имя базы данных")

    @property
    def connection_string(self) -> str:
        return f'sqlite:///{self.database}.db'


class DebugSettings(Fieldset):
    level = Field[int](3).label("Уровень логирования")

class Config(Parametrica):
    server_settings = Field[ServerSettings]().label("Настройки сервера")
    db_settings = Field[DBSettings]().label("Настройки подключения к базе данных")

config = Config(YAMLFileConfigIO(SETTINGS_FILE_NAME))

class DevConfig(Parametrica):
    dev_env = Field[bool](False).label('Окружение разработки')
    node_url = Field[str]('127.0.0.1:8080').label('УРЛ на ноду')
    stdout_logs = Field[bool](True).label("Логи в stdout")


dev_config = DevConfig(VirtualYAMLFileConfigIO('dev.env'))