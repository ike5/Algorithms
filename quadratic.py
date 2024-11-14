# O(N^2) - Quadratic
import random_list_module


def selection_sort(nums, nums_size):
    for i in range(nums_size):
        index_smallest = i
        for j in range(i + 1, nums_size):
            if nums[j] < nums[index_smallest]:
                index_smallest = j
        temp = nums[i]
        nums[i] = nums[index_smallest]
        nums[index_smallest] = temp


if __name__ == '__main__':
    nums = random_list_module.generate_random_list()
    nums_size = len(nums)

    selection_sort(nums, nums_size)
    print(nums)
