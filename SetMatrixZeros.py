def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])

    rows = [False] * m
    cols = [False] * n

    # First pass: mark rows and columns that contain 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True

    # Second pass: set elements to 0
    for i in range(m):
        for j in range(n):
            if rows[i] or cols[j]:
                matrix[i][j] = 0

    return matrix


# ---------------- Test Case ----------------
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print("Original Matrix:")
for row in matrix:
    print(row)

result = setZeroes(matrix)

print("\nMatrix After Setting Zeroes:")
for row in result:
    print(row)