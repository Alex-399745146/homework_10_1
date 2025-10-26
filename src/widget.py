"""
Файл widget.py
Этот модуль будет содержать функции для работы с новыми
возможностями приложения.
"""

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(open_string: str) -> str:
    """
    Обрабатывать информацию как о картах, так и о счетах.
    Принимать один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращать строку с замаскированным номером карты или счёта.
    """

    ls_string = open_string.rsplit(maxsplit=1)  # Разделяем справа один раз.
    part_1, part_2 = ls_string[0], ls_string[1]
    part_1 = part_1 + " "

    if len(part_2) == 16:
        card_name: str = part_1
        card_number: str = part_2
        return card_name + get_mask_card_number(card_number)

    elif len(part_2) == 20:
        account_name: str = part_1
        account_number: str = part_2
        return account_name + get_mask_account(account_number)
    return "В функцию - mask_account_card(): вводятся неверные данные."
