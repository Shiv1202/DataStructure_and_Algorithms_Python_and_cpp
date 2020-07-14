def solution(y):
    y = int(y) + 1
    while len(set(str(y))) != 4:
        y = int(y) + 1
    return int(y)

def main():
    year = input()
    print(solution(year))

if __name__ == "__main__":
    main()