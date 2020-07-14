def solution(n, m, k):
    if m == 0 or m == n:
        return 0
    x = min(n // k, m)
    y = (m - x + k - 2) // (k - 1)
    return max(0, (x - y))

def main():
    for _ in range(int(input())):
        n, m, k = map(int, input().split())
        print(solution(n,m,k))
    
if __name__ == "__main__":
    main()