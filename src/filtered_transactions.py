"""
В модуле filtered_transactions.py
В этом модуле реализованы функции фильтрующие списки трансакции.
"""

import os
import re
from collections import defaultdict
from typing import Any

from dotenv import load_dotenv

from src.data_extractor import get_info_csv


def process_bank_search(data: list[dict], search_text: str) -> list[dict]:
    """Фильтрация трансакции по ключевому слову"""
    pattern = re.compile(search_text)
    result = []
    for transaction in data:
        if pattern.search(str(transaction)):
            result.append(transaction)
        else:
            continue

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Фильтрация трансакции по категориям с подсчётом операций в категориях"""
    result: Any = defaultdict(int)
    for transaction in data:
        category = transaction.get("description")

        if category in categories:
            result[category] += 1

    return dict(result)


if __name__ == "__main__":
    load_dotenv()  # Загрузка переменных из .env-файла.
    file_csv_path = os.getenv("FILE_PATH_CSV", "default_log_file.csv")

    data = get_info_csv(file_csv_path)
    search_text = "EXECUTED"
    categories = ["Перевод организации", "Перевод с карты на карту", "Перевод со счета на счет"]

    filter_data_1 = process_bank_search(data, search_text)
    filter_data_2 = process_bank_operations(data, categories)

    # Для 1ой функции
    for transaction in filter_data_1:
        print(transaction)

    # Для 2ой функции
    # for key, value in filter_data_2.items():
    #     print(key, value)
