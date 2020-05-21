# Kth Smallest Element in a BST

Given a binary search tree, write a function `kthSmallest` to find the **k**th smallest element in it.

**Note**
* You may assume `k` is always valid, `1 ≤ k ≤ BST's total elements`.

**Example 1**

```
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```

**Example 2**

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```

**Follow up:**
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

## Solution

**Depth First Search (DFS)**

In this strategy, we adopt the depth as the priority, so that one would start from a root and reach all the way down to certain leaf, and then back to root to reach another branch.

For this perticuler problem we going to use **DFS inorder traversal**

**To solve the problem, one could use the property of BST : inorder traversal of BST is an array sorted in the ascending order.**

### Approach:

**DFS inorder**
```
       5
      / \
     3   6
    / \
   2   4
  /
 1
 
 inorder output = [1, 2, 3, 4, 5, 6]
 ```
 * `Left` --> `Node` --> `Right`
 * `inorder(root.left) + [root.val] + inorder(root.right) if root else []`
