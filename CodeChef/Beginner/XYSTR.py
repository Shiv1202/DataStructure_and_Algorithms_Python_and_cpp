for _ in range(int(input())):
    s = input()
    ans = 0
    i = 0
    while i < len(s) - 1:
        if (s[i]=="x" and s[i+1]=='y') or (s[i]=='y' and s[i+1]=='x'):
            ans += 1
            i += 1
        i += 1
    print(ans)    