# Список импортов
import re
import networkx as nx
import matplotlib.pyplot as plt
import copy

# Класс графа
class Graph(object):
    # Конструктор
    def __init__(self, edges_value = 0 , vertex_value = 0):
        # Граф строится на основе словаря
        self._edges = {}
        # Количество рёбер
        self._edges_value = edges_value

    # Метод заполнения направленного графа c клавиатуры
    def input_Directed_Graph(self):
        self._edges.clear()
        print("Введите количество рёбер графа: ")
        self._edges_value = self._graph_Edges_Input_Controller()
        print("Последовательно введите ребра графа: ")
        for i in range(self._edges_value):
            print("Идет ввод ", i + 1, " ребра графа: ")
            current_node = self.lexema_Filter()
            next_node = self.lexema_Filter()
            current_list = []
            current_list.append(next_node)
            if current_node in self._edges:
                if next_node not in self._edges[current_node]:
                    self._edges[current_node].append(next_node)
            else:
                self._edges[current_node] = current_list
        print("Граф был успешно заполнен")
        print("")

    # Метод заполнения ненаправленного графа с клавиатуры
    def input_Undirected_Graph(self):
        self._edges.clear()
        print("Введите количество рёбер графа: ")
        self._edges_value = self._graph_Edges_Input_Controller()
        print("Последовательно введите ребра графа: ")
        for i in range(self._edges_value):
            print("Идет ввод ", i + 1, " ребра графа: ")
            current_node = self.lexema_Filter()
            next_node = self.lexema_Filter()
            current_list_first = []
            current_list_second = []
            current_list_first.append(next_node)
            current_list_second.append(current_node)
            if current_node in self._edges:
                if next_node not in self._edges[current_node]:
                    self._edges[current_node].append(next_node)
            else:
                self._edges[current_node] = current_list_first
            if next_node in self._edges:
                if current_node not in self._edges[next_node]:
                    self._edges[next_node].append(current_node)
            else:
                self._edges[next_node] = current_list_second
        print("Граф был успешно заполнен")
        print("")

    # Метод заполнения неоринетированного графа из файла
    def file_Undirected_Graph(self, name):
        self._edges.clear()
        file = open(name)
        for line in file:
            pattern = re.compile("\n")
            match = pattern.search(line)
            if match:
                line = line[0:-1]
            values = line.split(' ')
            current_node = values[0]
            next_node = values[1]
            current_list_first = []
            current_list_second = []
            current_list_first.append(next_node)
            current_list_second.append(current_node)
            if current_node in self._edges:
                if next_node not in self._edges[current_node]:
                    self._edges[current_node].append(next_node)
            else:
                self._edges[current_node] = current_list_first
            if next_node in self._edges:
                if current_node not in self._edges[next_node]:
                    self._edges[next_node].append(current_node)
            else:
                self._edges[next_node] = current_list_second
            self._edges_value += 1
        print("Граф был успешно считан")
        print("")

    # Метод заполнения ориентированного графа из файла
    def file_Directed_Graph(self, name):
        self._edges.clear()
        file = open(name)
        for line in file:
            pattern = re.compile("\n")
            match = pattern.search(line)
            if match:
                line = line[0:-1]
            values = line.split(' ')
            current_node = values[0]
            next_node = values[1]
            current_list_first = []
            current_list_second = []
            current_list_first.append(next_node)
            current_list_second.append(current_node)
            if current_node in self._edges:
                if next_node not in self._edges[current_node]:
                    self._edges[current_node].append(next_node)
            else:
                self._edges[current_node] = current_list_first
            self._edges_value += 1
        print("Граф был успешно считан")
        print("")

    # Метод вывода графа
    def output_Graph(self):
        if self._edges_value > 0:
            print("Введённый граф: {")
            for key in self._edges:
                print(key, ":", self._edges[key])
            print("} Вывод графа окончен ")
            print("")
        else:
            print("Граф не был введён ")
            print("")

    # Метод защиты от некорректного ввода чисел
    def _graph_Edges_Input_Controller(self):
        while True:
            try:
                value = int(input(">>> "))
                if value > 0:
                    return value
                else:
                    print("Ошибка ввода")
                    print("")
            except ValueError:
                print("Ошибка ввода")
                print("")

    # Метод фильтра лексем
    def lexema_Filter(self):
        # Паттерн всего, что  является лексемой
        Pattern = r'[\.a-zA-Zа-яА-я0-9]+'
        while True:
            lexem = input(">>> ")
            if re.search(Pattern, lexem):
                return lexem
            else:
                print("Ошибка ввода")
                print("")

    # Метод удаления вершины из графа
    def vertex_Remove(self):
        if self._edges is not None:
            print("")
            print("Введите удаляемую вершину")
            remove_vertex = self.lexema_Filter()
            if remove_vertex in self._edges.keys():
                self._edges.pop(remove_vertex)
                for vertex in self._edges:
                    if remove_vertex in self._edges[vertex]:
                        self._edges[vertex].remove(remove_vertex)
                self._edges_value -= 1
                print("Вершина удалена")
            else:
                print("Введенной вершины не существует в графе")
        else:
            print("Граф пуст")

    # Метод определния есть ли в графе любые циклы
    def directed_cycle_Detector(self):
        path = set()
        visited = set()
        # Рекурсивный обход графа
        def visit(vertex):
            if vertex in visited:
                return False
            visited.add(vertex)
            path.add(vertex)
            for neighbour in self._edges.get(vertex, ()):
                if neighbour in path or visit(neighbour):
                    return True
            path.remove(vertex)
            return False
        return any(visit(vertex) for vertex in self._edges)

    # Метод проверки наличия циклов в неориентированном графе (т.е. игнорируя циклы вида {a -> b, b -> a})
    def undirected_cycle_Detector(self):
        marker = {vertex : False for vertex in self._edges}
        cycle = [False]
        # Рекрусивный обход графа
        def visit(vertex, cycle, pred_node, marker):
            if cycle[0]:
                return
            marker[vertex] = True
            for jertex in self._edges[vertex]:
                if marker[jertex] and jertex != pred_node:
                    cycle[0] = True
                    return
                if not marker[jertex]:
                    visit(jertex, cycle, vertex, marker)
        # Вызов обхода графа
        for vertex in self._edges:
            if not marker[vertex]:
                visit(vertex, cycle, vertex, marker)
            if cycle[0]:
                break
        return cycle[0]

    # Приведение графа из неориентированного вида к ориентированному
    def utod(self):
        graph = {}
        for vertex in self._edges:
            graph[vertex] = []
            values = self._edges.get(vertex)
            for value in values:
                if value not in graph.keys():
                    graph[vertex].append(value)
            if len(graph[vertex]) == 0:
                graph.pop(vertex)
        self._edges = graph

    # Удалить из графа N вершин и проверить на древовидность
    def tree_Detector(self):
        if self._edges_value > 0:
            if self.undirected_cycle_Detector():
                print("Исходный граф не является деревом")
            else:
                print("Исходный граф уже является деревом, выполнение задания невозможно")
                return
            print("Введите количество удаляемых вершин")
            N = self._graph_Edges_Input_Controller()
            if N < self._edges_value:
                for index in range(N):
                    self.vertex_Remove()
                if self.undirected_cycle_Detector():
                    print("После удаления вершин граф так и не стал деревом")
                    print("")
                else:
                    print("Путем удаления вершин введенный граф стал деревом")
                    print("")
                    self.output_Graph()
                    self.nx_Undirected_Graph_Draw()
                    #print("Приведем граф к ориентированному виду для удобства восприятия")
                    #self.utod()
                    #self.output_Graph()
            else:
                print("Введено некорректное число удаляемых вершин")
                print("")
        else:
            print("Граф не был введен")

    # Метод поиска всех путей между двумя вершинами графа
    def find_All_Paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self._edges.keys():
            return []
        paths = []
        for node in self._edges[start]:
            if node not in path:
                newpaths = self.find_All_Paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    # Метод подсчета количества путей между всеми вершинами графа
    def all_Graph_Paths(self):
        vertexes = set()
        for vertex in self._edges.keys():
            vertexes.add(vertex)
            for value in self._edges[vertex]:
                vertexes.add(value)
        count = 0
        all_paths = []
        for vertex in vertexes:
            for jertex in vertexes:
                if jertex != vertex:
                    all_paths.append(self.find_All_Paths(vertex, jertex, []))
        for paths in all_paths:
            count += len(paths)
        print("Между всеми вершинами графа существует " + str(count) + " путей")
        print("")
        self.nx_Directed_Graph_Draw()

    # Метод отрисовки ориентированного графа с помощью библиотеки networkx и matplotlib
    def nx_Undirected_Graph_Draw(self):
        G = nx.Graph()
        for vertex in self._edges.keys():
            values = self._edges[vertex]
            for value in values:
                G.add_edge(vertex, value)
        nx.draw(G, with_labels = True)
        plt.show()

    # Метод отрисовки неориентированного графа с помощью библиотеки networkx и matplotlib
    def nx_Directed_Graph_Draw(self):
        G = nx.DiGraph()
        for vertex in self._edges.keys():
            values = self._edges[vertex]
            for value in values:
                G.add_edge(vertex, value)
        nx.draw(G, with_labels = True)
        plt.show()

    # Метод поиска цила Эйлера в графе
    def eulerian_Detector(self):
        """
        Для неориентированного графа
        if self._edges_value > 0:
            graph = copy.deepcopy(self._edges) # Буферный граф
            odd = [ vertex for vertex in graph.keys() if len(graph[vertex]) & 1 ]
            keys = []
            for key in graph.keys():
                keys.append(key)
            odd.append(keys[0])
            if len(odd) > 3:
                print("Граф не содержит Эйлерова цикла")
                print("")
                return
            stack = [ odd[0] ]
            path = []
            # Цикл обхода графа
            while stack:
                vertex = stack[-1]
                if graph[vertex]:
                    jertex = graph[vertex][0]
                    stack.append(jertex)
                    del graph[jertex][ graph[jertex].index(vertex) ]
                    del graph[vertex][0]
                else:
                    path.append(stack.pop())
            print("Эйлеров цикл в введенном графе: ")
            print (str(path))
            print("")
            return path      
        else:
            print("Граф пуст")
            print("")
        """
        # Для всех типов графов:
        if self._edges_value > 0:
            G = nx.DiGraph()
            for vertex in self._edges.keys():
                values = self._edges[vertex]
                for value in values:
                    G.add_edge(vertex, value)
            if nx.is_eulerian(G):
                print("Граф содержит Эйлеров цикл")
                print("Эйлеров цикл в введенном графе: ")
                print (str(list(nx.eulerian_circuit(G))))
                print("")
                return list(nx.eulerian_circuit(G))    
            else:
                print("Граф не содержит Эйлеров цикл")
                print("")
        else:
            print("Граф пуст")
            print("")
            