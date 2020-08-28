s1, s2 = input(), input()
ans = ""
for i in range(0, len(s1)):
    if s1[i] != s2[i]:
        ans += "1"
    else:
        ans += "0"
for i in ans:
    print(int(i), end = "")