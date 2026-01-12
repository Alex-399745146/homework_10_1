"""
Файл test_external_api.py
Содержит кейсы для тестирования модуля external_api.py
"""

from unittest.mock import MagicMock, patch

from src.external_api import get_convert_amount


@patch("requests.get")
def test_get_convert_amount(mock_get: MagicMock, fixture_operation: list, fixture_response_api: dict) -> None:
    # Без обращения к публичным функциям.
    assert get_convert_amount(fixture_operation[0]) == "31957.58"
    # Заблокированное обращение к API.
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = fixture_response_api
    assert get_convert_amount(fixture_operation[1]) == 643311.1
