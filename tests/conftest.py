"""
Файл conftest.py для хранения фикстур.
"""

import os
from random import randint

import pandas as pd
import pytest
from dotenv import load_dotenv
from pandas import DataFrame


@pytest.fixture
def fixture_transactions() -> DataFrame:
    transactions_data = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    df = pd.DataFrame(transactions_data)
    return df


@pytest.fixture
def fixture_response_api() -> dict:
    response_api = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1768236064, "rate": 78.24865},
        "date": "2026-01-12",
        "result": 643311.103651,
    }
    return response_api


@pytest.fixture
def fixture_operation() -> list:
    transaction = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]
    return transaction


@pytest.fixture
def fixture_path() -> str:
    """Возвращает строку-путь до лог-файла"""
    load_dotenv()
    file_path = os.getenv("FILE_PATH", "default_log_file.json")
    return file_path


# Фикстура с генератором чисел без ведущего нуля.
@pytest.fixture
def fixture_num_str() -> dict[str, str]:
    """Возвращает словарь с 16 и 20-значным номерами"""
    first_digit = str(randint(1, 9))

    rest_digits_16 = "".join(str(randint(0, 9)) for _ in range(15))
    nums_digit_16 = first_digit + rest_digits_16

    rest_digits_20 = "".join(str(randint(0, 9)) for _ in range(19))
    nums_digit_20 = first_digit + rest_digits_20

    return {"digit_16": nums_digit_16, "digit_20": nums_digit_20}


@pytest.fixture
def fixture_list_operations() -> list[dict[str, str | int]]:
    """Возвращает список банковских операций словарями"""
    return [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 132452323, "state": "CANCELED", "date": "2020-09-12T21:27:25.241689"},
        {"id": 984357699, "state": "EXECUTED", "date": "2022-03-14T09:21:33.419441"},
        {"id": 984394534, "state": "EXECUTED", "date": "2017-12-15T08:23:38.419456"},
        {"id": 123432344, "state": "CANCELED", "date": "2023-11-18T20:11:31.455141"},
        {"id": 234554322, "state": "EXECUTED", "date": "2025-01-14T08:21:36.519841"},
        {"id": 768576858, "state": "EXECUTED", "date": "2025-01-14T10:25:33.317481"},
    ]
