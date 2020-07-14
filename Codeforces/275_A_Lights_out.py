a11, a12, a13 = map(int, input().split())
a21, a22, a23 = map(int, input().split())
a31, a32, a33 = map(int, input().split())
l1, l2, l3 = "","",""
if (a11 + a12 + a21) % 2 == 0:
    l1 += "1"
else:
    l1 += "0"
if (a11 + a12 + a13 + a22) % 2 == 0:
    l1 += "1"
else:
    l1 += "0"
if (a12 + a13 + a23) % 2 == 0:
    l1 += "1"
else:
    l1 += "0"
if (a11 + a21 + a22 + a31) % 2 == 0:
    l2 += "1"
else:
    l2 += "0"
if (a12 + a21 + a22 + a23 + a32) % 2 == 0:
    l2 += "1"
else:
    l2 += "0"
if (a13 + a22 + a23 + a33) % 2 == 0:
    l2 += "1"
else:
    l2 += "0"
if (a21 + a31 + a32) % 2 == 0:
    l3 += "1"
else:
    l3 += "0"
if (a22 + a31 + a32 + a33) % 2 == 0:
    l3 += "1"
else:
    l3 += "0"
if (a23 + a32 + a33) % 2 == 0:
    l3 += "1"
else:
    l3 += "0"

print(l1)
print(l2)
print(l3)