s1, s2 = input(), input()
i = j = count = 0
if len(s1) != len(s2):
    print("NO")
else:
    a = b = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
            a[j] = s1[i]
            b[j] = s2[i]
            j += 1

            if count > 2:
                print("NO")
if a[1] == b[0] and a[0] == b[1]:
    print("YES")
else:
    print("NO") 