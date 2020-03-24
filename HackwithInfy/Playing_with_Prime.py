# Function for check prime.
def is_prime(a):
    c = 0
    if a > 1:
        for i in range(2, a // 2):
            if a % i == 0:
                c += 1
        if c == 0:
            return True
    return False
# Driver Code.
for _ in range(int(input())):
    n = int(input())
    if n < 1 : print(-1)
    c = 0
    output = []
    for i in range(n + 1):
        for j in range(n + 1):
            x = list(map(int, str(i))) 
            y = list(map(int, str(j)))
            z = sum(x) + sum(y)
            if z > 1:
                if z != 2 and z % 2 == 0:
                    pass
                else:
                    if is_prime(z):
                        if (j, i) not in output:
                            c += 1
                            output.append((i, j))
                            output.append((j, i))
                            print((i, j))
    print(c)