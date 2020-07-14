n = int(input())
x, y, z = [], [], []
for i in range(n):
    a, b, c = map(int, input().split())
    x.append(a); y.append(b); z.append(c)
# print(x, y, z)
if sum(x) == 0 and sum(y) == 0 and sum(z) == 0:
    print("YES")
else:
    print("NO")