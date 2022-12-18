# 1: Реализовать гибридный алгоритм, сочетающий Quick и Insertion Sort
# 2: Реализовать гибридный алгоритм, сочетающий Merge и Insertion Sort
# 3: Подсчитать число элементарных операций в реализации сортировки вставками

from numpy.random import randint
import numpy as np

from sorts import merge_insertion_sort, quick_insertion_sort


def init():
    quantity = int(input("Enter quantity of arrays: "))
    size = int(input("Enter size of array: "))
    max_value = int(input("Enter max value: "))

    arrays = generate_arrays(quantity, size, max_value)

    print('Initial array:')
    print(arrays)

    # run_first_task(arrays)
    run_second_task(arrays)


def generate_array(size, max_value):
    return randint(0, max_value, size)


def generate_arrays(quantity, size, max_value):
    arrays_list = list(map(lambda p: generate_array(size, max_value), np.empty(quantity)))

    return np.asarray(arrays_list)


def run_first_task(arrays):
    sorted_array_list = list(map(lambda array: quick_insertion_sort(array), arrays))

    print("Sorted array: (quick + insertion):")
    print(np.asarray(sorted_array_list))


def run_second_task(arrays):
    sorted_array_list = list(map(lambda array: merge_insertion_sort(array), arrays))

    print("Sorted array: (merge + insertion):")
    print(np.asarray(sorted_array_list))


if __name__ == '__main__':
    init()
