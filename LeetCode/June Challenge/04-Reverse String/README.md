# Reverse String

Write a function that reverses a string. The input string is given as an array of characters `char[]`.

Do not allocate extra space for another array, you must do this by **modifying the input array in-place with O(1)** extra memory.

You may assume all the characters consist of printable ascii characters.

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

Life is short, use Python.
```
def reverseString(self, s):
  s.reverse()
```

Speaking seriously, let's use this problem to discuss two things:
* Does *in-place* mean constant space complexity?
* Two pointers approach.

**Approach 1**
**--> Recursion In-place, O(N) Space**
Here is an example. Let's implement recursive function `helper` which receives two pointers, left and right, as arguments.

* Base case: if `left >= right`, do nothing.

* Otherwise, swap `s[left]` and `s[right]` and call `helper(left + 1, right - 1)`.

To solve the problem, call helper function passing the head and tail indexes as arguments: `return helper(0, len(s) - 1)`.

Source code file given above.

**Approach 2**
**--> Two Pointers, Iteration, O(1) Space**
In this approach, two pointers are used to process two array elements at the same time. Usual implementation is to set one pointer in the beginning and one at the end and then to move them until they both meet.

*Algorithm*
* Set pointer left at index `0`, and pointer right at index `n - 1`, where n is a number of elements in the array.
* When left < right:
    Swap `s[left]` and `s[right]`.
    Move left pointer one step right, and right pointer one step left.
    
    
**Example**
```
     | H | e | l | l | o |
       ^               ^                  step1 : swap
      left            right
  ----------------------------------------------------------------
  
     | o | e | l | l | H |
           ^       ^                      step2: swap
          left     right
  ----------------------------------------------------------------
  
     | o | l | l | e | H |
               ^                          job is Done
           left = right
      
```

**Complexity Analysis**
* Time complexity : O(N) to swap N/2 element.
* Space complexity : O(1), it's a constant space solution.

