for _ in range(int(input())):
    k = int(input())
    output = [["." for j in range(8)] for i in range(8)]
    output[0][0] = "O"
    k -= 1
    for i in range(8):
        for j in range(8):
            if i == 0 and j == 0:
                continue
            if k > 0:
                output[i][j] = "."
                k -= 1
            else:
                output[i][j] = "X"
    for i in range(8):
        for j in range(8):
            print(output[i][j], end = "")
        print()