# PET-project | Домашний обучающий проект

# Widget for banking transactions | Виджет для банковских операций

---

### Описание проекта 
**_<span style="color: green;">Это моя домашняя работа выполняемая по этапно, по таскам заданий в skypro. 
~~В домашнем задании этого урока~~ я продолжил работать над проектом по методике - "GitFlow" с Git,
разделяя код на ветки и сразу объясню что в целях наработки практики чаше создаю коммит(ы)
и делаю больше веток, с каждой домашней работой будет добавляться что-то новое. Структура директа в проекте как в
библиотеках (все модули в деректории src)</span>_**

---

# Содержание
*(гиппер-ссылки)*
- [Стек-технологий >>](#стек-технологий)
- [Реализация функций >>](#реализация-функций)
- [QA-tests >>](#qa-tests)
- [FAQ >>](#faq)
- [To do >>](#to-do)
- [Автор проекта >>](#команда-проекта)
- [Источники информации >>](#источники-информации)

---
## Стек-технологий
- [Использован интерпретатор Python 3.14.](https://www.python.org/downloads/release/python-3140/)
- [Проект развёрнут через инструмент виртуального пространства Poetry.](https://python-poetry.org/)
- [Автоматизация обеспечения качества кода](https://habr.com/ru/companies/otus/articles/750214/)
- [Удалённый репозиторий проекта на GitHub тут.](https://github.com/Alex-399745146/homework_10_1)
- [Работа с Git велась по методу GitFlow](https://habr.com/ru/articles/767424/)
- [Написаны QA-тесты для фреймворк pytest](https://habr.com/ru/companies/otus/articles/480186/)
- [Опробована методология TDD (Test Driven Development)](https://habr.com/ru/companies/ruvds/articles/450316/)
- [Для оценки code coverage - применяем библиотеку cov из pytest](https://habr.com/ru/articles/836366/)

---
## Реализация-функций
### Модуль <span style="color: red;">generators.py</span>
    Реализованно в этом модуле две функции:
        1. Функция выборки трансакции измассива по виду валюты filter_by_currency.
        2. Функция выводит описание финансовых опираций через ленивый запросы transaction_descriptions.
        3. Вспомогательная генераторная функция number_generator - генератор чисел от 1 до 16 разрядного числа. 
        4. Генераторная функция номера карт в формате 9999 9999 9999 9999 (card_number_generator).

#### Для проверки функций filter_by_currency и transaction_descriptions:
```
transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)
```
### Модуль <span style="color: red;">masks.py</span>
    Реализованно в этом модуле две функции:
        1. Функцию маскировки номера банковской карты get_mask_card_number.
        2. Функцию маскировки номера банковского счета get_mask_account.

### Модуль <span style="color: red;">processing.py</span>
    Этот модуль будет содержать функции обработки данных.
        1. filter_by_state принимает список словарей и опционально значение для ключа state по умолчанию 'EXECUTED'. Возвращает новый
           список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
        2. sort_by_date принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
           Возвращает новый список, отсортированный по дате (date).

### Модуль <span style="color: red;">widget.py</span>
    Cодержит функции для работы с новыми возможностями приложения.
        1. mask_account_card обрабатывает информацию как о картах, так и о счетах. Принимает один аргумент — строки,
           содержащую тип и номер карты или счета. Возвращает строку с замаскированным номером карты или счёта.
        2. get_date принимает на вход строку '2024-03-11T02:26:18.671407' и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'.

### Модуль <span style="color: red;">main.py</span>
    В файле main.py реализуется основная логика виджета.
#### Проверочный код работы функций из модуля main.py
```
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

card_number = "7000792289606361"

account_number = "73654108430135874305"

open_string = "Visa Platinum 7000792289606361"
open_string_1 = "Счет 73654108430135874305"

date_time = "2024-03-11T02:26:18.671407"


print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
print(mask_account_card(open_string))
print(mask_account_card(open_string_1))
print(get_date(date_time))

print("Тест следующих новых фитчей прикрученых к проекту согласно тасков домашки по 10_1")

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
```
---

## QA-tests
### В тестах использованы фикстуры и параметризация.

- [x] Написаны тесты ко всем функциям проекта.
- [x] Модули тестируются в отдельных тестовых файлах.
- [x] Функциональный код покрыт тестами более чем на 80%.
- [x] При запуске тестов командой pytest все тесты завершаются успешно.


### Запуск тестов
```sh
pytest -v
```
```sh
pytest --cov
```
### Через Poetry запуск теста
```sh
poetry run pytest --cov
```
- [x] В репозитории есть папка с отчетом покрытия тестами в формате HTML.

---
## To do
### `Работа с GitHub`
- [x] Домашка сдана через pull request из ветки домашней работы в ветку develop.
- [x] В коммиты не добавлены игнорируемые файлы.
- [x] README-файл дополнен информацией о тестировании.
### `Тестирование`
- [x] Написаны тесты ко всем функциям проекта.
- [x] Модули тестируются в отдельных тестовых файлах.
- [x] Функциональный код покрыт тестами более чем на 80%.
- [x] При запуске тестов командой pytest все тесты завершаются успешно.
- [x] В репозитории есть папка с отчетом покрытия тестами в формате HTML.
### `Фикстуры и параметризация`
- [x] В тестах используются фикстуры для генерации данных для теста.
- [x] В тестах используется параметризация для проверки различных кейсов работы функций.
### `Оформление кода`
- [x] При запуске линтеров Flake 8 и mypy выдается не более 4 ошибок.
### `Работа с линтерами и форматерами`
- [x] При вызове isort форматируется не более 1 импорта.

---
## FAQ
Вывод структуры проекта
```sh
dir
```
```sh
Get-ChildItem -Recurse -Depth 1
```
Узнать версию интерпретатора Python для проекта надо 3.14
```sh
py --version
```
Установка Poetry
```sh
pip install poetry
```
Активация виртуального пространства
```sh
.\.venv\Scripts\activate
```
Проверка кода линтерами
```sh
flake8 .
```
```sh
isort .
```
```sh
black .
```
```sh
mypy .
```
---

## Команда проекта

- студент skypro [Бачевский Александр](https://github.com/Alex-399745146) — факультет Back-End Dev

![letter](https://upload.wikimedia.org/wikipedia/commons/2/2a/High-contrast-emblem-mail.svg)
bachevskiiaa@gmail.com

---
## Источники информации

Ресурс       | Название 
-------------|----------------------------
Skypro       | https://my.sky.pro 
Я.Практикум  | https://practicum.yandex.ru 
Stepik       | https://stepik.org

[<span style="color: green;">Skypro</span>](https://my.sky.pro/student-cabinet/stream-lesson/197233/homework-requirements)
[<span style="color: green;">Я.Практикум</span>](https://practicum.yandex.ru/)
[<span style="color: green;">Stepik</span>](https://stepik.org/learn?auth=login)
