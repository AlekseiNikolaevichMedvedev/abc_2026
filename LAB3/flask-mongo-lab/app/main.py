import logging
from flask import Flask, jsonify
from pymongo.errors import OperationFailure, PyMongoError
from .config import Config
from .db import mongo

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

app = Flask(__name__)
if not mongo.connect():
    app.logger.warning("Не удалось подключиться к MongoDB при старте")

@app.route("/")
@app.route("/hello")
def hello():
    """Возвращает приветствие и текущее время из MongoDB."""
    try:
        # Проверяем соединение
        if not mongo.ping():
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": "MongoDB недоступна",
                    }
                ),
                503,
            )

        collection = mongo.db["greetings"]

        # Атомарно увеличиваем счётчик обращений
        result = collection.find_one_and_update(
            {"_id": "counter"},
            {"$inc": {"visits": 1}},
            upsert=True,
            return_document=True,
        )

        visits = result.get("visits", 0) if result else 0

        return jsonify(
            {
                "status": "ok",
                "message": "Hello, World!",
                "db": Config.MONGO_DB,
                "visits": visits,
            }
        )
    except OperationFailure as e:
        app.logger.error("Ошибка операции MongoDB: %s", e)
        return jsonify({"status": "error", "message": "Ошибка запроса"}), 500
    except PyMongoError as e:
        app.logger.error("Ошибка PyMongo: %s", e)
        return jsonify({"status": "error", "message": "Ошибка БД"}), 500
    except Exception as e:
        app.logger.exception("Непредвиденная ошибка")
        return jsonify({"status": "error", "message": "Внутренняя ошибка"}), 500


@app.route("/health")
def health():
    """Healthcheck для Docker."""
    if mongo.ping():
        return jsonify({"status": "healthy"}), 200
    return jsonify({"status": "unhealthy"}), 503


if __name__ == "__main__":
    # Пытаемся подключиться на старте
    if not mongo.connect():
        app.logger.warning("Не удалось подключиться к MongoDB при старте")

    app.run(host="0.0.0.0", port=5000)
