for i in range(int(input())):
    D, N = map(int, input().split())
    s = 0
    if D == 1:
        s += (N * (N + 1)) // 2
    else:
        while D >= 1:
            s = 0
            s += (N * (N + 1)) // 2
            N = s
            D -= 1
    print(s)
        