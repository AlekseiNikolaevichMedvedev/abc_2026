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
