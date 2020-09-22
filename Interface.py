# Класс интерфейса
class Interface:
    # Конструктор
    def __init__(self):
        pass
    # Главное меню:
    def interface_Main(self):
        print ("Главное меню:")
        print ("Выберите действие:")
        print ("1 - Первое задание")
        print ("2 - Второе задание")
        print ("3 - Третье задание")
        print ("4 - Выход из программы.")
        print("")
        pass

    # Задание 1:
    def interface_Task1(self):
        print ("Меню задания 1")
        print ("Выберите действие:")
        print ("1 - Ввести граф с клавиатуры")
        print ("2 - Прочитать граф из файла")
        print ("3 - Вывести граф")
        print ("4 - Проверить, будет ли граф являться деревом, если из него удалить N вершин")
        print ("5 - В главное меню")
        print("")
        pass

    # Задание 2:
    def interface_Task2(self):
        print ("Меню задания 2")
        print ("Выберите действие:")
        print ("1 - Ввести граф с клавиатуры")
        print ("2 - Прочитать граф из файла")
        print ("3 - Вывести граф")
        print ("4 - Посчитать количество путей между всеми вершинами ориентированного графа")
        print ("5 - В главное меню")
        print("")
        pass

    # Задание 3:
    def interface_Task3(self):
        print ("Меню задания 3")
        print ("Выберите действие:")
        print ("1 - Ввести граф с клавиатуры")
        print ("2 - Прочитать граф из файла")
        print ("3 - Вывести граф")
        print ("4 - Определить, содержит ли граф Эйлеров цикл")
        print ("5 - В главное меню")
        print("")
        pass

    # Защита от некорректного ввода:
    def input_Controller(self):
        while True:
            try:
                Value = int(input(">>> "))
                if Value > 0:
                    return Value
                else:
                    print("Ошибка ввода!")
            except ValueError:
                print("Ошибка ввода!")
        print("")