"""
Файл masks.py
Реализованно в этом модуле две функции:
1. Функцию маскировки номера банковской карты get_mask_card_number.
2. Функцию маскировки номера банковского счета get_mask_account.
"""

import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(filename="logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.propagate = False


def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает его маскированную версию"""
    logger.info(f"Накладываем маску на номер карты: {card_number}")
    try:
        card_number = card_number[:6] + "*" * 6 + card_number[-4:]
        card_mask = " ".join([card_number[num : num + 4] for num in range(0, len(card_number), 4)])
        logger.info(f"Маска номера карты на выходе:     {card_mask}")

        return card_mask

    except Exception as e:
        logger.error(e, exc_info=True)
        raise


def get_mask_account(account_number: str) -> str:
    """Принимает номер счёта и возвращает его маскированную версию"""
    logger.info(f"Накладываем маску на номер счёта: {account_number}")
    try:
        account_mask = "*" * 2 + account_number[-4:]
        logger.info(f"Маска номера счёта на выходе:     {account_mask}")

        return account_mask

    except Exception as e:
        logger.error(e, exc_info=True)
        raise


if __name__ == "__main__":
    card_number = "7000792289606361"
    account_number = "73654108430135874305"

    print(get_mask_card_number(card_number))
    print(get_mask_account(account_number))
