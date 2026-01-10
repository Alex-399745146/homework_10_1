import json


def get_info_operations(file_path: str) -> list:
    """
    Принимает путь до лог_файла.json
    :return:
    Возвращает список словарей об трансакциях из файла
    """
    try:

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if type(data) is list and len(data) > 0:
            return data
        else:
            return []

    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка чтения JSON из файла '{file_path}'.")
        return []
    except Exception as exc:
        print(f"Произошла непредвиденная ошибка: {exc}")
        return []


if __name__ == "__main__":
    file_path = "C:/Python/Projects/homework_10_1/data/operations.json"

    print(get_info_operations(file_path))
