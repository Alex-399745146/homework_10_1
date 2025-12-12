"""
В модуле decorators.py
Этот модуль будет использоваться для размещения декораторов.
"""
from datetime import datetime
from functools import wraps


log_file = 'mylog.txt'


def log(filename=None):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            timer_start = datetime.now()
            func_name = func.__name__

            try:
                result = func(*args, **kwargs)
                message = f'{func_name} ok'

            except ValueError as error_1:
                message = f'{func_name} error: {error_1}. Inputs: {args}'

            except Exception as error_2:
                message = f'{func_name} unexpected error: {error_2}. Inputs: {args}'

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            timer_delta = datetime.now() - timer_start
            data_log = f'{timestamp} {message} {timer_delta.microseconds} мксек\n'

            if filename:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(data_log)

            else:
                return print(data_log)

        return wrapper

    return decorator


@log(log_file)
def my_function(x, y):
    """ Простая функция суммирования аргументов """
    return x + y


my_function(1, 2)
