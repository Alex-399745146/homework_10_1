"""
Файл(модуль) processing.py
Этот модуль будет содержать функции обработки данных.
"""


def filter_by_state(ls_positions: list, status: str = "EXECUTED") -> list:
    """
    Принимает список словарей и опционально значение для ключа
    state по умолчанию 'EXECUTED'.
    :return:
    Возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """
    new_ls_position = []

    for dict_position in ls_positions:
        if dict_position["state"] == status:
            new_ls_position.append(dict_position)

    return new_ls_position


def sort_by_date(positions: list[dict], direct_sort: bool=True) -> list:
    """
    Принимает список словарей и необязательный параметр, задающий
    порядок сортировки (по умолчанию — убывание).
    :return:
    Возвращает новый список, отсортированный по дате (date).
    """
    ls_sorted = sorted(positions, key=lambda position: position['date'], reverse=direct_sort)

    return ls_sorted
