# Лабораторная работа: Разработка веб-приложения на Flask с использованием шаблонизатора Jinja2


## Цель работы

Изучить архитектуру Flask-приложения, освоить механизм Request-Response Cycle, научиться создавать HTML-шаблоны с использованием Jinja2, применять блочную верстку HTML5, подключать CSS-стили и медиаресурсы из папки `static`, а также использовать наследование шаблонов.


## Теоретическая часть

### 1. Request-Response Cycle во Flask

При обработке HTTP-запроса во Flask происходит следующая последовательность действий:

1. Браузер отправляет HTTP-запрос на сервер.
2. Web-сервер разбирает URL и вызывает соответствующий **роутер** (`routes.py`).
3. Роутер обращается к **модели** (`models.py`) для извлечения данных из БД (MongoDB).
4. Модель возвращает данные из БД.
5. Данные передаются в **шаблонизатор** (папка `templates/`).
6. Шаблонизатор формирует HTML-страницу, подставляя данные.
7. Медиаресурсы (CSS, изображения, JS) подгружаются из папки `static/`.
8. Сформированная страница возвращается браузеру.

### 2. Технологический стек Web 2.0

- HTML5 / CSS3
- Препроцессоры CSS: SASS / LESS
- JavaScript / TypeScript
- Ajax
- WebSocket

### 3. HTML5 — семантическая разметка

В HTML5 появились семантические теги, заменяющие `<div>` с идентификаторами:

| HTML4 | HTML5 |
|-------|-------|
| `<div id="header">` | `<header>` |
| `<div id="nav">` | `<nav>` |
| `<div id="content">` | `<section>` |
| `<div class="post">` | `<article>` |
| `<div id="footer">` | `<footer>` |

### 4. Шаблонизатор Jinja2

**Шаблонизатор** — инструмент, позволяющий отделить логику представления данных от их отображения, делить разметку на компоненты и избегать дублирования кода.

Основные конструкции:

- `{{ переменная }}` — вывод значения
- `{% ... %}` — управляющие конструкции (блоки, циклы, условия)
- `{% extends "base.html" %}` — наследование шаблона
- `{% block name %}{% endblock %}` — определение блока
- `{{ super() }}` — вызов содержимого родительского блока
- `{{ url_for('static', filename='...') }}` — генерация ссылок на статику

---

## Ход работы

### Шаг 1. Создание папки проекта

```bash
mkdir flask_lab_jinja
cd flask_lab_jinja
```

### Шаг 2. Создание виртуального окружения

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Шаг 3. Установка Flask

```bash
pip install flask
pip freeze > requirements.txt
```

### Шаг 4. Структура проекта

```
flask_lab_jinja/
│
├── venv/                          # виртуальное окружение
├── app/
│   ├── __init__.py                # инициализация приложения
│   ├── routes.py                  # роутер
│   ├── templates/                 # HTML-шаблоны
│   │   ├── base.html              # базовый шаблон
│   │   ├── page.html              # страница на базе base.html
│   │   ├── index.html             # главная
│   │   └── about.html             # "О нас"
│   └── static/                    # медиаресурсы
│       ├── css/
│       │   └── default.css        # стили
│       └── img/
│           └── logo.png           # изображение
├── run.py                         # точка входа
└── requirements.txt
```


### Шаг 5. Инициализация приложения (`app/__init__.py`)

```python
from flask import Flask

app = Flask(__name__)

from app import routes
```

### Шаг 6. Роутер (`app/routes.py`)

```python
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/page')
def page():
    return render_template('page.html')
```

### Шаг 7. Точка входа (`run.py`)

```python
from app import app

if __name__ == '__main__':
    app.run(debug=True)
```

### Шаг 8. Базовый шаблон (`app/templates/base.html`)

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    {% block head %}
    <meta charset="utf-8">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/default.css') }}">
    <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
</head>
<body>
    <header>
        <h1 class="logo">First Web App</h1>
        <nav>
            <ul class="menu">
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('about') }}">About</a></li>
                <li><a href="{{ url_for('page') }}">Page</a></li>
            </ul>
        </nav>
    </header>

    <section id="content">
        {% block content %}{% endblock %}
    </section>

    <footer>
        {% block footer %}
        &copy; Copyright 2025 by <a href="#">student</a>.
        {% endblock %}
    </footer>
</body>
</html>
```

### Шаг 9. Страница на базе родительского шаблона (`app/templates/page.html`)

```html
{% extends "base.html" %}

{% block title %}Index{% endblock %}

{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}

{% block content %}
    <h1>Index</h1>
    <p class="important">
        Welcome to my awesome homepage.
    </p>
{% endblock %}
```

### Шаг 10. Главная страница с данными (`app/templates/index.html`)

```html
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
    <h1>Hello, {{ user.nickname }}!</h1>
    <p>Это главная страница. Данные подставлены через Jinja2.</p>
    <img src="{{ url_for('static', filename='img/logo.png') }}" alt="Logo" width="120">
{% endblock %}
```

### Шаг 11. Страница «О нас» (`app/templates/about.html`)

```html
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
    <h1>О нас</h1>
    <p>Лабораторная работа по Flask и Jinja2.</p>
{% endblock %}
```

### Шаг 12. CSS-стили (`app/static/css/default.css`)

```css
* { box-sizing: border-box; }

body {
    font-family: Verdana, Arial, Helvetica, sans-serif;
    margin: 0;
    color: #333;
}

header {
    background: #f2b6c1;
    padding: 20px;
    text-align: center;
}

h1.logo {
    font-size: 140%;
    color: #333366;
    margin: 0 0 10px;
}

nav ul.menu {
    list-style: none;
    padding: 0;
    margin: 0;
}

nav ul.menu li {
    display: inline-block;
    margin: 0 10px;
}

nav ul.menu a {
    color: #0066cc;
    text-decoration: none;
}

section#content {
    min-height: 300px;
    padding: 20px;
    background: #f9d9b5;
}

footer {
    background: #66c1b8;
    padding: 15px;
    text-align: center;
}
```

> **Примечание:** разместите любой файл `logo.png` в `app/static/img/`, либо удалите тег `<img>` из шаблона.

### Шаг 13. Запуск приложения

```bash
python run.py
```

Проверьте в браузере:

| URL | Что отображается |
|-----|------------------|
| `http://127.0.0.1:5000/` | Главная (Hello, Miguel!) |
| `http://127.0.0.1:5000/index` | То же самое (два маршрута на одну функцию) |
| `http://127.0.0.1:5000/about` | Страница «О нас» |
| `http://127.0.0.1:5000/page` | Страница на базе `base.html` |

### Шаг 14. Эксперименты с Jinja2

Добавьте в `index.html` блок с циклом и условием:

```html
{% block content %}
    <h1>Hello, {{ user.nickname }}!</h1>

    {% if user.nickname == 'Miguel' %}
        <p>Это наш администратор.</p>
    {% else %}
        <p>Это обычный пользователь.</p>
    {% endif %}

    <h2>Список пунктов:</h2>
    <ul>
    {% for i in range(1, 4) %}
        <li>Пункт {{ i }}</li>
    {% endfor %}
    </ul>
{% endblock %}
```

### Шаг 15. Дополнительное задание

1. **Макет по образцу.** Создайте шаблон с игрой "Поле чудес". Воспользуйтесь кодогенерацией по существующей логике игры.


---

## Контрольные вопросы

1. Опишите последовательность Request-Response Cycle во Flask.
2. Для чего нужны папки `templates` и `static`? Какие файлы хранятся в каждой из них?
3. Что такое шаблонизатор и какие задачи он решает?
4. В чём разница между конструкциями `{{ ... }}` и `{% ... %}` в Jinja2?
5. Как работает наследование шаблонов? Для чего нужны теги `{% extends %}` и `{% block %}`?
6. Что делает функция `super()` в Jinja2?
7. Зачем нужна функция `url_for()` и почему не рекомендуется указывать пути к статике напрямую?
8. Как передать данные из роутера в шаблон? Что принимает `render_template()`?
9. Приведите пример использования условного оператора и цикла в Jinja2.
10. Назовите семантические теги HTML5 и их HTML4-аналоги.

---

