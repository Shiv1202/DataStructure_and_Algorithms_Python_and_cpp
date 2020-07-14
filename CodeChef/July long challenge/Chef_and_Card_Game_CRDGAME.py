for _ in range(int(input())):
    n = int(input())
    chef = morty = 0
    for i in range(n):
        a, b = map(str, input().split())
        sum_a = sum_b = 0
        for i in a:
            sum_a += int(i)
        for i in b:
            sum_b += int(i)
        if sum_a > sum_b:
            chef += 1
        elif sum_a < sum_b:
            morty += 1
        else:
            chef += 1
            morty += 1
    if chef > morty:
        print(0, chef)
    elif morty > chef:
        print(1, morty)
    else:
        print(2, chef)