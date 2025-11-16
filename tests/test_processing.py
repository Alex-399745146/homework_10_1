"""
Файл test_processing.py
Содержит кейсы для тестирования модуля processing.py
со всеми его функциями.
"""
import re, pytest

from src.processing import filter_by_state, sort_by_date


# Параметризованный тест.
@pytest.mark.parametrize(
    'operation',
    [
        {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 132452323, 'state': 'CANCELED', 'date': '2020-09-12T21:27:25.241689'},
        {'id': 984357699, 'state': 'EXECUTED', 'date': '2022-03-14T09:21:33.419441'},
        {'id': 984394534, 'state': 'EXECUTED', 'date': '2017-12-14T08:23:38.419456'},
        {'id': 123432344, 'state': 'CANCELED', 'date': '2023-11-14T20:11:31.455141'},
        {'id': 234554322, 'state': 'EXECUTED', 'date': '2024-07-14T05:21:36.519841'},
        {'id': 768576858, 'state': 'CANCELED', 'date': '2025-01-14T08:25:33.317481'},
    ]
)
def test_filter_by_state(operation: dict) -> None:
    """Тест функции filter_by_state"""

    """Тесты входных данных"""
    volume_str_id = str(operation['id'])
    volume_str_date = operation['date']

    # Test входных данных id.
    assert len(volume_str_id) == 9, f'Длина входного id неверна: {volume_str_id}'
    assert volume_str_id.isdigit(), f'Входное id содержит буквы: {volume_str_id}'
    assert operation['id'] != 0 and str(operation['id'])[0] != '0', f'Некорректный id: {operation['id']}'

    # Test входных данных state.
    assert operation['state'] in ['EXECUTED', 'CANCELED'], f'Неверный статус операции: {operation['state']}'

    # Test входных данных date.
    date_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+$' # Регулярное выражение.
    assert re.match(date_pattern, volume_str_date), f'Неверный формат даты: {volume_str_date}'
    assert type(volume_str_date) == type('str'), f'Тип данных даты не str: {type(volume_str_date)}'

    """Тесты выходных данных"""
    volume_str_state = operation['state']

    if volume_str_state == 'CANCELED':
        select_operation = filter_by_state([operation], volume_str_state)[0]

        assert select_operation['state'] == volume_str_state

    elif volume_str_state == 'EXECUTED':
        select_operation = filter_by_state([operation])[0]

        assert select_operation['state'] == 'EXECUTED'

    out_data = filter_by_state([operation], volume_str_state)

    assert type(out_data) == type(list()), f'Выход данных не list(): {type(out_data)}'
    assert len(out_data[0]) == 3, f'Не верное количество ключей в словаре(3): {len(out_data)}'

    names_expected_keys = ['id', 'state', 'date']
    names_actual_keys = list(out_data[0].keys())

    assert names_expected_keys == names_actual_keys, \
        f'Неверные ключи. Ожидалось: {names_expected_keys}, получено: {names_actual_keys}'



def test_sort_by_date(fixture_list_operations: list[dict]) -> None:
    """Тест функции sort_by_date"""
    ls_sorted = sort_by_date(fixture_list_operations, direct_sort = True)
    fresh_operation = fixture_list_operations[-1] # Самое свежее событие.
    rev_sorted = sort_by_date(fixture_list_operations, direct_sort = False)

    assert len(fixture_list_operations) == len(ls_sorted), 'Потеря данных'
    assert ls_sorted[0] == fresh_operation, 'Неверная сортировка по убыванию'
    assert rev_sorted[-1] == fresh_operation, 'Неверная сортировка по возрастанию'
