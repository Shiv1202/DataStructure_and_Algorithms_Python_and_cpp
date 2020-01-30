for _ in range(int(input())):
    s1 = input()
    s2 = input()
    min_diff, max_diff = 0, 0
    for i in range(len(s1)):
        if s1[i] != s2[i] and s1[i] != "?" and s2[i] != "?":
            min_diff += 1
            max_diff += 1
        elif s1[i] == s2[i] and s2[i] == "?":
            max_diff += 1
        elif s1[i] != s2[i] and (s1[i] == "?" or s2[i] == "?"):
            max_diff += 1
    print(min_diff, max_diff)
