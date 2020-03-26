# Driver Code.
for _ in range(int(input())):
    n = int(input()) # No. of piles
    arr = list(map(int, input().split())) # No. of stone in each piles.
    k = int(input()) # integer k.
    c = 0
    while any(arr) > 0: # While each element != 0
        if max(arr) > k:
            x = arr.index(max(arr))
            arr[x] = max(arr) - k
            c += 1
        else:
            x = arr.index(max(arr))
            arr[x] = 0
            c += 1
    if c % 2 == 0:
        print(f"Alex wins the game of {n} pile(s)")
    else:
        print(f"Sam wins the game of {n} pile(s)")