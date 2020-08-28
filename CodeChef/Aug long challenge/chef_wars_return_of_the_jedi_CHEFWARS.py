def solution(h, p):
    while h > 0 and p > 0:
        h = h - p
        p = p // 2
    if h <= 0:
        return 1
    elif p <= 0:
        return 0


for _ in range(int(input())):
    h, p = map(int, input().split())

    print(solution(h, p))

