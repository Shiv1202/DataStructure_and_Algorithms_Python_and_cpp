matrix = []
for i in range(5):
    matrix.append(input().split(" "))
for j in range(len(matrix)):
    if "1" in matrix[j]:
        row, col = j, matrix[j].index("1")
print(abs(row - 2) + abs(col - 2))