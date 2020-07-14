for _ in range(int(input())):
    n = int(input())
    x, y = set(), set()
    for i in range(4 * n - 1):
        a, b = map(int, input().split())
        if a in x:
            x.remove(a)
        else:
            x.add(a)
        if b in y:
            y.remove(b)
        else:
            y.add(b)
    print(list(x)[0], list(y)[0])
