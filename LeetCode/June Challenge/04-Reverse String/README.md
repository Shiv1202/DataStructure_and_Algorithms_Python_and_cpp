# Reverse String

Write a function that reverses a string. The input string is given as an array of characters `char[]`.

Do not allocate extra space for another array, you must do this by **modifying the input array in-place** with `O(1) extra memory`.

You may assume all the characters consist of `printable ascii characters`.

**Example 1**

```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Example 2**

```
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Solution

**Two Pointers Approach** 
In this approach, two pointers are used to process two array elements at the same time.
We set one pointer in the beginning and one at the end and then to move them until they both meet.

* Set pointer left at index 0, and pointer right at index n - 1, where n is a number of elements in the array.

* While left < right:
  1. Swap s[left] and s[right].
  2. Move left pointer one step right, and right pointer one step left.

Or, using a `for loop` we can `increase and decrease` the `left and right pointer` respectively, till they iterate to `half the size of string`

swapping goes as: 

**Input**: a b c d e f

**a** b c d e **f**  
f **b** c d **e** a  
f e **c** **d** b a

**Output**: f e d c b a

