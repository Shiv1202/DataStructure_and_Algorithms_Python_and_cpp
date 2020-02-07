n, k = map(int, input().split())
scores = list(map(int, input().split()))
c = 0
for i in range(n):
    if scores[k - 1] == 0:
        c = scores.index(0)
    else:
        if k == n or scores[k] < scores[k - 1]:
            c = k
        if k < len(scores) and scores[i] > 0 and scores[i] >= scores[k - 1]:
            c += 1
        else:
            break
print(c)