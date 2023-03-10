'''
Задание 3.1

Граф G задан списками смежностей вершин. Найти компоненты связности данного графа.
Определить, является ли граф эйлеровым; если это так - построить эйлеров цикл.
Определить, двудольный ли граф; если это так - найти разбиение на доли.

Задание 3.2

В городе есть N перекрестков и M дорог (каждая дорога начинается и заканчивается перекрестком, дороги имеют направление).
Известно время проезда каждой дороги (движение двустороннее, и время на движение в одну сторону может не совпадать со временем движения назад).
Определить перекресток для расположения на нем пожарной станции с условием:
пожарная машина должна попасть в наиболее удаленный от станции перекресток за минимальное время
(пожарная машина может нарушать ПДД и ехать по встречному направлению). Задачу реализовать двумя алгоритмами.

Задание 3.3

Есть N узлов, которые необходимо объединить в сеть.
Известна стоимость прокладки оптоволоконного кабеля между любой парой узлов.
Требуется спроектировать связную сеть (между любыми узлами которой можно передать сигнал) минимальной стоимости.
Задачу реализовать двумя алгоритмами.

Задание 3.4

Есть K сотрудников и K задач.
Для каждого сотрудника определены задачи, которые он умеет выполнять.
Назначить задачи сотрудникам так, чтобы каждый работал только над одной задачей, и все задачи были выполнены.
В случае невозможности такого назначения указать, какого сотрудника необходимо обучить какой задаче для возможности назначения.

Задание 3.5

В компании есть N сотрудников и M задач для исполнения.
У каждого сотрудника есть список задач, в работе над которыми он заинтересован и умеет выполнять (в порядке убывания интереса).
Для каждой задачи же известен список эффективности сотрудников, умеющих выполнять эту задачу (в порядке убывания эффективности).
Над каждой задачей может работать не более одного сотрудника, и каждый сотрудник может работать не более чем над одной задачей.

Провести 2 разных распределения максимального числа задач по сотрудникам в компании в соответствии с принципами:

(а) Сотрудник мог быть назначен выполнять задачу,
только если все более интересные для него задачи были назначены для выполнения другим,
более эффективным сотрудником.

(б) Задача назначена сотруднику,
только если все более эффективные для выполнения данной задачи сотрудники были назначены на более интересные для них задачи.
'''

from sys import maxsize as INF



def DFS_for_components(vertex: int, adjacents: list, visited: list, component: list, component_counter: list):
    component[vertex] = component_counter[0]
    visited[vertex] = True

    for adjacent in adjacents[vertex]:
        if not visited[adjacent]:
            DFS_for_components(adjacent, adjacents, visited, component, component_counter)


def components(graph: list) -> list:
    visited = [False] * len(graph)
    component = [-1] * len(graph)
    component_counter = [0]

    for vertex in enumerate(graph):
        if not visited[vertex[0]]:
            DFS_for_components(vertex[0], graph, visited, component, component_counter)
            component_counter[0] += 1

    for i in enumerate(component):
        component[i[0]] += 1

    return [component, component_counter[0]]



def graph_ribs(graph: list) -> list:
    ribs = []

    for vertex, adjacents in enumerate(graph):
        for adjacent in adjacents:
            if (vertex, adjacent) not in ribs and (adjacent, vertex) not in ribs:
                ribs.append((vertex, adjacent))

    return ribs


def vertex_degree(vertex: int, ribs: list) -> int:
    degree = 0

    for rib in ribs:
        if vertex is rib[0] or vertex is rib[1]:
            degree += 1

    return degree


def rib_and_index(vertex: int, ribs: list) -> list:
    rib = ()
    index = -1

    for i in range(len(ribs)):
        if vertex is ribs[i][0] or vertex is ribs[i][1]:
            rib, index = ribs[i], i
            break

    return rib, index


def is_eulerian(graph: list) -> bool:
    for adjacents in graph:
        if not len(adjacents) or len(adjacents) % 2:
            return False

    return True


def eulerian_path(graph: list) -> list:
    ribs = graph_ribs(graph)

    stack = [ribs[0][0]]
    path = []

    while len(stack) > 0:
        vertex = stack[len(stack) - 1]

        degree = vertex_degree(vertex, ribs)

        if degree == 0:
            stack.pop()
            path.append(vertex)
        else:
            rib, index = rib_and_index(vertex, ribs)
            ribs.pop(index)
            stack.append(rib[1] if vertex is rib[0] else rib[0])

    return path



def DFS_for_bipartite_graph(vertex: int, graph: list, colors: list, bipartition_flag: list):
    for adjacent in graph[vertex]:
        if not colors[adjacent]:
            colors[adjacent] = 3 - colors[vertex]
            DFS_for_bipartite_graph(adjacent, graph, colors, bipartition_flag)
        elif colors[adjacent] is colors[vertex]:
            bipartition_flag[0] = False


def is_bipartite(graph: list) -> bool:
    colors = [0] * len(graph)
    bipartition_flag = [True]

    for vertex, adjacents in enumerate(graph):
        if not colors[vertex]:
            colors[vertex] = 1
            DFS_for_bipartite_graph(vertex, graph, colors, bipartition_flag)

    return bipartition_flag[0]


def parties(graph: list) -> list:
    colors = [0] * len(graph)

    for vertex, adjacents in enumerate(graph):
        if not colors[vertex]:
            colors[vertex] = 1
            DFS_for_bipartite_graph(vertex, graph, colors, [])

    first_party = set()
    second_party = set()

    for vertex, color in enumerate(colors):
        first_party.add(vertex) if color == 1 else second_party.add(vertex)

    return first_party, second_party



def floyd_warshall(graph: list) -> list:
    distances = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k, x in enumerate(graph):
        for i, x in enumerate(graph):
            for j, x in enumerate(graph):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances



def prim(graph: list) -> list:
    key = [INF] * len(graph)
    parent = [None] * len(graph)
    visited = [False] * len(graph)

    key[0] = 0
    parent[0] = -1

    for cout, x in enumerate(graph):
        u = min_key(graph, key, visited)

        visited[u] = True

        for v, x in enumerate(graph):
            if graph[u][v] > 0 and visited[v] is False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    ribs = [((parent[i] + 1, i + 1), graph[i][parent[i]]) for i in range(1, len(graph))]

    return ribs


# USEFUL FUNCTIONS

def break_rules(graph: list) -> list:
    for i, x in enumerate(graph):
        for j, x in enumerate(graph):
            if i < j:
                graph[i][j] = graph[j][i] = min(graph[i][j], graph[j][i])

    return graph


def most_convenient_crossroads(graph: list) -> int:
    crossroads = []
    max_distances_list = []

    for crossroads, distances_list in enumerate(graph):
        max_distances_list.append((crossroads, max(distances_list)))

    min_distances_list = []
    min_distance = max_distances_list[0][1]

    for crossroads in max_distances_list:
        if crossroads[1] < min_distance:
            min_distance = crossroads[1]

    for crossroads in max_distances_list:
        if crossroads[1] == min_distance:
            min_distances_list.append((crossroads[0], graph[crossroads[0]]))

    return min_distance, min_distances_list


def min_key(graph: list, key: int, visited: set) -> int:
    min = INF

    for v, x in enumerate(graph):
        if key[v] < min and visited[v] is False:
            min = key[v]
            min_index = v

    return min_index


def distribute_work(graph: list) -> list:
    completed_tasks = [[i, None, False] for i, j in enumerate(graph)]
    uncompleted_tasks = []
    unbusy_employee = [i for i, j in enumerate(graph)]

    tasks_list = [(employee, tasks) for employee, tasks in enumerate(graph)]
    tasks_list.sort(key=lambda info: len(info[1]))

    for employee, tasks in tasks_list:
        for task in tasks:
            if not completed_tasks[task][-1]:
                completed_tasks[task][1] = employee
                completed_tasks[task][-1] = True
                unbusy_employee.remove(employee)
                break

    for task in completed_tasks:
        if not task[-1]:
            task[1] = unbusy_employee.pop()
            task[-1] = True
            uncompleted_tasks.append(task)
            completed_tasks.remove(task)

    completed_tasks.sort(key=lambda info: info[1])
    uncompleted_tasks.sort(key=lambda info: info[1])

    return completed_tasks, uncompleted_tasks


def distribute_hard_work(opportunities_graph: list, performance_graph: list) -> list:
    opportunities_list = [[employee, tasks, []] for employee, tasks in enumerate(opportunities_graph)]

    performance_list = [[task, employees, False] for task, employees in enumerate(performance_graph)]

    for task, employees, completed in performance_list:
        for employee in employees:
            employee_tasks = opportunities_list[employee][1]
            task_index = employee_tasks.index(task)
            more_intresting_tasks = employee_tasks[:task_index]

            count = len(more_intresting_tasks)

            for more_intresting_task in more_intresting_tasks:
                if performance_list[more_intresting_task][-1] and more_intresting_task not in \
                        opportunities_list[employee][-1]:
                    count -= 1

            if not count:
                performance_list[task][-1] = True
                opportunities_list[employee][-1].append(task)
                break

    opportunities_list.sort(key=lambda info: info[0])
    performance_list.sort(key=lambda info: info[0])

    return opportunities_list, performance_list


# TASK 3.1

def task_3_1():
    GRAPH = [
        [3],
        [4],
        [4],
        [0, 4],
        [1, 2, 3],
        [6, 8],
        [5, 8],
        [],
        [5, 6],
        []
    ]

    vertices, components_number = components(GRAPH)

    print(f'Количество компонент связности: {components_number}')
    for vertex, component in enumerate(vertices):
        print(f'{vertex}: {component}')

    EULERIAN_GRAPH = [
        [1, 4],
        [0, 5, 7, 6],
        [4, 5],
        [6, 7],
        [0, 8, 2, 5],
        [1, 4, 2, 9],
        [1, 3],
        [1, 3],
        [4, 9],
        [5, 8]
    ]

    if is_eulerian(EULERIAN_GRAPH):
        print(f'\nЭйлеров цикл: {eulerian_path(EULERIAN_GRAPH)}')
    else:
        print('\nГраф не является эйлеровым')

    BIPARTITE_GRAPH = [
        [5, 7],
        [2, 4, 6],
        [1, 5],
        [4],
        [1, 3],
        [0, 2],
        [1, 9],
        [0],
        [9],
        [6, 8]
    ]

    if is_bipartite(BIPARTITE_GRAPH):
        first_party, second_party = parties(BIPARTITE_GRAPH)
        print(f'\nДоли двудольного графа:\n{first_party}\n{second_party}')
    else:
        print('\nГраф не является двудольным')


# TASK 3.2

def task_3_2():
    GRAPH = [
        [0, INF, INF, INF, INF, 3, 7],
        [INF, 0, 3, 1, INF, INF, INF],
        [INF, 6, 0, INF, INF, INF, INF],
        [INF, INF, 4, 0, INF, INF, 3],
        [INF, INF, INF, 1, 0, 1, INF],
        [5, INF, INF, INF, INF, 0, INF],
        [6, 9, INF, 11, INF, INF, 0]
    ]

    min_distance, crossroads = most_convenient_crossroads(
        floyd_warshall(
            break_rules(GRAPH)))

    print(f'\nСамые удобные перекрестки с максимальным расстояние {min_distance}:')
    for crossroad in crossroads:
        print(f'{crossroad[0]}: {crossroad[1]}')


# TASK 3.3

def task_3_3():
    GRAPH = [
        [0, 1, 1, 2, 5],
        [1, 0, 3, 5, 3],
        [1, 3, 0, 4, 1],
        [2, 5, 4, 0, 2],
        [5, 3, 1, 2, 0]
    ]

    ribs = prim(GRAPH)

    print('\nУзлы, которые требуется соединить:')
    for rib in ribs:
        print(f'{rib[0][0]} - {rib[0][1]}: {rib[1]}')


# TASK 3.4

def task_3_4():
    EMPLOYEE_OPPORTUNITIES = [
        [0, 1],
        [2],
        [3],
        [0],
        [1, 2, 3]
    ]

    completed_tasks, uncompleted_tasks = distribute_work(EMPLOYEE_OPPORTUNITIES)

    print()

    for task in completed_tasks:
        print(f'Сотрудник {task[1]} -> Задание {task[0]}')

    for task in uncompleted_tasks:
        print(f'Обучить сотрудника {task[1]} -> Задание {task[0]}')


# TASK 3.5

def task_3_5():
    EMPLOYEE_OPPORTUNITIES = [
        [5, 1, 9, 6],
        [0, 1, 7, 2, 4],
        [8, 9, 5],
        [6, 2, 3, 5],
        [4, 0, 9, 7, 5]
    ]

    EMPLOYEE_PERFORMANCE = [
        [4, 1],
        [0, 1],
        [3, 1],
        [3],
        [1, 4],
        [0, 2, 4, 3],
        [3, 0],
        [4, 1],
        [2],
        [2, 4, 0]
    ]

    opportunities_list, performance_list = distribute_hard_work(EMPLOYEE_OPPORTUNITIES, EMPLOYEE_PERFORMANCE)

    print()

    for employee, tasks, completed_tasks in opportunities_list:
        if completed_tasks:
            print(f'Сотрудник {employee} получил задания: {completed_tasks}')
        else:
            print(f'Сотрудник {employee} не получил задания')

    for task, employees, completed in performance_list:
        if not completed:
            print(f'Задание {task} никто не получил')


if __name__ == '__main__':
    task_3_1()
    task_3_2()
    task_3_3()
    task_3_4()
    task_3_5()