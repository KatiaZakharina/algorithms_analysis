import math
import itertools
from prettytable import PrettyTable

KNUTH_CONST = (math.sqrt(5) + 1) / 2
MY_KNUTH_CONST = KNUTH_CONST


class Hashing:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)]
        self.current_size = 0

    def insert(self, key, is_own_const=False):
        index = self.multiplication_hash(key, is_own_const)

        # self.double_hashing(index, key)
        self.linear_probing(index, key)

    def multiplication_hash(self, key, is_own_const=False):
        multiply_const = MY_KNUTH_CONST if is_own_const else KNUTH_CONST
        return math.floor(self.table_size * (key * multiply_const - math.floor(key * multiply_const)))

    def double_hashing(self, index, key):
        if self.is_full():
            self.append(index, key)

            self.current_size += 1
            return

        second_index = self.hash_fn_2(key)

        if len(self.hash_table[index]) != 0:
            i = 1
            while True:
                new_index = (index + i * second_index) % self.table_size

                if len(self.hash_table[new_index]) == 0:
                    self.append(new_index, key)
                break
            i += 1
        else:
            self.append(index, key)

        self.current_size += 1

    def check_prime(self, n):
        if n == 1 or n == 0:
            return 0

        for i in range(2, n // 2):
            if n % i == 0:
                return 0
        return 1

    def get_prime(self, n):
        if n % 2 == 0:
            n = n + 1
        while not self.check_prime(n):
            n += 2
        return n

    def hash_fn_2(self, key):
        prime = self.get_prime(self.table_size)
        return key % prime

    def is_full(self):
        return self.current_size >= self.table_size

    def append(self, index, key):
        self.hash_table[index] += [key]

    def linear_probing(self, index, key):
        if self.is_full():
            self.append(index, key)
            self.current_size += 1
            return

        if len(self.hash_table[index]) != 0:
            for i in range(index + 1, index + self.table_size):
                if len(self.hash_table[i % self.table_size]) == 0:
                    self.append(i % self.table_size, key)
                    break
        else:
            self.append(index, key)

        self.current_size += 1

    def print(self):
        table = PrettyTable()

        for title, lst in zip([f"{i}" for i in range(self.table_size)],
                              itertools.zip_longest(*self.hash_table,
                                                    fillvalue="-")):
            table.add_column(title, lst)

        print(table)
