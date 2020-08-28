def solution(k, n, pos):
    min_moves = float('inf')
    ans = 0
    for i in range(n):
        if pos[i] <= k:
            if k % pos[i] == 0:
                m = k / pos[i]
                if m < min_moves:
                    min_moves = m
                    ans = pos[i]

    if min_moves == float('inf'):
        return -1
    return ans
     
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(solution(k, n, arr))