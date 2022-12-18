import math

MERGE_INSERTION_MAX_QUANTITY = 13


def merge_insertion_sort(array):
    if len(array) < MERGE_INSERTION_MAX_QUANTITY:
        return insertion_sort(array)

    average_index = math.floor(len(array) / 2)
    left = merge_insertion_sort(array[0:average_index])
    right = merge_insertion_sort(array[average_index:])

    return merge(left, right)


def merge(left, right):
    sorted_array = []
    print(sorted_array)

    while len(left) and len(right):
        if left[0] < right[0]:
            sorted_array += [left[0]]
            left = left[1:]
            continue

        sorted_array += [right[0]]
        right = right[1:]

    print(sorted_array, left, right)

    return sorted_array + left + right


QUICK_INSERTION_MAX_QUANTITY = 16


def quick_insertion_sort(array):
    if len(array) < QUICK_INSERTION_MAX_QUANTITY:
        return insertion_sort(array)

    pivot = array[0]
    left = []
    right = []

    for i in range(len(array)):
        if pivot > array[i]:
            left += array[i]
        else:
            right += array[i]

    return quick_insertion_sort(left) + pivot + quick_insertion_sort(right)


# n * (7 + {1, n} * 8) =>  O(n^2)

def insertion_sort(array):
    for i in range(len(array)):
        current_value = array[i]
        j = i
        while j > 0 and array[j - 1] > current_value:
            array[j] = array[j - 1]
            j -= 1
            array[j] = current_value

    return array
