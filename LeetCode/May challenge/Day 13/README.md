# Remove K Digits

Given a non-negative integer `num` represented as a string, remove `k` digits from the number so that the new number is the smallest possible.

**Note**
* The length of num is less than 10002 and will be ≥ k.
* The given num does not contain any leading zero.

**Example 1**

```
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
```

**Example 2**

```
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
```

**Example 3**

```
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
```

## Solution

Initilize an empty list to store the previous digits.
Iterate over given string and check `while` value of `k` is greater then `0` and `len(list) > 0` and last element of `list` is greater then the current digit of the string then `pop` the value for the `list`.

after break of `while` loop append the digit into list.

After full Iteration check if `K > 0`. Then `while k > 0` pop the value of list.

`return` the `"0"` if `len(list) == 0` else `return string from list`.

**Example**
``` 
num = "10200"
k = 1
stack = []
for first itreation digit = "1"
  but stack is empty.
  stack.append(digit) // ["1"]
for second iteration digit = "0"
  here all conditions are True.
  satck.pop() // []
  k = k - 1 // k = 0
  stack.append(digit) // ["0"]
for next every iteration k = 0 then While loop never run.
stack = ["0","2","0","0"]
res = "".join(stack)
res = "0200"
res = int(res)
res = 200
return str(res) // "200"
```
