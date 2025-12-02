"""
Тестовый-модуль tests_generators.py
Содержит кейсы для тестирования функций модуля generators.py.
"""

import pytest

from src.generators import card_number_generator, filter_by_currency, number_generator, transaction_descriptions

world_currency_codes: tuple = (
    "RUB",
    "USD",
    "EUR",
    "GBP",
    "JPY",
    "CHF",
    "CAD",
    "AUD",
    "NZD",
    "CNY",
    "INR",
    "KRW",
    "SGD",
    "MXN",
    "BRL",
    "HKD",
    "SAR",
    "THB",
    "AED",
    "SEK",
    "NOK",
    "DKK",
    "PLN",
    "HUF",
    "CZK",
    "DZD",
    "AMD",
    "BHD",
    "BGN",
    "GEL",
    "ILS",
    "KZT",
    "UZS",
    "PHP",
    "ZAR",
    "TRY",
    "UAH",
    "CZK",
    "RON",
    "HRK",
    "ISK",
    "MYR",
    "IDR",
    "VND",
    "THB",
    "QAR",
    "OMR",
    "KWD",
    "JOD",
    "LYD",
)

full_transactions: list[dict] = [
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


@pytest.mark.parametrize(
    "full_transactions, filter_name, result",
    [
        (full_transactions[:], "RUB", 1),
        (full_transactions[:], "EUR", 0),
        (full_transactions[:], "USD", 2),
        ([], "RUB", 0),
    ],
)
def test_filter_by_currency(full_transactions: list[dict], filter_name: str, result: int) -> None:
    """Тест функции filter_by_currency"""
    assert len(list(filter_by_currency(full_transactions, filter_name))) == result
    assert filter_name in world_currency_codes, f"Не корректный код валюты >> {filter_name}."


@pytest.mark.parametrize(
    "transaction, result",
    [
        ([full_transactions[0]], "Перевод организации"),
        ([full_transactions[1]], "Перевод со счета на счет"),
        ([full_transactions[2]], "Перевод со счета на счет"),
        ([full_transactions[3]], "Перевод с карты на карту"),
        ([full_transactions[4]], "Перевод организации"),
    ],
)
def test_transaction_descriptions(transaction: list[dict], result: str) -> None:
    """Тест функции transaction_descriptions"""
    assert next(transaction_descriptions(transaction)) == result


def test_number_generator() -> None:
    """Тест функции number_generator."""
    expected = [100, 101, 102, 103, 104, 105, 106, 107]
    # Создаём генератор и берём первые 8 значений.
    generator = number_generator(100)
    fact_result = list(next(generator) for _ in range(8))
    assert expected == fact_result


expected_result = [
    [
        "0000 0000 0000 0000",
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
    ],
    [
        "7079 2345 2343 4560",
        "7079 2345 2343 4561",
    ],
    [],
]


@pytest.mark.parametrize(
    "start, stop, exception",
    [
        (0, 2, expected_result[0]),
        (7079234523434560, 7079234523434561, expected_result[1]),
        (10000000000000000, 10000000000000001, expected_result[2]),
    ],
)
def test_card_number_generator(start: int, stop: int, exception: list[str]) -> None:
    """Тест функции card_number_generator"""
    generator = list(card_number_generator(start, stop))
    assert generator == exception
