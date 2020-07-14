for _ in range(int(input())):
    minimum = 0

    for _ in range(int(input())):
        s, p, v = map(int, input().split())
        i = p // (s + 1)

        if i * v > minimum:
            minimum = i * v
    print(minimum)