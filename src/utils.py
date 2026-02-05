"""Модуль utils.py содержит функции обработчики данных по трансакциям"""

import json
import logging
import os

from dotenv import load_dotenv

# Переменные для формирования точного пути до лог-файла.
path_inside_project = os.path.dirname(os.path.abspath(__file__))
path_inside_logs = "../logs/utils.log"

# Создаем путь до файла логов относительно текущей директории.
full_path = os.path.join(path_inside_project, path_inside_logs)
abs_path = os.path.abspath(full_path)


logger = logging.getLogger("utils")  # pragma: no cover
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename=abs_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_info_operations(file_path: str) -> list:
    """
    Принимает путь до лог-файла формата json.
    Возвращает список словарей об трансакциях из файла.
    """
    logger.info(f"Функция приняла адрес до лог-файла трансакций: {file_path}")
    try:

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        logger.debug("Данные из указанного файла считаны корректно")

        if type(data) is list and len(data) > 0:
            logger.debug("Данные не пустые, информация выдана функцией успешно")

            return data
        else:
            logger.warning("Данные пустые, функция выдала пустой список данных")

            return []

    except FileNotFoundError as e:
        logger.error(e, exc_info=True)

        return []

    except Exception as e:
        logger.error(e, exc_info=True)

        return []


if __name__ == "__main__":  # pragma: no cover
    load_dotenv()  # Загрузка переменных из .env-файла.
    file_path = os.getenv("FILE_PATH", "default_log_file.json")
    data = get_info_operations(file_path)

    for line in data:
        print()
        for key, value in line.items():
            print(key, ":", value)
