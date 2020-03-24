from itertools import combinations
# Function for Finding Minimum Particle
def antimatter(a):
    global _min
    if len(a) > 1:
        for i in combinations(a, 2):
            temp = abs(i[0] - i[1])
            if _min > temp: _min = temp
            k = a.copy()
            k.remove(i[0])
            k.remove(i[1])
            k.append(temp)
            antimatter(k)
# Driver Code.
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    _min = min(arr)
    antimatter(arr)
    print(_min)
