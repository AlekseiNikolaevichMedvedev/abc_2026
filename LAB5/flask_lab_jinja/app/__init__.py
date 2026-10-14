from flask import Flask

app = Flask(__name__)
# Секретный ключ необходим для шифрования данных сессии (куки)
app.secret_key = 'super-secret-key-for-lab-work'

from app import routes