# Not sure, but I think this program finds/uses the smallest index
# This program is meant to teach nested loops

# Nested Loops Runtime

def main(n: int, nums: []) -> None:
    for i in range(n):
        index_smallest = i
        for j in range(i + 1, n):
            if nums[i] < nums[index_smallest]:
                index_smallest = j
        temp = nums[i]
        nums[i] = nums[index_smallest]
        nums[index_smallest] = temp


if __name__ == '__main__':
    numbers: [] = [5, 2, 9, 7, 1, 6]
    main(len(numbers), numbers)
