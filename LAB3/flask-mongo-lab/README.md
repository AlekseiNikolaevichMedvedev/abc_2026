# Flask + MongoDB Lab
## Запуск
```bash
cp .env.example .env # при необходимости
docker compose up --build -d
```
## Проверка
```bash
curl http://localhost:5000/hello
curl http://localhost:5000/health
```
Ожидаемый ответ `/hello`:
```json
{
"status": "ok",
"message": "Hello, World!",
"db": "hello_db",
"visits": 1
}
```
## Остановка
```bash
docker compose down # остановить
docker compose down -v # остановить и удалить volumes
```
## Логи
```bash
docker compose logs -f app
docker compose logs -f mongo
```