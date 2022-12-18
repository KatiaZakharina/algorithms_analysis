from prettytable import PrettyTable


# 1 запрограммировать алгоритм Евклида
# 2 вывести таблицу "сложности" (кол-ва итераций) для пар чисел 1 - 100
# 3 попробовать оценить сложность алгоритма

def dict_to_list(dict):
    dictlist = []

    for key, value in dict.items():
        temp = [key, value]
        dictlist.append(temp)

    return dictlist


def gcd(a, b):
    # to count the number of function calls
    gcd.counter += 1

    if a == 0:
        return b

    return gcd(b % a, a)


def gcd_stats():
    gcd_dict = {}

    for i in range(1, 100):
        for j in range(i + 1, 100):
            gcd.counter = 0
            gcd(i, j)

            ij_str = f"{i}, {j}"
            gcd_dict[ij_str] = gcd.counter

    gcd_dict_list = dict_to_list(gcd_dict)

    table = PrettyTable()
    table.field_names = ['a, b', 'num of iterations']
    table.add_rows(gcd_dict_list)
    print(table)


gcd_stats()
