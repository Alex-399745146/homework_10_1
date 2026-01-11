import json
import os

from dotenv import load_dotenv


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
    load_dotenv()  # Загрузка переменных из .env-файла.
    file_path = os.getenv("FILE_PATH", "default_log_file.json")
    data = get_info_operations(file_path)

    for line in data:
        print()
        for key, value in line.items():
            print(key, ":", value)
