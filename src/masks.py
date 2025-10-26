"""
Файл masks.py
Реализованно в этом модуле две функции:
1. Функцию маскировки номера банковской карты get_mask_card_number.
2. Функцию маскировки номера банковского счета get_mask_account.
"""


def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает его маскированную версию."""
    card_number = card_number[:6] + "*" * 6 + card_number[-4:]  # Конкатенация.
    card_mask = " ".join([card_number[num : num + 4] for num in range(0, len(card_number), 4)])
    return card_mask


def get_mask_account(account_number: str) -> str:
    """Принимает номер счёта и возвращает его маскированную версию."""
    account_mask = "*" * 2 + account_number[-4:]
    return account_mask
