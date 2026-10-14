import pytest
from wheel_of_fortune import WheelOfFortune


def test_initial_state(game):
    """Проверяем начальное состояние игры"""
    assert game.current_state == "********"
    assert game.lives == 3
    assert game.is_won is False
    assert game.is_game_over is False


def test_empty_word_raises_error():
    """Проверяем, что пустое слово вызывает исключение"""
    with pytest.raises(ValueError):
        WheelOfFortune(word="")


def test_guess_correct_letter(game):
    """Проверяем успешное угадывание буквы"""
    assert game.guess_letter("б") is True
    assert game.current_state == "***б****"
    assert game.lives == 3  # Жизни не уменьшились


def test_guess_wrong_letter(game):
    """Проверяем ошибку при угадывании буквы"""
    assert game.guess_letter("х") is False
    assert game.lives == 2  # Минус одна жизнь
    assert game.current_state == "********"


def test_guess_duplicate_letter(game):
    """Проверяем, что повторный ввод буквы не тратит жизни"""
    game.guess_letter("я")
    initial_lives = game.lives

    assert game.guess_letter("я") is False
    assert game.lives == initial_lives


def test_invalid_input_length(game):
    """Проверяем ввод нескольких букв вместо одной"""
    with pytest.raises(ValueError):
        game.guess_letter("абв")


def test_win_condition():
    """Проверяем логику победы"""
    game = WheelOfFortune(word="он", lives=2)
    game.guess_letter("о")
    game.guess_letter("н")
    assert game.is_won is True
    assert game.is_game_over is True


def test_lose_condition():
    """Проверяем логику проигрыша"""
    game = WheelOfFortune(word="да", lives=1)
    game.guess_letter("х")
    assert game.is_won is False
    assert game.is_game_over is True
    assert game.lives == 0
