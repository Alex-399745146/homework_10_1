from datetime import datetime
from functools import wraps


name_file_logs = 'mylog.txt'


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

#name_file_logs
@log()
def my_function(x, y):
    """ Простая функция суммирования аргументов """
    return x + y

@log(name_file_logs)  # Без указания файла — вывод в консоль
def another_function(a, b, c=0):
    """Функция с именованными аргументами"""
    if a < 0:
        raise ValueError('ValueError')
    return a + b + c


my_function(1, 2)
another_function(3, 4, c=5)
another_function(-1, 2)
