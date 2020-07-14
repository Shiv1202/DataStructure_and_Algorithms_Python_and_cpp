for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    arr.sort()
    for i in arr:
        if count >= i:
            count += 1
    print(count)

