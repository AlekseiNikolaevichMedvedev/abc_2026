import os
from helpers.crypt import caesar_cipher_left

def process_file(input_path="message.txt", output_path="encrypted.txt"):
    if not os.path.exists(input_path):
        print(f"Ошибка: Файл {input_path} не найден.")
        return False
        
    with open(input_path, "r", encoding="utf-8") as infile, \
         open(output_path, "w", encoding="utf-8") as outfile:
        
        for line_num, line in enumerate(infile, start=1):
            encrypted_line = caesar_cipher_left(line, line_num)
            outfile.write(encrypted_line)
            
    print(f"Файл {output_path} успешно записан зашифрованными данными.")
    return True
