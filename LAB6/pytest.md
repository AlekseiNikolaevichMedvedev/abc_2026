# Лабораторная работа: «PyTest + GitHub Actions»

**Цель:** написать тесты на PyTest и автоматически запускать их в GitHub Actions при каждом пуше.


### Шаг 1. Создайте папку проекта

```bash
mkdir pytest_lab
cd pytest_lab
```

### Шаг 2. Создайте виртуальное окружение

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (cmd):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

После активации в начале строки терминала появится `(venv)`.


### Шаг 3. Установите библиотеки

Создайте файл `requirements.txt`:

```
pytest
pytest-cov
```

Установите:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Проверьте:

```bash
pytest --version
```

### Создайте структура проекта 

```
pytest_lab/
├── venv/
├── requirements.txt
├── calculator.py          ← создадим в части 1
├── conftest.py
├── pytest.ini
├── .github/
│   └── workflows/
│       └── tests.yml
└── tests/
    └── test_calculator.py
```

---

## Часть 1. Код 

###  `calculator.py`

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль")
        return a / b

    def is_even(self, n):
        return n % 2 == 0
```


## Часть 2. Конфиг 

### `pytest.ini`

```ini
[pytest]
markers =
    smoke: быстрые проверки
testpaths = tests
```

### `conftest.py`

```python
import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()
```

### `tests/test_calculator.py`

```python
import pytest

@pytest.mark.smoke
def test_add(calc):
    assert calc.add(2, 2) == 4

def test_subtract(calc):
    pass

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add_parametrized(calc, a, b, expected):
    assert calc.add(a, b) == expected


def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(1, 0)


@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, False),
])
def test_is_even(calc, n, expected):
    assert calc.is_even(n) is expected
```

### Проверка

```bash
pytest -v                    # все тесты
pytest -m smoke -v           # только smoke
pytest --cov=calculator      # с покрытием
```

**Ожидаемо:** все зелёные 

---

## Часть 3. GitHub Actions 

### `.github/workflows/tests.yml`

```yaml
name: Tests

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run smoke tests
        run: pytest -m smoke -v

      - name: Run full test suite with coverage
        run: pytest --cov=calculator --cov-report=term-missing
```

### Что здесь происходит

| Блок | Зачем |
|---|---|
| `on: push / pull_request` | Запуск на каждый пуш и PR |
| `matrix.python-version` | Проверка на 3 версиях Python |
| `actions/checkout@v4` | Клонирует репозиторий |
| `setup-python@v5` | Ставит нужную версию Python |
| `pip install -r` | Устанавливает зависимости |
| `pytest -m smoke` | Быстрая проверка «жив ли код» |
| `pytest --cov` | Полный прогон с покрытием |

---

## Часть 4. Пуш и проверка 

```bash
git init
git add .
git commit -m "Add pytest lab with CI"
git branch -M main
git remote add origin <ваш-репозиторий>
git push -u origin main
```

### Где смотреть результат

1. Откройте репозиторий на GitHub
2. Вкладка **Actions** → workflow **Tests**
3. Зелёная галочка ✅ = всё прошло
4. Красный крест ❌ = смотрите лог

---

## Часть 5. Итоговое задание (5 мин)
1. Для игры "Поле чудес" сгенерировать покрытие тестами и проверку на
   Github Action


