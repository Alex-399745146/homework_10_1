"""
Файл conftest.py для хранения фикстур.
"""

import pytest, random


# Фикстура с генератором чисел без ведущего нуля.
@pytest.fixture
def fixture_num_str():
    """Возвращает словарь с 16 и 20-значным номерами"""
    first_digit = str(random.randint(1, 9))

    rest_digits_16 = ''.join(str(random.randint(0, 9)) for _ in range(15))
    nums_digit_16 = first_digit + rest_digits_16

    rest_digits_20 = ''.join(str(random.randint(0, 9)) for _ in range(19))
    nums_digit_20 = first_digit + rest_digits_20

    return { 'digit_16': nums_digit_16, 'digit_20': nums_digit_20}
