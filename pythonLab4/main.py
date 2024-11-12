""" Главный файл запуска всех методов лабораторной работы"""
from Classes.Join_List import Join_List
from Classes.CheckData import CheckData
from Classes.File_Method import multiplit_table_simple, process_numbers
from Classes.File_Method import multiplit_table_hard
from Classes.File_Method import file_test
from Classes.File_Method import file_update_method
from Classes.Home import Home

if __name__ == "__main__":
    print("Start Program")
    print("Всего в программе 9 шагов для проверки генераций исключений в Python \n")
    numbers = int(input("Введите шаг: "))
    match numbers:
        case 1:
            # Шаг 1
            object_List = Join_List()
            object_List.list_summ(4)  #1
        case 2:
            # Шаг 2
            multiplit_table_simple(5, 500)  #5,5
        case 3:
            # Шаг 3
            multiplit_table_hard(5, 5)  #5,500
        case 4:
            # Шаг 4
            object_Check = CheckData()
            object_Check.check_int(1)
            object_Check.check_file("E:\\AILab5\\Prolog\\")  #myfile.txt
            object_Check.check_input("Напиши текс")
        case 5:
            # Шаг 5
            list_int = []
            for i in range(10):
                list_int.append(input("Введите число: "))
            process_numbers()
        case 6:
            # Шаг 6
            print("Этот шаг информативный."
                  " Дело в том, что в предыдущих шагах уже реализованы пользовательские "
                  "исключения через вызов raise <Тип Исключения>(Текст Исключения)")
            print("Например на шаге 4 реализованы исключения типа :"
                  " Exception - общий, SyntaxError - Ошибка синтаксиса")
            print("Для примера сделаем третье исключение через открытие файла")
            file_test('myfile.txt')
        case 7:
            # Шаг 7
            file_update_method(file_test('myfile.txt'))
        case 8:
            # Шаг 8
            home = Home()
            home.entrance(1274)  #1247
