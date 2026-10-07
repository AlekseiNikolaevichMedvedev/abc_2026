0. Создайте новый проект game-flask-app с виртуальным окружением

1. Создайте структуру проекта.

game-flask-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── templates/
    └── index.html


2. Создайте Dockerfile с содержимым
------------------------------------
# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Открываем порт
EXPOSE 5000

# Команда запуска
CMD ["python", "app.py"]
-----------------------------------

3. Установите микрофреймворк Flask через pip  

4. Создайте файл app.py со следующем кодом 
--------------------------------------------
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask in Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


6. Исключи из сборки (docker build) файли и папки в .dockerignore
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
.git
.gitignore
.pytest_cache
.coverage
htmlcov/
*.log
.DS_Store
.idea/
.vscode/
*.sqlite3
.env
Dockerfile
docker-compose.yml
README.md
   

7. Введите команды для сборки и запуска проекта

# Сборка образа
docker build -t game-flask-app .

# Запуск контейнера
docker run -d -p 5000:5000 --name flask-container game-flask-app

# Проверка
curl http://localhost:5000

# Просмотр логов
docker logs -f flask-container

# Остановка
docker stop flask-container && docker rm flask-container

