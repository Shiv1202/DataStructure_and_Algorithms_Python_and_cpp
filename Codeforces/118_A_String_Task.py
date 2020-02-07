s = input().lower().strip()
s1 = "AEIOU"
x = s.split()
i = 0
for i in range(len(x)):
    if x[i] not in s1:
        x.insert(i - 1, ".")
    else:
        x.remove(x[i])
print(''.join(x))