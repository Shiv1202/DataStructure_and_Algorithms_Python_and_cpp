# Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

**Example 1**

```
Input: "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

**Example 2**

```
Input: "cccaaa"
Output: "cccaaa"
Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
```

**Example 3**

```
Input: "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

### Approach:

* **Step 1:** we `create a frequency map` of the characters in the given string.
* **Step 2:** we now need to `sort` this datastructure in `decreasing order by frequency value`. 
we may achieve so using a maxheap, priority queue or simply reverse sort any type of container.
* **Step 3:** now with this `reverse sorted structure`, we need to create our `resultant string ` by using its values.
