"""
Файл test_masks.py
Содержит кейсы для тестирования модуля masks.py
со всеми его функциями.
"""

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(fixture_num_str: dict) -> None:
    """Тест функции get_mask_card_number"""
    digit_16: str = fixture_num_str["digit_16"]

    # Test входных данных.
    assert str.isdigit(digit_16) and len(digit_16) == 16, "Не корректные входные данные"

    # Test выходных данных.
    card_mask: str = get_mask_card_number(digit_16)

    assert card_mask.count(" ") == 3, "Не верный формат данных выхода"
    assert card_mask.count("*") == 6, "Неверно созданная маска"
    assert isinstance(card_mask, str), "Вывод не строкового типа данных"


def test_get_mask_account(fixture_num_str: dict) -> None:
    """Тест функции get_mask_account"""
    digit_20: str = fixture_num_str["digit_20"]

    # Test входных данных.
    assert str.isdigit(digit_20) and len(digit_20) == 20, "Не корректные входные данные"

    # Test выходных данных.
    account_mask: str = get_mask_account(digit_20)

    assert account_mask[:2] == "**" and str.isdigit(account_mask[2:]), "Неверно созданная маска"
    assert isinstance(account_mask, str), "Вывод не строкового типа данных"
