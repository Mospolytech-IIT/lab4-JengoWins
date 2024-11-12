"""Класс, описывающий посведневную жизнь, после работы"""


class Home:
    """Домик, хранящий список занятий, комнат и пароль квартиры"""
    key_password: int
    list_room: list[str]
    list_action: list[str]

    def __init__(self):
        self.key_password = 1274
        self.list_room = ["Кухня", "Зал", "Комната"]
        self.list_action = []

    def entrance(self, password):
        """МетоД. что проверяет дверь на ключ"""
        try:
            if self.key_password == password:
                self.the_way()
            else:
                raise ValueError("Пароль не правильный. \n")
        except ValueError as e:
            print(e)

    def the_way(self):
        """Метод, который определяет комнату для пользователя"""
        try:
            room = input("Выберите комнату: ")
            room_id = 0
            if room != "":
                for i in range(len(self.list_room)):
                    if self.list_room[i] == room:
                        room_id = i
                        print("Exit")
                self.the_action(room_id)
            else:
                raise KeyboardInterrupt("Такой комнаты не существует. \n")
        except (ValueError, KeyboardInterrupt, TypeError) as e:
            print("Кажись что-то сломалось", e)

    def the_action(self, i):
        """Метод, который описывает действие пользователя в комнате"""
        try:
            match i:
                case 0:
                    self.list_action.append("Приготовить макароны")
                    self.list_action.append("Разогреть фатфуд")
                    self.list_action.append("Помыть посуду")
                case 1:
                    self.list_action.append("Сыграть на гитаре")
                    self.list_action.append("Потанцевать")
                    self.list_action.append("Посмотреть фильм")
                case 2:
                    self.list_action.append("Включить компьютре и поиграть")
                    self.list_action.append("Лечь спать")
                    self.list_action.append("Заняться своим хобби")
                case _:
                    print("Упс")
            action = input("Выберите действие: ")
            print(len(self.list_action))
            if action != "":
                for g in range(len(self.list_action)):
                    if self.list_action[g] == action:
                        print("Ваше действие - ", self.list_action[g])
            else:
                raise KeyboardInterrupt("Не существует такой команды. \n")
        except (ValueError, KeyboardInterrupt) as e:
            print(e)
