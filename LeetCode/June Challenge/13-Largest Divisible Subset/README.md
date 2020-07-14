# Largest Divisible Subset

Given a set of **distinct** positive integers, find the largest subset such that every pair `(Si, Sj)` of elements in this subset satisfies:

`Si % Sj = 0 or Sj % Si = 0.`

If there are multiple solutions, return any subset is fine.

**Example 1**

```
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
```

**Example 2**

```
Input: [1,2,4,8]
Output: [1,2,4,8]
```

## Solution

As we know For two numbers, `A` and `B`, if `A < B`, then `A % B` must > 0(A != 0). The only chance `A % B == 0` must be `A >= B`.
With this idea, we sort the given list. Then the question turns similar to no. **300 - longest increasing subsequence**.

For `ith` number, its largest divisible subset is the max of subset of any `j` from `0` - `i-1` in which `nums[i] % nums[j] == 0`.
