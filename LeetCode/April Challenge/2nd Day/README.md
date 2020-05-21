# Happy Number

Write an algorithm to determine if a number `n` is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1. Those numbers for which this process **ends in 1** are happy numbers.

Return True if n is a happy number, and False if not.

**Example**

```
Input: 19
Output: true
Explanation: 
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 02 = 1
```

## Solution
* We have to check if after performing given operation if we get `1` then we have to return `True` else we have to return `Fasle`.
* If we get any number again after performing the given operation the loop never end.

Initialize a set pr a hash table for sotring the values which we get after performing operation.
Loop untill `n != "1"` and add that number into set/hash table
Now find the sum of square and assign to n.
If n is in set/hash table `return False` else `return True`
