""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
Given an array arr[0.. n - 1] of distinct ele.
and a range [low, high], find all no that are 
in range but not in array. The missing ele
should be printed in sorted order.
--------------> Example <-----------------
Input: arr = [10, 12, 11, 15]
    low = 10, high = 15
Output: 13, 14
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* """

# Missing Element Function.
def missing_ele(arr, n, l, h):
    s = set(arr)
    for i in range(l, h + 1):
        if i not in s:
            print(i, end = " ")
# Main Function.
def main():
    arr = [1, 3, 5, 4]
    n = len(arr)
    low, high = 1, 10
    missing_ele(arr, n, low, high)
# Driver Code.
if __name__ == "__main__":
    main()