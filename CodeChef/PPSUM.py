def sum_D(D, s):
    return 0

for i in range(int(input())):
    D, N = map(int, input().split())
    s = 0
    for i in range(N + 1):
        s += i
    print(s)
    ans = sum_D(D - 1, s)
        