"""
Файл test_data_extractor.py
Содержит кейсы для тестирования модуля data_extractor.py
"""

import os
import re
from unittest.mock import Mock

import pandas as pd
from dotenv import load_dotenv
from pandas import DataFrame

from src.data_extractor import get_info_csv, get_info_xlsx


def test_get_info_csv(fixture_transactions: DataFrame) -> None:
    load_dotenv()
    file_csv_path = os.getenv("FILE_PATH_CSV", "default_log_file.csv")
    mock_read_csv = Mock(return_value=fixture_transactions)
    pd.read_csv = mock_read_csv
    pattern = r"^" + re.escape(file_csv_path) + r"$"
    result = get_info_csv(file_csv_path)
    assert isinstance(result, list)
    assert isinstance(file_csv_path, str)
    assert isinstance(result, list)
    assert re.fullmatch(pattern, file_csv_path)
    try:
        with open(file_csv_path, "r", encoding="utf-8"):
            pass  # файл существует и доступен для чтения
        assert True
    except FileNotFoundError:
        assert False, "Файл не найден"


def test_get_info_xlsx(fixture_transactions: DataFrame) -> None:
    load_dotenv()
    file_xlsx_path = os.getenv("FILE_PATH_XLSX", "default_log_file.xlsx")
    mock_read_excel = Mock(return_value=fixture_transactions)
    pd.read_excel = mock_read_excel
    pattern = r"^" + re.escape(file_xlsx_path) + r"$"
    result = get_info_xlsx(file_xlsx_path)
    assert isinstance(result, list)
    assert isinstance(file_xlsx_path, str)
    assert isinstance(result, list)
    assert re.fullmatch(pattern, file_xlsx_path)
    try:
        with open(file_xlsx_path, "r", encoding="utf-8"):
            pass  # файл существует и доступен для чтения
        assert True
    except FileNotFoundError:
        assert False, "Файл не найден"
