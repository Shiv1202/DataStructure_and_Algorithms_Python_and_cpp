def solution(n, p, x):
    p.sort();
    min_day = 0; temp = []

    for i in range(n):
        if (p[i] < x / 2):
            min_day += 1
        else:
            temp.append(p[i])
    i = 0
    while i < len(temp):
        if x < temp[i]:
            x = 2 * x
            min_day += 1
        else:
            min_day += 1
            x = 2 * temp[i]; i += 1
    return min_day
def main():
    for _ in range(int(input())):
        n, x = map(int, input().split())
        popu = list(map(int, input().split()))
        print(solution(n, popu, x))

if __name__ == "__main__":
    main()