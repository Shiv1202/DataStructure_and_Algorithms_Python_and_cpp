for _ in range(int(input())):
    N = int(input())
    x = list(map(int, input().split()))
    y = x
    i = 0
    ans = ""
    while i + 1 != N - 1 and x[i + 1] - x[i] == 1 :
        i += 1
        x.remove(i)
    ans = ans.join(f"{y[0]}...{y[i]}")
    print(ans, x)