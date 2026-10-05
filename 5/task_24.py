# # todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

import os

def caesar_cipher_left(text, shift):
    ru_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    ru_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ALPHABET_SIZE = 33
    result = []
    for char in text:
        if char in ru_lower:
            idx = ru_lower.index(char)
            new_idx = (idx - shift) % ALPHABET_SIZE
            result.append(ru_lower[new_idx])
        elif char in ru_upper:
            idx = ru_upper.index(char)
            new_idx = (idx - shift) % ALPHABET_SIZE
            result.append(ru_upper[new_idx])
        else:
            result.append(char)    
    return "".join(result)


def process_file():
    with open("message.txt", "r", encoding="utf-8") as infile, \
         open("encrypted.txt", "w", encoding="utf-8") as outfile:
        
        for line_num, line in enumerate(infile, start=1):
            encrypted_line = caesar_cipher_left(line, line_num)
            outfile.write(encrypted_line)
            
    print("Файл encrypted.txt успешно записан зашифрованными данными.")

if __name__ == "__main__":
    process_file()


