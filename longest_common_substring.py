def max_value_in_matrix(matrix: [[]]) -> (int, int):
    return 3, 3


def longest_common_substring(str1: str, str2: str) -> str:
    rows = len(str1)
    cols = len(str2)
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    #    print(matrix)

    for row in range(len(str1)):
        for col in range(len(str2)):
            if str1[row] == str2[col]:
                up_left = 0
                if row > 0 & col > 0:
                    up_left = matrix[row - 1][col - 1]
                matrix[row][col] = 1 + up_left
            else:
                matrix[row][col] = 0
    substring_length, row_index = max_value_in_matrix(matrix)
    start_index = row_index - substring_length + 1
    return str1[start_index: start_index + substring_length]


if __name__ == '__main__':
    print(longest_common_substring("Look", "zyBooks"))
