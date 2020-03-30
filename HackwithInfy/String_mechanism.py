# Function for check Mechanism
def check(i, n):
    for j in range(len(n)):
        if len(i) == len(n[j]):
            c = 0
            for x in range(len(i)):
                if i[x] != n[j][x]:
                    c += 1
            if c == 1:
                return True
    return False
# Main Code.
for _ in range(int(input())): # No. of Test Case.
    n, m = map(int, input().split())
    intital_arr = []
    for i in range(n):
        intital_arr.append(input())
    query_str = []
    for i in range(m):
        query_str.append(input())
    for i in query_str:
        if check(i, intital_arr):
            print("YES")
        else:
            print("NO")