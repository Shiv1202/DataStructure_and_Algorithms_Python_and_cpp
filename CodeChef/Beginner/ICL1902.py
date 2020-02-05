from math import sqrt
for _ in range(int(input())):
    n = int(input())
    c, value = 0, 0
    while True:
        if n == 0:
            break
        else:
            value = int(sqrt(n))
            c += 1
            n = n - value ** 2
    print(c)
