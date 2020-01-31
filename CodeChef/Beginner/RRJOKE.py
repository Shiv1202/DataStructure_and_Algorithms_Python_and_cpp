from itertools import permutations

for _ in range(int(input())):
    N = int(input())
    perm = permutations([i] for i in range(1, N + 1))
    for i in perm:
        print(i)