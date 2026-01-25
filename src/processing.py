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


if __name__ == "__main__":  # pragma: no cover
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    [print(f"{i}") for i in filter_by_state(data, "CANCELED")]
    print()
    [print(f"{i}") for i in filter_by_state(data)]
    print()

    print("Согласно таска сортировка на убывание.")
    for i in sort_by_date(data):
        print(i["date"][:10])
