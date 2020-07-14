def solution(n, stones):
    i = 0
    count = 0
    for i in range(1, len(stones)):
        if stones[i] == stones[i - 1]:
            count += 1
    return count

def main():
    n, stones = int(input()), input()
    print(solution(n, stones))

if __name__ == "__main__":
    main()
