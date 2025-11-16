"""
Файл test_widget.py
Содержит кейсы для тестирования модуля widget.py
со всеми его функциями.
"""
import pytest

from src.widget import get_date, mask_account_card


# Параметризованный тест.
@pytest.mark.parametrize(
    'open_string, expected',
    [
        ('Visa Platinum 7003792289606361', 'Visa Platinum 7003 79** **** 6361'),
        ('Maestro 6904586730976943', 'Maestro 6904 58** **** 6943'),
        ('MasterCard 9078642349023874', 'MasterCard 9078 64** **** 3874'),
        ('Visa Classic 7080792289606537', 'Visa Classic 7080 79** **** 6537'),
        ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
        ('Мир 9000787785436476', 'Мир 9000 78** **** 6476'),
        ('Счет 73654108430135874305', 'Счет **4305'),
        ('Счет 40395673049567304957', 'Счет **4957'),
        ('Счет 93482570239867239847', 'Счет **9847'),
    ]
)
def test_mask_account_card(open_string: str, expected: str) -> None:
    """Тест функции mask_account_card"""
    assert mask_account_card(open_string) == expected


@pytest.mark.parametrize(
    'format_date, expected',
    [
        ('2019-07-03T18:35:29.512364', '03.07.2019'),
        ('2018-06-30T02:08:58.425572', '30.06.2018'),
        ('2020-09-12T21:27:25.241689', '12.09.2020'),
        ('2022-03-14T09:21:33.419441', '14.03.2022'),
        ('2017-12-15T08:23:38.419456', '15.12.2017'),
        ('2023-11-18T20:11:31.455141', '18.11.2023'),
        ('2025-01-14T08:21:36.519841', '14.01.2025'),
        ('2025-01-14T10:25:33.317481', '14.01.2025'),
    ]
)
def test_get_date(format_date: str, expected: str) -> None:
    assert get_date(format_date) == expected
