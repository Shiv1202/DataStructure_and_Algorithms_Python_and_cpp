# Function for min_rotation.
def min_rotation(arr):
    if not arr:
        return -1
    n = len(arr[0])
    cnt = {(arr[0][i:] + arr[0][:i]) : i for i in range(n)}
    for s in arr[1:]:
        if len(s) != n: return -1
        for i in range(n):
            cur = s[i:] + s[:i]
            if cur not in cnt: return -1
            cnt[cur] += i
    return cnt[min(cnt, key = lambda x: cnt[x])]

# Driver Code.
for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    print(min_rotation(arr))

"""
Example : 
    n = 4
    arr = ['11234', '23411', '41123', '11234']
Explanation : 
    finally all the strings would be 11234.
    first and last string input needs no rotations
    Second needs 3 rotations.
    third needs 1 rotations.
    total Min_Rotation = 4.
"""