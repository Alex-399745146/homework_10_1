"""
Файл widget.py
Этот модуль будет содержать функции для работы с новыми
возможностями приложения.
"""

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(open_string: str) -> str:
    """
    Обрабатывать информацию как о КАРТАХ, так и о СЧЕТАХ.
    Принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращать строку с замаскированным номером карты или счёта.
    # Пример для карты
    Visa Platinum 7000792289606361 # входной аргумент
    Visa Platinum 7000 79** **** 6361 # выход функции
    # Пример для счета
    Счет 73654108430135874305 # входной аргумент
    Счет **4305 # выход функции
    """

    ls_string = open_string.rsplit(maxsplit=1)  # Разделяем справа один раз.
    name_acc, num_acc = ls_string[0], ls_string[1]
    prefix = name_acc + " "

    if len(num_acc) == 16:
        card_name = prefix
        card_number: str = num_acc
        return card_name + get_mask_card_number(card_number)

    elif len(num_acc) == 20:
        account_name: str = prefix
        account_number: str = num_acc
        return account_name + get_mask_account(account_number)
    return "В функцию - mask_account_card(): вводятся неверные данные."


def get_date(date_time: str) -> str:
    """
    Принимает на вход строку '2024-03-11T02:26:18.671407'
    и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'.
    """
    ls_date = date_time[:10].split("-")
    format_date = ".".join(ls_date[::-1])
    return format_date
