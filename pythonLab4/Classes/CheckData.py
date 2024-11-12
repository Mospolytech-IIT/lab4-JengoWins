"""Класс методов, позволяющий просматривать вводимые данные """


class CheckData:
    """Класс, хранящий методы. Первоначально создает объект и передает сообщение о его создании"""
    def __init__(self):
        print("Generate Check")

    def check_int(self, param):
        """Проверка валидности числового параметра, путем его деления"""
        try:
            result = param / 5
            print(result)
            if result > 1.0:
                print("Итоговое значение: ", result)
            else:
                raise ValueError("SIMPLE NUMBER")

        except ValueError:
            print("Проблемы с преобразованием переменной.")
        except ZeroDivisionError:
            print("Проблемы с делением нулевого значения.")
        except TypeError as e3:
            print(f"Проблемы типизации. Это должно быть число: {e3}")
        finally:
            print("Завершаю работу \n")

    def check_file(self, filepath):
        """Запись и чтение файла"""
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                for message in file:
                    print(message, end="")
            message = input("Введите строку: ")
            with open(filepath, "a", encoding="utf-8") as file:
                file.write("\n" + message + "\n")
            print("\n")
        except FileExistsError as ex1:
            print("Ошибка - попытка создать файл: ", ex1)
        except FileNotFoundError as ex2:
            print("Ошибка - файл или директория не существует: ", ex2)
        except ValueError as ex3:
            print(ex3)

    def check_input(self, param):
        "Проверяет ввод данных пользователя для дубликации предложения"
        try:
            if param == "Напиши текст":
                print("Окей, понял, напиши текст и я его продублирую \n")
                text = input("Введите текст: ")
                if text == "":
                    raise ValueError("Ошибка. Строка пустая")
                print("Дублирую: ", text)
            else:
                raise SyntaxError()
        except KeyboardInterrupt:
            print("Проблемы с приостановкой ввода текста.")
        except SyntaxError:
            print("Проблемы синтаксиса.")
        except ValueError as e3:
            print(f"Проблемы возвращения. Число не должно быть ниже 1. Ошибка: {e3}")
