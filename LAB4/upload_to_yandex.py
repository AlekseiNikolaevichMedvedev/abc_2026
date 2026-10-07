import os
import sys
import requests

API_BASE = "https://cloud-api.yandex.net/v1/disk"

TOKEN = os.environ.get("YANDEX_DISK_TOKEN")
if not TOKEN:
    sys.exit("Ошибка: Не задана переменная окружения YANDEX_DISK_TOKEN. Задайте её перед запуском.")

HEADERS = {"Authorization": f"OAuth {TOKEN}"}

def get_upload_url(disk_path: str, overwrite: bool = True) -> str:
    """Запрашивает временную ссылку для загрузки файла."""
    print(f"[ЛОГ] 1. Запрос ссылки для загрузки файла в '{disk_path}'...")
    
    try:
        response = requests.get(
            f"{API_BASE}/resources/upload",
            headers=HEADERS,
            params={"path": disk_path, "overwrite": str(overwrite).lower()},
        )
        response.raise_for_status()
        return response.json()["href"]
    except requests.exceptions.HTTPError as e:
        print(f"[ОШИБКА] API при получении URL ({response.status_code}): {response.text}")
        sys.exit(1)

def upload_file(local_path: str, disk_path: str) -> None:
    """Загружает локальный файл на Яндекс.Диск."""
    if not os.path.exists(local_path):
        raise FileNotFoundError(f"Локальный файл не найден по пути: {local_path}")
        
    upload_url = get_upload_url(disk_path)
    
    print(f"[ЛОГ] 2. Отправка бинарных данных файла '{local_path}' методом PUT...")
    with open(local_path, "rb") as f:
        response = requests.put(upload_url, data=f)
        
    if response.status_code in [201, 202]:
        print(f"[УСПЕХ] Файл успешно отправлен на Диск: {disk_path}")
    else:
        print(f"[ОШИБКА] При передаче файла ({response.status_code}): {response.text}")
        response.raise_for_status()

def check_file(disk_path: str) -> dict:
    """Проверяет наличие файла на Диске и возвращает его метаданные."""
    print(f"[ЛОГ] 3. Проверка файла в облаке и запрос метаданных...")
    try:
        response = requests.get(
            f"{API_BASE}/resources",
            headers=HEADERS,
            params={"path": disk_path},
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        print(f"[ОШИБКА] API при проверке файла ({response.status_code}): {response.text}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Использование: python upload_to_yandex.py <local_file> <disk_path>")
        
    local_file = sys.argv[1]
    disk_route = sys.argv[2]
    
    try:
        upload_file(local_file, disk_route)
        meta = check_file(disk_route)
        
        print("\n--- Результаты проверки метаданных ---")
        print(f" Имя на Диске: {meta['name']}")
        print(f" Размер в облаке: {meta['size']} байт")
        print(f" Тип ресурса: {meta['type']}")
        
    except FileNotFoundError as err:
        print(f"Ошибка: {err}")
        sys.exit(1)
    except Exception as err:
        print(f"Непредвиденная ошибка во время выполнения: {err}")
        sys.exit(1)
