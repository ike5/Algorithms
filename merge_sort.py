# O(N log N) - linearithmic
# not finished and needs to be worked on to work properly

import random_list_module


def merge_sort(nums, i, k):
    j = 0
    if i < k:
        j = (i + k) / 2  # midpoint
        merge_sort(nums, i, j)  # sort left part
        merge_sort(nums, j + 1, k)  # sort right part
        merge(nums, i, j, k)  # merge parts


def merge(nums, i, j, k):
    return nums + i + j + k


if __name__ == '__main__':
    nums = random_list_module.generate_random_list()
    print(nums)
