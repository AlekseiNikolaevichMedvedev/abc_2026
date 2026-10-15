# #todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

import nltk
import re

nltk.download('words', quiet=True)

from nltk.corpus import words

english_vocab = set(w.lower() for w in words.words())


def caesar_decode(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)


def score_by_vocab(text):
    found_words = re.findall(r'[a-zA-Z]+', text)
    if not found_words:
        return 0.0
    hits = sum(1 for word in found_words if word.lower() in english_vocab)
    return hits / len(found_words)


def break_caesar(ciphertext):
    best_shift = None
    best_text = None
    best_score = -1.0
    for shift in range(26):
        decoded = caesar_decode(ciphertext, shift)
        score = score_by_vocab(decoded)
        if score > best_score:
            best_score = score
            best_shift = shift
            best_text = decoded
    return best_shift, best_text, best_score


if __name__ == '__main__':
    cipher = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
    shift, text, score = break_caesar(cipher)
    print(f"Сдвиг: {shift}")
    print(f"Оценка: {score:.2%}")
    print(f"Текст: {text}")