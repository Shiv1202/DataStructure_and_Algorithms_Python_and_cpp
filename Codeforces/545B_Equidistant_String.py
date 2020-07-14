s = input()
t = input()
p = [""] * len(s)
# print(p)
diff = []
if len(s) != len(t):
    print("impossible")
else:
    for i in range(len(s)):
        if s[i] == t[i]:
            p[i] += s[i]
        else:
            diff.append(i)
    if len(diff) & 1:
        print("impossible")
    else:
        for i in range(len(diff)):
            if i >= len(diff) / 2:
                p[diff[i]] += t[diff[i]]
            else:
                p[diff[i]] += s[diff[i]]
        print("".join(p))