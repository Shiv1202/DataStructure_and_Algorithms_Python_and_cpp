def solution(x, y, a, b):
    m, cost = min(x, y), 0
    if 2 * a > b:
        cost = b * m
    else:
        cost = m * 2 * a
    return cost + ((x - m) * a + (y - m) * a)

def main():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        a, b = map(int, input().split())

        print(solution(x,y,a,b))


if __name__ == "__main__":
    main()