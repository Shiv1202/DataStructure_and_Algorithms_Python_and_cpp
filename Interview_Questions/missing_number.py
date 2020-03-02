""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
Question : You are supposed to label a
bunch of boxes with numbers from 0 to n,
and all the labels are stored in the
array arr. Unfortunately one of the
labels is missing. Your task is to
find it.
************** Example ****************
For arr = [3, 1, 0], the output should be
missingNumber(arr) = 2
******** Guaranteed constraints ********
        1 ≤ arr.length ≤ 1000,
        0 ≤ arr[i] ≤ arr.length.
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""

# Missing Number Function.
def missing_no(arr):
    l = len(arr)
    s = (l*(l+1)) // 2
    return s - sum(arr)

# Main Function.
def main():
    arr = [3, 1, 0]
    res = missing_no(arr)
    print(res)

# Driver Code.
if __name__ == "__main__":
    main()