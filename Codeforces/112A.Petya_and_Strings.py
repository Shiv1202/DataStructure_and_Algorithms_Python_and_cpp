def check(s1, s2):
    n = len(s1)
    # flag = [0] * n
    for i in range(n):
        if s1[i].lower() > s2[i].lower():
            return 1
        elif s1[i].lower() < s2[i].lower():
            return -1
        else:
            continue
    return 0

def main():
    s1, s2 = input(), input()
    res = check(s1, s2)
    print(res)

if __name__ == "__main__":
    main()