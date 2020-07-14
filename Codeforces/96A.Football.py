def solution(s):
    if len(s) <= 7:
        return "NO"
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
            if count == 7:
                return "YES"
        else:
            count = 1
    return "NO"

def main():
    s = input()
    print(solution(s))

if __name__ == "__main__":
    main()