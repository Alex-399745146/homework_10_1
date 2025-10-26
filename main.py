"""
Файл main.py
Основной файл исполнения.
"""

from src.masks import get_mask_account, get_mask_card_number

card_number = "7000792289606361"

account_number = "73654108430135874305"


print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
