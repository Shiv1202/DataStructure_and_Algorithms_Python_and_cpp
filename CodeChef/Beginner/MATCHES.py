for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = a + b
    match = [6,2,5,5,4,5,6,3,7,6]
    total = 0
    for i in str(ans):
        total += match[int(i)]
    print(total)