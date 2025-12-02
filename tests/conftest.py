"""
Файл conftest.py для хранения фикстур.
"""

from random import randint

import pytest


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


@pytest.fixture
def fixture_full_transactions() -> list[dict]:
    """Фикстура примера входных данных"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "", "code": ""}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
