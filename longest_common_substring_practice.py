# Create a matrix
rows = 4
cols = 4

matrix = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = i - j

if __name__ == "__main__":
    print(matrix)
    for row in matrix:
        print(row)
