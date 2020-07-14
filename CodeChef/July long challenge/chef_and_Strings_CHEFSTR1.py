for _ in range(int(input())):
    n = int(input())
    strings = list(map(int, input().split()))
    total_skip = 0
    for i in range(n - 1):
        total_skip += abs(strings[i] - strings[i + 1]) - 1
    print(total_skip)