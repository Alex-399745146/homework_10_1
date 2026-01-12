"""
Файл test_utils.py
Содержит кейсы для тестирования модуля utils.py
"""

from src.utils import get_info_operations


def test_get_info_operations(fixture_path: str) -> None:
    """Тест функции get_info_operations из utils.py"""
    # Тест входных данных.
    assert isinstance(fixture_path, str), "Ввод в функцию не строкового типа данных"
    assert ":" and "/" in fixture_path, "Не корректно указан путь к файлу с транс-акциями"

    # Тест выходных данных.
    result = get_info_operations(fixture_path)
    assert isinstance(result, list) and isinstance(result[0], dict), "get_info_operations() выдаёт не тот тип данных"
