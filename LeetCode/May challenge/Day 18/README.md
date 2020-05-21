# Permutation in String

Given two strings **s1** and **s2**, write a function to return true if **s2** contains the permutation of **s1**. In other words, one of the first string's permutations is the substring of the second string.

**Example 1**

```
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2**

```
Input:s1= "ab" s2 = "eidboaoo"
Output: False
```

**Note:**

1. The input strings only contain lower case letters.
1. The length of both given strings is in range `[1, 10,000]`.

## Solution

**Algorithm**

Instead of generating the hashmap afresh for every window considered in `s2`, we can create the hashmap just once for the first window in `s2`. Then, later on when we slide the window, we know that we add one preceding character and add a new succeeding character to the new window considered. Thus, we can update the hashmap by just updating the indices associated with those two characters only. Again, for every updated hashmap, we compare all the elements of the hashmap for equality to get the required result.

