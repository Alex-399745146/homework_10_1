"""
В модуле filtered_transactions.py
В этом модуле реализованы функции фильтрующие списки трансакции.
"""

import os
import re

from dotenv import load_dotenv

from src.data_extractor import get_info_csv


def process_bank_search(data: list[dict], search_text: str) -> list[dict]:
    """Фильтруем трансакции по ключевому слову"""
    pattern = re.compile(search_text)
    result = []
    for transaction in data:
        if pattern.search(str(transaction["description"])):
            result.append(transaction)
        else:
            continue

    return result


if __name__ == "__main__":
    load_dotenv()  # Загрузка переменных из .env-файла.
    file_csv_path = os.getenv("FILE_PATH_CSV", "default_log_file.csv")
    search_text = "Перевод организации"

    data = get_info_csv(file_csv_path)

    filter_data = process_bank_search(data, search_text)

    for item in filter_data:
        print(item)
