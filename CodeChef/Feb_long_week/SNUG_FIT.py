for _ in range(int(input())):
    N = int(input())
    total = 0
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    for j in range(N):
        if A[j] < B[j] :
            total += A[j]
        else:
            total += B[j]
    print(total)