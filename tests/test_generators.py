"""
Тестовый-модуль tests_generators.py
Содержит кейсы для тестирования функций модуля generators.py.
"""


def test_filter_by_currency(fixture_full_transactions, fixture_filter_name) -> None:
    """Тест функции filter_by_currency"""


def test_transaction_descriptions(fixture_full_transactions) -> None:
    """Тест функции transaction_descriptions"""


def test_number_generator(fixture_integer) -> None:
    """Тест функции number_generator"""


def test_card_number_generator(fixture_integer, fixture_separator: str = " ") -> None:
    """Тест функции card_number_generator"""
