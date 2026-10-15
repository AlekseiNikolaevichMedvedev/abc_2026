import os
import pytest
from helpers.crypt import caesar_cipher_left
from helpers.io import process_file

# ==========================================
# 1. ТЕСТЫ ШИФРОВАНИЯ (helpers/crypt.py)
# ==========================================

def test_caesar_left_simple():
    # Г -> В, д -> г, е -> д
    assert caesar_cipher_left("Где", 1) == "Вгд"

def test_caesar_ignore_symbols():
    assert caesar_cipher_left("!123,", 3) == "!123,"

def test_process_file_success():
    input_name = "test_input.txt"
    output_name = "test_output.txt"
    
    with open(input_name, "w", encoding="utf-8") as f:
        f.write("Где")
    result = process_file(input_name, output_name)
    
    assert result is True
    assert os.path.exists(output_name)
    
    with open(output_name, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == "Вгд"
    
    if os.path.exists(input_name): 
        os.remove(input_name)
    if os.path.exists(output_name): 
        os.remove(output_name)

def test_process_file_not_found():
    result = process_file("missing_file.txt", "output.txt")
    assert result is False
