for _ in range(int(input())):
    n, k = map(int, input().split())
    price = list(map(int, input().split()))
    print(sum([i - k for i in price if i > k]))