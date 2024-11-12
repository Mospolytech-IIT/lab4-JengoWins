"""Набор методов, которые выполняют ту или иную часть функций лабораторной работы"""
"""По сути это методы, которым особо не требуется находится 
в каком-либо наборе для описание большого объекта класса"""


def multiplit_table_simple(param1, param2):
    """Генерация таблицы умножения до 100"""
    """Стоит обратить внимание, что PyLint жалуется на генерацию исключения Exception"""
    """Это предупреждение не было пофиксино, связи с требованием задания"""
    try:
        result = param2 * param1
        if result <= 100:
            print(f"Итоговый результат умножения {param1}*{param2}={result}")
        else:
            raise Exception("Превышен лимит. Это уже не простая таблица умножения")
    except Exception as e:
        print(e)


def multiplit_table_hard(param1, param2):
    """Генерация таблицы умножения свыше 100"""
    """Стоит обратить внимание, что PyLint жалуется на генерацию исключения Exception"""
    """Это предупреждение не было пофиксино, связи с требованием задания"""
    try:
        result = param2 * param1
        if result > 100:
            print(f"Итоговый результат умножения {param1}*{param2}={result}")
        else:
            raise Exception("Лимит умножения довольно мал. Это уже не сложная таблица умножения")


    except Exception as e:
        print(e)
    finally:
        print("Обратите внимание, что для работы с простой таблицей умножения есть Шаг 3 \n")
        print("Завершаю работу")


def file_test(path):
    """Демонстрирует работу с исключениями файловой системы."""
    try:
        file = open(path, 'r+')
        raise IOError("Ошибка открытия файла. Создадим новый. \n")
    except IOError:
        file = open(path, 'w+')
        print("Как мы видим, нас перекинуло в исключение типа IOError")
        return file


def file_update_method(file):
    """Метод, что позволяет обновить документ"""
    try:
        print("Давайте через другой метод реализуем чтение-запись")
        message = input("Введите строку для записи: ")
        if message != "":
            file.write(message)
            file.close()
        else:
            raise KeyboardInterrupt("Ошибка. Строка пустая")
    except IOError as e:
        print("Ошибка файловой системы: ", e)


def process_numbers(*args):
    try:
        # Проверка на наличие аргументов
        if not args:
            raise ValueError("Аргументы не найдены. Пожалуйста, введите аргументы")

        total = []
        for num in args:
            # Проверка на то, является ли аргумент числом
            if isinstance(num, (int, float)):
                total.append(num)
            else:
                raise TypeError(f"Ошибка типа: {num}. Аргументы должны быть числовыми.")
        print(f"Список значений: {total}")

    except ValueError as ve:
        print(f"ValueError: О боже мой, число не то {ve}")
    except TypeError as te:
        print(f"TypeError: Ооо нет, тип не тот{te}")
    finally:
        print("Function execution completed.")
