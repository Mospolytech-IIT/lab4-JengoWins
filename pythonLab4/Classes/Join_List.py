"""Класс, который генерирует лист значений с возможностью генерации суммы"""


class Join_List:
    """Поинт начального значения и реузьтат обработки суммы"""
    param1: int
    result: int

    def __init__(self):
        self.param1 = 5
        self.result = 0

    def check_summ(self, param_int):
        """Проверка суммы? Не может этого быть"""
        try:
            if int(param_int):
                self.result = self.param1 + param_int
                print(f"Проверка числа через сумму: {self.result}")
            else:
                raise TypeError("ГГ, ну что тут сказать, купите мне число, а не строку")
        except TypeError:
            print("Поверка прошла неудачно.")

    def list_summ(self, param_int):
        """Лист, что создает произвольный список и создает сумму значений"""
        try:
            list_int = []
            for i in range(param_int):
                number = input(f"Введите {i} число: ")
                print("\n")
                #list.append(self.check_summ(int(number))) #Для починки первой функции

                if i != param_int - 1:
                    list_int.append(self.check_summ(int(number)))
                else:
                    list_int.append(self.check_summ(number))

            for i in range(param_int):
                #if i < param_int-1: #Для починки
                if list_int[i] < list_int[i + 1]:
                    self.result = list_int[i] + list_int[i + 1]
                    print(f"Сумма {i} и {i + 1} равно: ", self.result)
                else:
                    self.result = list_int[i] - list_int[i + 1]
                    print(f"Сумма {i} и {i + 1} равно: ", self.result)
        except (ValueError, TypeError):
            print("Переборка массива прошла неудачно.")
