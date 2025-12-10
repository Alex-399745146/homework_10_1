"""
Файл main.py
Основной файл исполнения.
"""

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

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

print("Тест следующих новых фитчей прикрученых к проекту согласно тасков домашки по 10_1")

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

[print(f"{i}") for i in filter_by_state(data, "CANCELED")]
print()
[print(f"{i}") for i in filter_by_state(data)]
print()

print("Согласно таска сортировка на убывание.")
for i in sort_by_date(data):
    print(i["date"][:10])
