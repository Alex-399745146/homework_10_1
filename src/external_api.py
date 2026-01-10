"""
Принимает на вход транзакцию и возвращает сумму транзакции
(amount) в рублях, тип данных — float.
Если транзакция была в USD или EUR, происходит обращение
к внешнему API для получения текущего курса валют и
конвертации суммы операции в рубли.
"""

import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()


def convert_amount(amount: int) -> Dict[str, Any]:

    currency_in, currency_out = "USD", "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_out}&from={currency_in}&amount={amount}"
    headers = {"apikey": os.getenv("API_KEY")}

    response = requests.request("GET", url, headers=headers)

    status_code = response.status_code
    print("Status_server:", status_code)
    result: Dict[str, Any] = response.json()
    return result


data = convert_amount(100)
print(data)
for key, value in data.items():
    print(key, ":", value)
