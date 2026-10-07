Лабораторная: Парсинг сайта через requests
Цель: Написать скрипт, который скачивает страницу через requests и извлекает из неё данные.

Подготовка
Установить библиотки 
pip install requests beautifulsoup4 lxml

Описание библиотек.
requests
Элегантная и простая HTTP-библиотека для Python, созданная для людей . Она позволяет отправлять GET и POST запросы, управлять заголовками, работать с cookies и сессиями, а также обрабатывать ответы сервера (JSON, текст, бинарные данные) .

Ключевая особенность: Автоматически берет на себя всю «черную работу» по реализации HTTP/1.1: управление keep-alive, пулинг соединений, декодирование контента и многое другое .
Ссылка на документацию: https://docs.python-requests.org/


BeautifulSoup 
Библиотека для парсинга HTML и XML документов . Она строит дерево разбора из полученной HTML-страницы и предоставляет удобные методы для поиска, навигации и извлечения данных из этого дерева .

Ключевая особенность: Позволяет искать элементы по имени тега, CSS-классу, атрибутам или тексту с помощью методов find() и find_all() .

Ссылка на документацию: https://www.crummy.com/software/BeautifulSoup/bs4/doc/


lxml
Что это: Библиотека для обработки XML и HTML на Python, которая служит высокопроизводительным парсером . Она часто используется совместно с BeautifulSoup в качестве «движка» для разбора HTML, так как работает значительно быстрее стандартного парсера Python .

Ключевая особенность: Предоставляет Pythonic API, совместимый с ElementTree, но при этом использует скорость и мощь C-библиотек libxml2 и libxslt .

Ссылка на документацию: https://lxml.de/




Спарсить цитаты с https://quotes.toscrape.com (текст + автор) и сохранить в JSON.

Код (parser.py)

import json
import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com"
HEADERS = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=HEADERS, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
quotes = [
    {
        "text": q.select_one("span.text").get_text(strip=True),
        "author": q.select_one("smal.author").get_text(strip=True),
    }
    for q in soup.select("div.quote")
]

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=2)

print(f"Спарсено {len(quotes)} цитат")

Запуск.
python parser.py

Задание:
Получив общее представление как извлекаются данные из ресурса.
Создать базу данных в MongoDB для игры "Поле чудес". Для этого найти 
подходящие сайты. Просмотреть их HTML и найти необходимые блоки.
