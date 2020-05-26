# Interval List Intersections

Given two lists of **closed** intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval `[a, b]` (with `a <= b`) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

**Example 1**

```
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

**Example 2**

```
Input: A = [[1,4],[8,12],[15,20]], B=[[3,9],[11,13]]
Output: [[3,4],[8,9],[11,12]]
```

**Constraints**
* `0 <= A.length < 1000`
* `0 <= B.length < 1000`
* `0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9`

## Solution

**Points to remember**
* intervals are both inclusive
* intervls are pairwise disjoint, ie., in no case s1==s2 && e1==e2 simultaneously
* intervals are sorted in ascending order
```
s1-------------e1 
       |        |
       |        |
       s2------------e2
```
**Conditions for an intersecting interval**
* `(e1 >= s2)`
* `(e2 >= s1)`  
both of the above conditions must follow for an intersecting interval.

**How to find an intersecting interval?**  
`output : [ max(s1,s2) , min(e1,e2) ]`

**Special case**
```
1----------8          12-----------16
           |
           |
           8-------10
           
output: [[8,8]]
in this case, (s2>=s1) && (s2<=e1) will follow
``` 
Now, for iterating the `A list` and `B list` we take two pointers, say `aptr` and `bptr` respectively. Now if `e1 < e2` we increase the `aptr` else increase the `bptr`. 
