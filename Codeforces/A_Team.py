N = int(input())
ans = 0
for _ in range(N):
    x  = list(map(int, input().split()))
    if x.count(1) >= 2:
        ans += 1
print(ans)