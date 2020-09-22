# Список импортов
from Graph import Graph
from Interface import Interface

# Консольное меню программы
menu = Interface()
# Вызов метода отображения главного меню
menu.interface_Main()

# Цикл обработки команд
while True:
    # Ввод выбранного действия
    Step = menu.input_Controller()

    # Задание 1
    if Step == 1:
        print("")
        # Создание объекта класса Граф
        graph = Graph()
        menu.interface_Task1()
        while True:
            Step = menu.input_Controller()

            # Ввести неоринетированный граф с клавиатуры
            if Step == 1:
                graph.input_Undirected_Graph()
                #print(graph.undirected_cycle_Detector())
                menu.interface_Task1()

            # Ввести граф из файла
            elif Step == 2:
                graph.file_Undirected_Graph("Task1.txt")
                menu.interface_Task1()

            # Вывести граф
            elif Step == 3:
                graph.output_Graph()
                if graph._edges_value > 0:
                      graph.nx_Undirected_Graph_Draw()
                menu.interface_Task1()

            # Удалить из графа N вершин и проверить его на древовидность
            elif Step == 4:
                graph.tree_Detector()
                menu.interface_Task1()

            # Выход в главное меню
            elif Step == 5:
                print("")
                menu.interface_Main()
                break

            # Остальные случаи
            else:
                print("Ошибка ввода")
                print("")
        
    # Задание 2
    elif Step == 2:
        print("")
        # Создание объекта класса Граф
        graph = Graph()
        menu.interface_Task2()
        while True:
            Step = menu.input_Controller()

            # Ввести ориентированный граф с клавиатуры
            if Step == 1:
                graph.input_Directed_Graph()
                #print(graph.undirected_cycle_Detector())
                menu.interface_Task2()

            # Ввести граф из файла
            elif Step == 2:
                graph.file_Directed_Graph("Task2.txt")
                menu.interface_Task2()

            # Вывести граф
            elif Step == 3:
                graph.output_Graph()
                if graph._edges_value > 0:
                      graph.nx_Directed_Graph_Draw()
                menu.interface_Task2()

            # Посчитать количество всех путей между вершинами графа
            elif Step == 4:
                graph.all_Graph_Paths()
                menu.interface_Task2()

            # Выход в главное меню
            elif Step == 5:
                print("")
                menu.interface_Main()
                break

            # Остальные случаи
            else:
                print("Ошибка ввода")
                print("")

    # Задание 3
    elif Step == 3:
        print("")
        # Создание объекта класса Граф
        graph = Graph()
        menu.interface_Task3()
        while True:
            Step = menu.input_Controller()

            # Ввести ориентированный или неориентированный граф с клавиатуры
            if Step == 1:
                graph.input_Directed_Graph()
                #print(graph.undirected_cycle_Detector())
                menu.interface_Task3()

            # Ввести граф из файла
            elif Step == 2:
                graph.file_Undirected_Graph("Task3.txt")
                menu.interface_Task3()

            # Вывести граф
            elif Step == 3:
                graph.output_Graph()
                if graph._edges_value > 0:
                      graph.nx_Directed_Graph_Draw()
                menu.interface_Task3()

            # Определить, содержит ли граф Гамильтонов цикл
            elif Step == 4:
                graph.eulerian_Detector()
                menu.interface_Task3()

            # Выход в главное меню
            elif Step == 5:
                print("")
                menu.interface_Main()
                break

            # Остальные случаи
            else:
                print("Ошибка ввода")
                print("")

    # Выход из программы
    elif Step == 4:
        print("Программа завершена")
        break

    # Остальные случаи
    else:
        print("Ошибка ввода")
        print("")
