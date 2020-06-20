# Longest Duplicate Substring

Given a string `S`, consider all duplicated substrings: (contiguous) substrings of `S` that occur 2 or more times.  (The occurrences may overlap.)

Return **any** duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is `""`.)

 **Example 1**
 
 ```
Input: "banana"
Output: "ana"
 ```
 
 **Example 2**
 
 ```
Input: "abcd"
Output: ""
 ```
 
 **Note**
* `2 <= S.length <= 10^5`
* `S` consists of lowercase English letters.
 
 
 **Hints given in Question**
 1. Binary search for the length of the answer. (If there's an answer of length 10, then there are answers of length 9, 8, 7, ...)
 1. To check whether an answer of length K exists, we can use Rabin-Karp 's algorithm.
 
 
 ## Solution
 
 **Explanation**
 
Binary search the length of longest duplicate substring and call the help function `test(L)`.
`test(L)` slide a window of length `L`,
rolling hash the string in this window,
record the seen string in a hashset,
and try to find duplicated string.

I give it a big mod for rolling hash and it should be enough for this problem.
Actually there could be hash collision.
One solution is to have two different mod for hash.
Or we can use a hashmap to record the index of string.

**Complexity**

Binary Search in range 1` and `N`, so it's `O(logN)`
Rolling hash `O(N)`
Overall `O(NlogN)`
Space `O(N)`
