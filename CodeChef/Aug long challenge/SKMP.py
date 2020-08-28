from copy import deepcopy
def solution(s, p):
    # n, m = len(s), len(p)
    for char in p:
        s.remove(char)
    s.sort()
    # print(s)
    temp = deepcopy(s)
    temp.append(p[0])
    temp = sorted(temp, reverse = True)
    # print(temp)
    if p[0] not in s:
        s_left = s[0:len(temp) - temp.index(p[0]) - 1]
        s_right = s[len(temp) - temp.index(p[0]) - 1:]
        return "".join(s_left) + "".join(p) + "".join(s_right)
    else:
        s_left = s[0 : s.index(p[0])]
        s_right = s[s.index(p[0]) : ]
        x = "".join(s_left) + "".join(p) + "".join(s_right)
        return min(x, "".join(s[0:len(temp) - temp.index(p[0]) - 1]) + "".join(p) + "".join(s[len(temp) - temp.index(p[0]) - 1 :]))

for _ in range(int(input())):
    string = list(input())
    patt = list(input())

    print(solution(string, patt))
