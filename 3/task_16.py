# # todo: База данных пользователя.
# # Задан массив объектов пользователя

# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

# #Затем сообщение для ввода
# Ввидите критерии поиска: 16

# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"
def get_slice(database, ind, criterion):
    if not database:
        return []      
    try:
        keys = list(database[0].keys())
        key_index = int(ind) - 1
        key = keys[key_index]
    except (ValueError, IndexError):
        print("Введен некорректный критерий поиска")
        return []
    if key == 'age':
        slice = [user for user in database if user[key] > int(criterion)]    
    elif key == 'login':
        slice = [user for user in database if user[key][0].lower() == criterion.lower()]   
    else:
        slice = [user for user in database if user[key].lower() == criterion.lower()]
    return slice

if __name__ == "__main__":
    users = [
        {'login': 'Piter', 'age': 23, 'group': "admin"},
        {'login': 'Ivan',  'age': 10, 'group': "guest"},
        {'login': 'Dasha', 'age': 30, 'group': "master"},
        {'login': 'Fedor', 'age': 13, 'group': "guest"}
    ]

    print("Введите номер типа сортировки:")
    print("1. По первой букве")
    print("2. По возрасту")
    print("3. По группе\n")

    ind = input("тип сортировки: ").strip()
    
    criterion = input("Введите критерии поиска: ").strip()
    print()
    
    filtered_users = get_slice(users, ind, criterion)
    
    if filtered_users:
        print("Результат:")
        for user in filtered_users:
            print(f"Пользователь: {user['login']}, "+ 
                  f"возраст {user['age']}, группа  \"{user['group']}\"")
    else:
        print("Пользователи по заданным критериям не найдены.")

