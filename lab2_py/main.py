from numpy.random import randint

from hashing import Hashing
from search import Search

# 1) Реализовать алгоритмы бинарного и интерполяционного поиска числа x в массиве длины N,
# элементы которого - случайные целые числа в диапазоне от 0 до M.
# Вывести число операций сравнения, выполненных алгоритмом для заданных величин.


# 2) Реализовать алгоритмы построения, обхода и балансировки дерева бинарного поиска.
# На вход алгоритма подается последовательность целых положительных чисел.
# Программа должна строить BST, добавляя узлы в порядке последовательности.
# Реализовать обходы дерева по возрастанию и по убыванию узлов.
# Реализовать алгоритм нахождения k-го минимального ключа в дереве.
# На его основе сбалансировать построенное дерево
# (ротациями вправо и влево (n/2)-ый минимальный элемент помещается в корень и это повторяется рекурсией в дочерних узлах).

# 3) Реализовать хэширование умножением с разрешением коллизий цепочками переполнения,
# линейным зондированием и двойным хэшированием.
# Провести вычислительный эксперимент: подобрать константу для метода умножения,
# сравнить ее с константой Кнута по наибольшей длине цепочек коллизий
# (например, проитерировать константу Кнута, уменьшая или увеличивая с очень малым шагом)

MAX_VALUE = 100
VALUES_SIZE = 11
TABLE_SIZE = 7


def run_hashing(values, table_size):
    print('3) Hashing: ')

    hash_table = Hashing(table_size)

    for number in values:
        hash_table.insert(number, True)

    hash_table.print()


def run_search(values):
    values.sort()
    print('Sorted: ', values)

    element = values[randint(0, len(values) - 1)]
    print(f"1) Search:' {element}")

    binary_search_result = Search.binary_search(values, 0, len(values) - 1, element)
    print(f"binary_search_result: {binary_search_result}")

    interpolation_search_result = Search.interpolation_search(values, 0, len(values) - 1, element)
    print(f"interpolation_search_result: {interpolation_search_result}")


def generate_array(size, max_value):
    return randint(0, max_value, size)


def init():
    # VALUES_SIZE = int(input("Enter VALUES_SIZE: "))
    # MAX_VALUE = int(input("Enter MAX_VALUE: "))
    # TABLE_SIZE = int(input("Enter TABLE_SIZE: "))

    values = generate_array(VALUES_SIZE, MAX_VALUE)
    print('Values: ', values)

    run_search(values)
    run_hashing(values, TABLE_SIZE)


if __name__ == '__main__':
    init()
