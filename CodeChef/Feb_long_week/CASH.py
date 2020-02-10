for _ in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = sum(A)
    print(ans % K)