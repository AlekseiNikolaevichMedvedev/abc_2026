# #todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

import re

def get_letter_from_int(number_str: str) -> str:
    number = int(number_str)
    if number == 0:
        return " "
    ascii_code = 96 + number
    return chr(ascii_code)

def change_ints_to_letters(input_string: str) -> str:
    output_string = ""
    parts = re.split(r"(\d+)", input_string)   
    for part in parts:
        if part.isdigit():
            output_string += get_letter_from_int(part)
        else:
            if output_string.endswith(" ") and part.startswith(" "):
                output_string += part[1:]
            else:
                output_string += part            
    return output_string

if __name__ == '__main__':
    input_string = input("Введите строку для конвертации: ")
    output_string = change_ints_to_letters(input_string)
    print(f"Результат: {output_string}")
