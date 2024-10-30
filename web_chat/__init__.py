
__version__ = (0, 0, 0, 1)
from loguru import logger
from . import untils #noqa
from .app import run_server
from .orm import migrate


def start():
    try:
        logger.info("Запуск миграций")
        migrate()
        logger.success("Миграции пройдены успешно")
        logger.info("Запуск сервера")
        try:
            run_server()
        except SystemExit:
            logger.critical("Процедура запуска сервера завершилась ошибкой.")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logger.error(f"Необработанная ошибка: {str(e)}")

if __name__ == "__main__":
    start()