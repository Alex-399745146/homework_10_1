"""Модуль external_api.py содержит функции работающие в валютами а волатильность валют обновляет API"""

import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.utils import get_info_operations


def get_convert_amount(transaction: dict) -> Any:
    """
    Конвертирует сумму транзакции в рубли по курсу API.
    Возвращает float или поднимает исключение при ошибке.
    """
    tx_currency_code: str = transaction["operationAmount"]["currency"]["code"]
    amount: float = transaction["operationAmount"]["amount"]

    if tx_currency_code == "RUB":

        return amount

    convert_in = tx_currency_code
    convert_out = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={convert_out}&from={convert_in}&amount={amount}"
    headers = {"apikey": os.getenv("API_KEY")}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Проверить, произошла ли ошибка во время запроса.

        if response.status_code == 200:
            response_api = response.json()
            print(response_api)
            return round(response_api["result"], 2)

    except requests.exceptions.RequestException as err:

        raise ConnectionError(f"Ошибка запроса к API: {err}")

    except (KeyError, ValueError, TypeError) as err:

        raise ValueError(f"Некорректный ответ от API: {err}")


if __name__ == "__main__":
    load_dotenv()  # Загрузка переменных из .env-файла.
    file_path = os.getenv("FILE_PATH", "default_log_file.json")
    transaction = get_info_operations(file_path)[1]
    data = get_convert_amount(transaction)
    print(data)
