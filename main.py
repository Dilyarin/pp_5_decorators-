from pprint import pprint
from datetime import datetime
import os

BASE_PATH = os.getcwd()
LOGS_DIR_NAME = 'logs'
LOGS_FUNC1_NAME = 'sum'
LOGS_FUNC2_NAME = 'div'
LOGS_FILE_NAME = 'logs.txt'

# full_path = os.path.join(BASE_PATH, LOGS_DIR_NAME, LOGS_FILE_NAME)


# print(full_path)

def parametrized_decor(full_path):
    def decor(foo):
        def log_func(*args, **kwars):
            print('Код до вызова функции')
            res = foo(*args, **kwars)
            with open(full_path, 'a', encoding='utf-8') as file_obj:
                result = f"Вызов функции {foo.__name__}, дата и время вызова функции - {datetime.now()}, аргументы - {args}, результат - {res} \n"
                print(result)
                file_obj.write(result)
            print('Код после вызова функции')
        return log_func
    return decor


#
# def foo():
#     pass

@parametrized_decor(full_path=os.path.join(BASE_PATH, LOGS_DIR_NAME, LOGS_FUNC1_NAME, LOGS_FILE_NAME))
def summator(a, b, c):
    return (a+b+c)
    # print(f'Сумма равно {a+b+c}')

@parametrized_decor(full_path = os.path.join(BASE_PATH, LOGS_DIR_NAME, LOGS_FUNC2_NAME,LOGS_FILE_NAME))
def division(a, b):
    return a/b
    # print(f'Деление равно {a/b}')

if __name__ == '__main__':
    # summator=decor(summator)
    summator(1,8,4)
    summator(8,9,8)
    division(18,2)
    division(15,3)