for _ in range(int(input())):
    s = input()
    ans = 0
    for char in s:
        if char.isdigit():
            ans += int(char)
    print(ans)

