import logging
from typing import Optional
from pymongo import MongoClient
from pymongo.errors import (
    ConfigurationError,
    ConnectionFailure,
    PyMongoError,
    ServerSelectionTimeoutError,
)

from .config import Config
logger = logging.getLogger(__name__)


class MongoDB:
    """Обёртка над PyMongo с корректной обработкой ошибок."""

    def __init__(self, config: Config):
        self.config = config
        self._client: Optional[MongoClient] = None
        self._db = None

    def connect(self) -> bool:
        try:
            self._client = MongoClient(
                self.config.mongo_uri,
                serverSelectionTimeoutMS=self.config.MONGO_TIMEOUT_MS,
                retryWrites=True,
                retryReads=True,
            )
            # Реальная проверка соединения
            self._client.admin.command("ping")
            self._db = self._client[self.config.MONGO_DB]
            logger.info("Подключение к MongoDB установлено")
            return True
        except ServerSelectionTimeoutError:
            logger.error("MongoDB недоступна (timeout)")
        except ConfigurationError as e:
            logger.error("Ошибка конфигурации MongoDB: %s", e)
        except ConnectionFailure as e:
            logger.error("Ошибка соединения с MongoDB: %s", e)
        except PyMongoError as e:
            logger.error("Ошибка PyMongo: %s", e)
        return False

    def close(self):
        if self._client:
            self._client.close()
            logger.info("Соединение с MongoDB закрыто")

    @property
    def db(self):
        if self._db is None:
            raise RuntimeError("MongoDB не инициализирована")
        return self._db

    def ping(self) -> bool:
        try:
            self._client.admin.command("ping")
            return True
        except PyMongoError:
            return False


# Глобальный экземпляр (для простоты лабы)
mongo = MongoDB(Config())