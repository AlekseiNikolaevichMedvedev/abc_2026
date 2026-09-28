import warnings
def transform_array(my_list):
    try:
        if not my_list:
            raise ValueError("Список пуст")
        result = [x + 1 for x in my_list if type(x) is int]
        if len(result) != len(my_list):
            warnings.warn(
                "В списке были обнаружены некорректные не int. Они проигнорированы.", 
                UserWarning
            )
            
        return result
        
    except ValueError as e:
        print(f"Критическая ошибка: {e}")
        return None


if __name__ == "__main__":
    while True:
        raw_input = input("Введите целые числа через пробел: ").strip()
       
        if raw_input:
            input_list = []
            for x in raw_input.split():
                try:
                    input_list.append(int(x))
                except ValueError:
                    input_list.append(x)
            
            print("Результат:", transform_array(input_list))
            break
        else:
            print("Вы ничего не ввели, попробуйте еще.")