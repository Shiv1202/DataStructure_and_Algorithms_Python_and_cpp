k, n = map(int, input().split())
lucky_str = []
for _ in range(k):
    lucky_str.append(input())
for _ in range(n):
    x = input()
    bool = []
    for i in lucky_str:
        if i in x:
            bool.append(1)
        else:
            bool.append(0)
    if len(x) >= 47 or any(bool):
        print("Good")
    else:
        print("Bad")