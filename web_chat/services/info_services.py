from ..dto.info_schemas import AppInfoSchema
from .. import __version__

class InfoServices:
    def __init__(self):
        pass

    def get_app_info(self) -> AppInfoSchema:
        return AppInfoSchema(
            app_version=".".join(map(str, __version__)))