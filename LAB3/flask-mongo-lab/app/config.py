import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_USER = os.getenv("MONGO_ROOT_USER", "admin")
    MONGO_PASSWORD = os.getenv("MONGO_ROOT_PASSWORD", "secret123")
    MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_DB = os.getenv("MONGO_DB", "hello_db")

    # Таймаут выбора сервера (важно для быстрого падения при недоступности)
    MONGO_TIMEOUT_MS = 5000

    @property
    def mongo_uri(self) -> str:
        return (
            f"mongodb://{self.MONGO_USER}:{self.MONGO_PASSWORD}"
            f"@{self.MONGO_HOST}:{self.MONGO_PORT}/?authSource=admin"
        )
