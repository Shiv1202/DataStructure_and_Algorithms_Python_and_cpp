def solution(s):
    target = "hello"
    j, pas = 0, 0
    for i in range(len(s)):
        if s[i] == target[j]:
            j += 1
            pas += 1

            if pas == 5:
                break
    if pas == 5:
        return "YES"
    return "NO"

def main():
    s = input()
    print(solution(s))

if __name__ == "__main__":
    main()


