"""
Файл(модуль) processing.py
Этот модуль будет содержать функции обработки данных.
"""


def filter_by_state(array_operations: list, status: str = "EXECUTED") -> list:
    """
    Принимает список словарей и опционально значение для ключа
    state по умолчанию 'EXECUTED'.
    Возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """
    select_operations = []

    for operation in array_operations:
        if operation["state"] == status:
            select_operations.append(operation)

    return select_operations


def sort_by_date(positions: list[dict], direct_sort: bool = True) -> list:
    """
    Принимает список словарей и необязательный параметр, задающий
    порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате (date).
    """
    ls_sorted = sorted(positions, key=lambda position: position["date"], reverse=direct_sort)

    return ls_sorted
