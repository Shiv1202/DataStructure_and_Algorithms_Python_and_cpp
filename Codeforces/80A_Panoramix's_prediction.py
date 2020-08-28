def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def mid_prime(x, y):
    for num in range(x + 1, y):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                return True
    return False

x, y = map(int, input().split())
if not is_prime(y):
    print("NO")
else:
    if mid_prime(x, y):
        print("NO")
    else:
        print("YES")
