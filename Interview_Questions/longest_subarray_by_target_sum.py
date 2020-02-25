""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
Question : You have an unsorted array arr
of non-negative integers and a number s.
Find a longest contiguous subarray in arr
that has a sum equal to s. Return two
integers that represent its inclusive bounds.
If there are several possible answers,
return the one with the smallest left bound.
If there are no answers, return [-1].
Your answer should be 1-based, meaning
that the first position of the array
is 1 instead of 0.
************** Example ****************
s = 12 and arr = [1, 2, 3, 7, 5], the
output should be
findLongestSubarrayBySum(s, arr) = [2, 4].
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""

# Function fo Subarray.
def findLongestSubarrayBySum(s, arr):
    result = [-1]
    total = 0
    left, right = 0, 0
    while right < len(arr):
        total += arr[right]
        while left < right and total > s:
            total -= arr[left]
            left += 1
        if total == s and (len(result) == 1 or result[1] - result[0] < right - left):
            result = [left + 1, right + 1]
        right += 1
    return result

# Main Function.
def main():
    s = 12
    arr = [1, 2, 3, 7, 5]
    res = findLongestSubarrayBySum(s, arr)
    print(res)

# Driver Code.
if __name__ == "__main__":
    main()