import math
import itertools
from prettytable import PrettyTable

KNUTH_CONST = (math.sqrt(5) + 1) / 2
MY_KNUTH_CONST = KNUTH_CONST


class Search:
    @staticmethod
    def binary_search(arr, low, high, x):

        # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return Search.binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
            else:
                return Search.binary_search(arr, mid + 1, high, x)

        else:
            # Element is not present in the array
            return -1

    @staticmethod
    def interpolation_search(arr, lo, hi, x):

        # Since array is sorted, an element present
        # in array must be in range defined by corner
        if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

            # Probing the position with keeping
            # uniform distribution in mind.
            pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                        (x - arr[lo]))

            # Condition of target found
            if arr[pos] == x:
                return pos

            # If x is larger, x is in right subarray
            if arr[pos] < x:
                return Search.interpolation_search(arr, pos + 1,
                                                   hi, x)

            # If x is smaller, x is in left subarray
            if arr[pos] > x:
                return Search.interpolation_search(arr, lo,
                                                   pos - 1, x)
        return -1

    # @staticmethod
    # def binary_search(key, is_own_const=False):
    #     multiply_const = MY_KNUTH_CONST if is_own_const else KNUTH_CONST
    #     return math.floor(self.table_size * (key * multiply_const - math.floor(key * multiply_const)))
