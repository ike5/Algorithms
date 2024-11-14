# O(N) - Linear

def linear_search(nums, numsSize, key):
    for i in range(numsSize):
        if nums[i] == key:
            return i
    return -1


if __name__ == '__main__':
    nums = [3, 6, 2, 7, 9, 0, 1]
    numsSize = len(nums)
    key = int(input("Enter a number to search: "))

    result = linear_search(nums, numsSize, key)
    if result == -1:
        print("Element not found")
    else:
        print("Element found at index", result)
