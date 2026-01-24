"""
В модуле data_extractor.py
В этом модуле реализованы функции считывания финансовых операций
из файлов CSV- и XLSX-файлов из data.
"""

import csv
import json
import logging
import os

from dotenv import load_dotenv


def get_info_csv(file_csv_path: str) -> Any:
    """ Считывает данные из csv в data и выдаёт их на выходе """
    pass


def get_info_xlsx(file_csv_path: str) -> Any:
    """ Считывает данные из xlsx в data и выдаёт их на выходе """
    pass


if __name__ == "__main__":
    load_dotenv()  # Загрузка переменных из .env-файла.

    file_csv_path = os.getenv("FILE_PATH_CSV", "default_log_file.csv")
    file_xlsx_path = os.getenv("FILE_PATH_XLSX", "default_log_file.xlsx")

    data_csv = get_info_csv(file_path)
    data_xlsx = get_info_xlsx(file_xlsx_path)