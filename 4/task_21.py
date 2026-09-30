# #todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# # нужно сопоставить данные для подстановки.

# # Содержимое файла config_default.txt
# # Конфигурация приложения.
# app_name    = ?
# version     = ?
# debug       = ?

# # Настройки базы данных
# db_host     = ?
# db_port     = ?
# db_name     = ?
# db_user     = ?
# db_password = ?

# # Настройки API
# api_key     = ?
# api_secret  = ?
# base_url    = ?

# # Пути
# log_file    = ?
# data_dir    = ?
# temp_dir    = ?


# # Данные для подстановки
# config_values = {
#     'app_name': 'NextGen',
#     'version': '1.0.0',
#     'debug':  True,
#     'db_host': 'localhost',
#     'db_port': 5432,
#     'db_name': 'my_database',
#     'db_user': 'admin',
#     'db_password': 'secret123',
#     'api_key': 'ak_123456789',
#     'api_secret': 'sk_987654321',
#     'base_url': 'https://api.example.com',
#     'log_file': '/var/log/app.log',
#     'data_dir': '/opt/app/data',
#     'temp_dir': '/tmp/app',
#     'max_workers': 10,
#     'timeout': 30,
#     'retry_attempts': 3
# }

# # В итоге вместо "?" должны подставиться значения и получиться файл config.txt:

# # Конфигурация приложения
# app_name    =  "NextGen"
# version     =  '1.0.0'
# debug       =  True

# # Настройки базы данных
# db_host     =  5432
# .....
import re

config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug':  True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

config_default_str = '''
# Содержимое файла config_default.txt
# Конфигурация приложения.
app_name    = ?
version     = ?
debug       = ?

# Настройки базы данных
db_host     = ?
db_port     = ?
db_name     = ?
db_user     = ?
db_password = ?

# Настройки API
api_key     = ?
api_secret  = ?
base_url    = ?

# Пути
log_file    = ?
data_dir    = ?
temp_dir    = ?
'''
def replace_config_value(match):
    key = match.group(1)

    if key not in config_values:
        return match.group(0) 
    
    val = config_values[key]

    if isinstance(val, str):
        formatted_val = f'"{val}"'

    else:
        formatted_val = str(val)

    return f"{key}{match.group(2)}{formatted_val}"

with open('./config_default.txt', mode = 'w', encoding = 'utf-8') as file:
    file.write(config_default_str)

pattern = r'^(\w+)(\s*=\s*)\?'

with open('config_default.txt', 'r', encoding='utf-8') as file:
     template_content = file.read()

filling = re.sub(pattern, replace_config_value, config_default_str, flags=re.MULTILINE)

with open('./config.txt',mode = 'w', encoding = 'utf-8') as file:
    file.write(filling)

