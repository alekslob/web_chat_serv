
from contextlib import contextmanager
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session
from sqlalchemy.orm import Mapped, mapped_column
from web_chat.config import config as app_config

try:
    engine = create_engine(app_config.db_settings.connection_string)
except Exception as e:
    raise Exception(f"При создании соединения произошла ошибка: {e}")

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    deleted: Mapped[bool] = mapped_column(default=False)

def session_factory(**kwargs):
    return scoped_session(sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False,
            future=True,
            **kwargs
        )
    )

from typing import Generator
from sqlalchemy.orm import Session

@contextmanager
def session_context():# -> Generator[Session, None, None]:
    session = session_factory()

    try:
        yield session
    except Exception:
        logger.error('Session rollback because of exception')
        session.rollback()
        raise
    else:
        session.commit()
    finally:
        session.close()


from alembic import config, command
def migrate():
    cfg = config.Config()
    cfg.set_main_option("script_location", "./alembic/")
    cfg.set_main_option("sqlalchemy.url", app_config.db_settings.connection_string)

    with engine.begin() as connection:
        cfg.attributes["connection"] = connection
        command.upgrade(cfg, "head")