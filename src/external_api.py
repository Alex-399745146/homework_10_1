"""
Принимает на вход транзакцию и возвращает сумму транзакции
(amount) в рублях, тип данных — float.
Если транзакция была в USD или EUR, происходит обращение
к внешнему API для получения текущего курса валют и
конвертации суммы операции в рубли.
"""
import requests
import json


API_KEY = 'igbRaoSo61jT3RxKFmVzf2viHC9e24MT'


def convert_amount(amount):
    API_KEY = 'igbRaoSo61jT3RxKFmVzf2viHC9e24MT'
    # обязательный параметр — трехбуквенный код валюты, из которой происходит конвертация
    currency_in = 'USD'
    # обязательный параметр — трехбуквенный код валюты, в которую происходит конвертация
    currency_out = 'RUB'

    url = f'https://api.apilayer.com/exchangerates_data/convert?to={currency_out}&from={currency_in}&amount={amount}'
    headers = {'apikey': API_KEY}

    response = requests.request("GET", url, headers=headers)

    status_code = response.status_code
    data = response.json()
    return data, status_code

data, status = convert_amount(100)
print('Status_server:', status)
for _ in data:
    print(_, ':', data[_])