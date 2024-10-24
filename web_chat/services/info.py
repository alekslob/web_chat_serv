from ..dto.info import AppInfoResponse
from .. import __version__

class InfoServices:
    def __init__(self):
        pass

    def get_app_info(self) -> AppInfoResponse:
        '''Информация о приложении'''
        return AppInfoResponse(
            app_version=".".join(map(str, __version__))
            )