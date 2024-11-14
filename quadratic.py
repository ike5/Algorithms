# O(N^2) - Quadratic

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
    nums = [2, 9, 3, 1, 0, 5, 4, 7, 6]
    nums_size = len(nums)

    selection_sort(nums, nums_size)
    print(nums)
