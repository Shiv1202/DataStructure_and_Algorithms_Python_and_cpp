# Maximum Sum Circular Subarray

Given a **circular array C** of integers represented by `A`, find the maximum possible sum of a non-empty subarray of **C**.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, `C[i] = A[i]` when `0 <= i < A.length`, and `C[i+A.length] = C[i]` when `i >= 0`.)

Also, a subarray may only include each element of the fixed buffer `A` at most once.  (Formally, for a subarray `C[i]`, `C[i+1], ..., C[j]`, there does not exist `i <= k1`, `k2 <= j` with `k1 % A.length = k2 % A.length`.)

**Examples**

```
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
```
```
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
```
```
Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
```
```
Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
```
```
Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
```

**Note**

1. `-30000 <= A[i] <= 30000`
1. `<= A.length <= 30000`


## Solution
For those of you who are familiar with the **Kadane's algorithm**, think in terms of that.

**Overview of Kadane's algorithm**
For a given array `A`, Kadane's algorithm can be used to find the maximum sum of the subarrays of `A`. Here, we only consider non-empty subarrays.

Kadane's algorithm is based on dynamic programming. Let `dp[j]` be the maximum sum of a subarray that ends in `A[j]`. That is,

`dp[j]= max(A[i] + A[i + 1] + .... A[j])`

Then, a subarray ending in `j+1 (such as A[i], A[i+1] + ... + A[j+1]) maximizes the A[i] + ... + A[j]` part of the sum by being equal to `dp[j]` if it is non-empty, and `0` if it is. Thus, we have the recurrence:

`dp[j + 1] = A[j + 1] + max(dp[j], 0)`
Since a subarray must end somewhere, `max(dp[j])` must be the desired answer.

To compute `dp` efficiently, Kadane's algorithm is usually written in the form that reduces space complexity. We maintain two variables: ans as `max(dp[j])` and cur as `dp[j]` and update them as `j` iterates from `0` to `A.length - 1`.

Then, Kadane's algorithm is given by the following psuedocode:

    
    #Kadane's algorithm
    ans = cur = None
    for x in A:
      cur = x + max(cur, 0)
      ans = max(ans, cur)
    return ans
    
    
**My Solution**

This Solution is also based on Kadane's algorithm but shightly modified.
We are going to maintain 4 different variable
1. `curr_max` = Current maximum of array at index `i`.
1. `till_max` = Maximum value till that index of array.
1. `curr_min` = Current Minimum of array at index `i`.
1. `till_min` = Minimum value till that index of array.

Here `till_min` is the total minimum of array at the end and `till_max` is total maximum at the end of array.
2 Cases are possible 
  1. ` if till_min == sum(A)` then return `till_max` as ans.
  
  1. else return maximum of `(till_max, sum(A) - till_min)`.
  
Let's see an Example:
```
A = [8, -8, 9, -9, 10, -11, 12]
n = len(A)
curr_max = curr_min = till_max = till_min = A[0] = 8
loop through array from i = 1 to i = n - 1
For i = 1:
  curr_max = max(A[i], curr_max + A[i]) // max(-8, 8 + (-8)) = 0
  till_max = max(till_max, curr_max) // max(8, 0) = 8
  curr_min = min(A[i], curr_min + A[i]) // min(-8, 8 + (-8)) = -8
  till_min = min(till_min, curr_min) // min(8, -8) = -8

For i = 2:
  curr_max = max(A[i], curr_max + A[i]) // max(9, 0 + 9) = 9
  till_max = max(till_max, curr_max) // max(8, 9) = 9
  curr_min = min(A[i], curr_min + A[i]) // min(9, -8 + 9) = 1
  till_min = min(till_min, curr_min) // min(-8, 1) = -8
  
For i = 3:
  curr_max = max(A[i], curr_max + A[i]) // max(-9, 9 + (-9)) = 0
  till_max = max(till_max, curr_max) // max(9, 0) = 9
  curr_min = min(A[i], curr_min + A[i]) // min(-9, 1 + (-9)) = -9
  till_min = min(till_min, curr_min) // min(-8, -9) = -9
  
For i = 4:
  curr_max = max(A[i], curr_max + A[i]) // max(10, 0 + 10) = 10
  till_max = max(till_max, curr_max) // max(9, 10) = 10
  curr_min = min(A[i], curr_min + A[i]) // min(10, -9 + 10) = 1
  till_min = min(till_min, curr_min) // min(-9, 1) = -9
  
For i = 5:
  curr_max = max(A[i], curr_max + A[i]) // max(-11, 10 + (-11)) = -1
  till_max = max(till_max, curr_max) // max(10, -1) = 10
  curr_min = min(A[i], curr_min + A[i]) // min(-11, 1 + (-11)) = -11
  till_min = min(till_min, curr_min) // min(-9, -11) = -11
  
For i = 6:
  curr_max = max(A[i], curr_max + A[i]) // max(12, -1 + 12) = 12
  till_max = max(till_max, curr_max) // max(10, 12) = 12
  curr_min = min(A[i], curr_min + A[i]) // min(12, -11 + 12) = 1
  till_min = min(till_min, curr_min) // min(-11, 1) = -11
  
Finally Here,
sum(A) = 11
till_min != sum(A)
then we return,
max(till_max, sum(A) - till_min) // max(12, 11 - (-11)) = 22
```
