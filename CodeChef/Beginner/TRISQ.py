def triangle(B):
    if B <= 3:
        return 0
    total = ((B // 2) - 1) + triangle(B - 2)
    return total

for i in range(int(input())):
    B = int(input())
    print(triangle(B))