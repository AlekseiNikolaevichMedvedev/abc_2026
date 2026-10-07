
# Лабораторная работа: Загрузка файлов на Яндекс.Диск через REST API (Python)

##  Цель работы

Написать Python-скрипт, который загружает локальный файл на Яндекс.Диск через REST API, используя OAuth-токен.


## Предварительные требования
   
- Установленная библиотека `requests`:  
      
    pip install requests
    
- Аккаунт на Яндексе и зарегистрированное приложение для получения OAuth-токена.
    


## Шаг 1. Получение OAuth-токена

Токен нужен для авторизации запросов к API.

**Вариант А — через Полигон (быстро, для лабы):**

1. Откройте [https://yandex.ru/dev/disk/poligon/](https://yandex.ru/dev/disk/poligon/)
    
2. Нажмите «Получить OAuth-токен» и авторизуйтесь.
    
3. Скопируйте токен.
    

**Вариант Б — через регистрацию приложения (правильный путь):**

1. Зайдите в [https://oauth.yandex.ru/](https://oauth.yandex.ru/) → «Создать приложение».
    
2. Выберите платформу «Веб-сервисы», укажите Redirect URI (например, `https://oauth.yandex.ru/verification_code`).
    
3. В правах доступа отметьте:
    
    - `cloud_api:disk.read`
        
    - `cloud_api:disk.write`
        
    - `cloud_api:disk.info`
        
4. Получите `ClientID` и `ClientSecret`, затем пройдите OAuth-флоу для получения токена.
    

**Сохраните токен** — он понадобится в скрипте. Лучше не хардкодить его, а положить в переменную окружения.


export YANDEX_DISK_TOKEN="y0_AgAAAA..."


## Шаг 2. Структура скрипта

Скрипт должен состоять из трёх логических частей:

### 2.1. Запрос URL для загрузки

Яндекс.Диск работает по двухшаговой схеме: сначала запрашивается временная ссылка (`upload_url`), потом на неё отправляется файл.
https://yandex.ru/dev/disk-api/doc/ru/reference/upload

**Эндпоинт:** `GET https://cloud-api.yandex.net/v1/disk/resources/upload`

**Параметры:**

- `path` (обязательный) — путь на Диске, например `disk:/test.txt`
    
- `overwrite` (опционально) — `true`, чтобы перезаписать существующий файл
    

**Заголовки:**

- `Authorization: OAuth <ваш_токен>`
    

**Ожидаемый ответ:**

{
  "href": "https://uploader...",
  "method": "PUT",
  "templated": false
}

### 2.2. Загрузка файла по полученному URL

**Метод:** `PUT <href из шага 2.1>`

**Тело запроса:** содержимое файла (в бинарном виде).

**Важно:** OAuth-токен здесь **не нужен** — ссылка уже авторизована и действует ~30 минут.

**Успешный ответ:** HTTP `201 Created`.

### 2.3. (Опционально) Проверка результата

**Эндпоинт:** `GET https://cloud-api.yandex.net/v1/disk/resources`

**Параметры:**

- `path` — путь к загруженному файлу
    

Убедитесь, что файл появился и его размер совпадает с локальным.



## Шаг 3. Реализация

Напишите скрипт `upload_to_yandex.py`:

python

import os
import sys
import requests
API_BASE = "https://cloud-api.yandex.net/v1/disk"
TOKEN = ""
if not TOKEN:
    sys.exit("Ошибка: не задана переменная окружения YANDEX_DISK_TOKEN")

HEADERS = {"Authorization": f"OAuth {TOKEN}"}
def get_upload_url(disk_path: str, overwrite: bool = True) -> str:
    """Запрашивает временную ссылку для загрузки файла."""
    response = requests.get(
        f"{API_BASE}/resources/upload",
        headers=HEADERS,
        params={"path": disk_path, "overwrite": str(overwrite).lower()},
    )
    response.raise_for_status()
    return response.json()["href"]

def upload_file(local_path: str, disk_path: str) -> None:
    """Загружает локальный файл на Яндекс.Диск."""
    upload_url = get_upload_url(disk_path)
    with open(local_path, "rb") as f:
        response = requests.put(upload_url, data=f)
    if response.status_code == 201:
        print(f"Файл загружен: {disk_path}")
    else:
        response.raise_for_status()
def check_file(disk_path: str) -> dict:
    """Проверяет наличие файла на Диске и возвращает его метаданные."""
    response = requests.get(
        f"{API_BASE}/resources",
        headers=HEADERS,
        params={"path": disk_path},
    )
    response.raise_for_status()
    return response.json()
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Использование: python upload_to_yandex.py <local_file> <disk_path>")
    local_file, disk_path = sys.argv[1], sys.argv[2]
    upload_file(local_file, disk_path)
    meta = check_file(disk_path)
    print(f" Имя: {meta['name']}")
    print(f" Размер: {meta['size']} байт")
    print(f" Ссылка: {meta.get('public_url', '—')}")

**Запуск:**

python upload_to_yandex.py ./test.txt disk:/test.txt

---

## Шаг 4. Критерии сдачи

1. **Рабочий скрипт**, который:
    
    - принимает путь к локальному файлу и путь на Диске;
        
    - получает `upload_url` через API;
        
    - загружает файл методом `PUT`;
        
    - проверяет результат через `GET /resources`.
        
2. **Обработка ошибок**:
    
    - отсутствие токена → понятное сообщение;
        
    - `4xx/5xx` от API → вывод тела ответа и статуса;
        
    - отсутствие локального файла → `FileNotFoundError`.
        
3. **Работа с секретами**: токен берётся из переменной окружения, а не хардкодится.
    
4. **Логи**: выводятся все ключевые шаги (получение URL, загрузка, проверка).
    
5. **Демонстрация**: скриншот успешного запуска + файл, видимый в веб-интерфейсе Яндекс.Диска.