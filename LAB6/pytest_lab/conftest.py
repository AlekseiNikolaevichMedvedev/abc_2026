import pytest
from calculator import Calculator
from wheel_of_fortune import WheelOfFortune


@pytest.fixture
def calc():
    return Calculator()


@pytest.fixture
def game():
    """Фикстура для создания игры с дефолтным словом и 3 жизнями"""
    return WheelOfFortune(word="якубович", lives=3)
