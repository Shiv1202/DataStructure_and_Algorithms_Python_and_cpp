def triangle(B):
    if B <= 3:
        return 0
    total = ((B // 2) - 1) + triangle(B - 2)
    return total

for i in range(int(input())):
    Base = int(input())
    print(triangle(Base))


# Method 2
for _ in range(int(input())):
    b = int(input())
    c = 0
    while b > 3:
        c += (b // 2 -1)
        b -= 2
    print(c)