# Valid Perfect Square

Given a positive integer `num`, write a function which returns `True` if `num` is a perfect square else `False`.

**Note: Do Not** use any built-in library function such as `sqrt`.

**Example 1**

```
Input: 16
Output: true
```

**Example 2**

```
Input: 14
Output: false
```

## Solution

```
Initilize i = 1
If num is perfect square of i then num is perfectly devisible by i and num / i == i.
Check these condition while i * i <= num
If Condition is True then return True
Else return False.
