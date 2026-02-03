"""
Файл main.py
Основной файл исполнения.
"""
import os
import pandas as pd

from dotenv import load_dotenv
from src.utils import get_info_operations
from src.data_extractor import get_info_csv, get_info_xlsx
from src.filtered_transactions import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency

def main():
    head_message_ai = '\033[31mПрограмма:\033[0m'
    head_message_you = '\033[32mПрограмма: \033[0m'
    menu_item = None
    status = None
    answer_sort = None
    direction = None
    answer_currency = None
    answer_search = None
    answer_text = None

    # Опрос для выдачи результата:
    # Вопрос №1 откуда берем данные.

    print(f'''{head_message_ai} Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла''')

    while menu_item not in ['1', '2', '3']:
        menu_item = input(head_message_you)

    name_file = {'1': 'JSON', '2': 'CSV', '3': 'XLSX'}

    if menu_item == '1':
        data_file = get_info_operations(file_json_path)
    elif menu_item == '2':
        data_file = get_info_csv(file_csv_path)
    else:
        data_file = get_info_xlsx(file_xlsx_path)

    for data in data_file:  ###
        print(data)         ###

    print(f'\n{head_message_ai} Для обработки выбран {name_file[menu_item]}-файл.\n')

    # Вопрос №2 выбор статуса интересующих операций.

    print(f'''{head_message_ai} Выберите статус, по которому необходимо выполнить фильтрацию.\n
        Выберите необходимый пункт меню:
        1. EXECUTED
        2. CANCELED
        3. PENDING
            * или введите статус вручную, регистр неважен.''')

    while status not in ['1', '2', '3', 'EXECUTED', 'CANCELED', 'PENDING']:
        status = input(head_message_you).upper()

    if status.isdigit():
        name_status = {'1': 'EXECUTED', '2': 'CANCELED', '3': 'PENDING'}
        flag_status = name_status[status]
    else:
        flag_status = status

    transactions = filter_by_state(data_file, flag_status)

    for transaction in transactions:
        print(transaction)

    print(f'\n{head_message_ai} Операции отфильтрованы по статусу "{flag_status}".\n')

    # Вопрос №3 уточнения выборки операций сортировки.

    print(f'''{head_message_ai} Отсортировать операции по дате? Да/Нет\n
        Выберите необходимый пункт меню:
        1. Да
        2. Нет
            * или введите ответ вручную, регистр неважен.''')

    while answer_sort not in ['1', '2', 'ДА', 'НЕТ']:
        answer_sort = input(head_message_you).upper()

    if answer_sort == '1' or answer_sort == 'ДА':

        print(f'''\n{head_message_ai} Отсортировать по возрастанию или по убыванию?\n
        Выберите необходимый пункт меню:
        1. по возрастанию
        2. по убыванию''')

        while direction not in ['1', '2']:
            direction = input(head_message_you)

        if direction == '1':
            sorting_direction = False
            text_direction = 'по возрастанию'

        else:
            sorting_direction = True
            text_direction = 'по убыванию'

        transactions = sort_by_date(transactions, sorting_direction)


        for transaction in transactions:
            print(transaction)

        print(f'\n{head_message_ai} Отсортирован {text_direction}.\n')

    else:

        print(f'\n{head_message_ai} Сортировка по дате не применялась.\n')

    # Вопрос №4 фильтрация по валюте.

    print(f'''{head_message_ai} Выводить только рублевые транзакции? Да/Нет\n
        Выберите необходимый пункт меню:
        1. Да
        2. Нет''')

    while answer_currency not in ['1', '2']:
        answer_currency = input(head_message_you)

    if answer_currency == '1':
        transactions = filter_by_currency(transactions, 'RUB')

        for transaction in transactions:
            print(transaction)

        print(f'\n{head_message_ai} Произведена фильтрация по валюте.\n')

    else:
        print(f'\n{head_message_ai} Фильтрация по валюте не производилась.\n')

    # Вопрос №5 фильтрация по фабуле в описании трансакций.

    print(f'''\n{head_message_ai} Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n
        Выберите необходимый пункт меню:
        1. Да
        2. Нет\n''')

    while answer_search not in ['1', '2']:
        answer_search = input(head_message_you)

    if answer_search == '1':
        print('\nВведи текст для поиска:\n')
        while answer_text is None:
            answer_text = str(input(f'{head_message_you}'))
        transactions = process_bank_search(transactions, answer_text)


        print(len(transactions))
        # for transaction in transactions:
        #     print(transaction)

        print(f'\n{head_message_ai} Фильтрация по тексту произведена.\n')

    else:

        for transaction in transactions:
            print(transaction)

        print(f'\n{head_message_ai} Фильтрация по тексту не производилась.\n')


    # Вопрос №6
    # Вопрос №7

load_dotenv()  # Загрузка переменных из .env-файла.
file_json_path = os.getenv("FILE_PATH", "default_log_file.json")
file_csv_path = os.getenv("FILE_PATH_CSV", "default_log_file.csv")
file_xlsx_path = os.getenv("FILE_PATH_XLSX", "default_log_file.xlsx")

main()
