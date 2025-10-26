"""
Файл main.py
Основной файл исполнения.
"""

from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date

card_number = "7000792289606361"

account_number = "73654108430135874305"

open_string = "Visa Platinum 7000792289606361"
open_string_1 = "Счет 73654108430135874305"

date_time = "2024-03-11T02:26:18.671407"


print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
print(mask_account_card(open_string))
print(mask_account_card(open_string_1))
print(get_date(date_time))
