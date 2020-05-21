# Single Number

Given a **non-empty** array of integers, every element appears *twice* except for one. Find that single one.

**Note**
* Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example 1**
```
Input: [2,2,1]
Output: 1
```

**Example 2**
```
Input: [4,1,2,1,2]
Output: 4
```

## Solution

Let single element is `x`

In Question the frequency of all element are `2` except `x`.

So after converting nums array into `set` the element are unique.

```
sum(set(nums)) * 2 == sum(nums) - x

x = abs(sum(nums) - (sum(set(nums)) * 2))
```

**Example**

```
  nums = [3,3,7,7,10,11,11]
  sum(nums) = 52
  set(nums) = {3,7,10,11}
  sum(set(nums)) = 31
  sum(set(nums)) * 2 = 62
  sum(nums) - sum(set(nums)) * 2 = 10
```
