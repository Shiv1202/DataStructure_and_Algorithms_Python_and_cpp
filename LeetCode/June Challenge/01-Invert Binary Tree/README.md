# Invert Binary Tree

Invert a binary tree.

**Example 1**

#### INPUT
```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```

#### OUTPUT
```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

## Solution

**This is a classic tree problem that is best-suited for a recursive approach.**

The inverse of an empty tree is the empty tree. The inverse of a tree with root `R`, and subtrees `RL` and `RR`, is a tree with root `R`, whose right subtree is the inverse of `RL`, and whose left subtree is the inverse of `RR`.
We simply swap the `left` and `right` subtrees or `children` of each node in a recursive call.

