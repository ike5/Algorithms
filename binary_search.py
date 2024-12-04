# O(log N) - logarithmic
import random_list_module


def binary_search(nums, N, key):
    mid = 0
    low = 0
    high = N - 1
    while high >= low:
        mid = (high + low) / 2
        if nums[mid] < key:
            low = mid + 1
        elif nums[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    nums = random_list_module.generate_random_list()
    N = len(nums)
    key = 3000

    return_value = binary_search(nums, N, key)
