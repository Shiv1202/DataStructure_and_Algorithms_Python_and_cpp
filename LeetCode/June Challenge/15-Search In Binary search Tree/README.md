# Search in a Binary Search Tree

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example,
**Example**

```
Input:
Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2

Output:
      2     
     / \   
    1   3

```
In the example above, if we want to search the value `5`, since there is no node with value `5`, we should return `NULL`.

Note that an empty tree is represented by `NULL`, therefore you would see the expected output (serialized tree format) as `[]`, not null.

## Solution
**Basic Property of Binary Tree**
1. The left subtree of a node contains only nodes with keys lesser then the value of that node.
1. The right subtree of a node contains only nodes with keys greater then the value of that node.
1. The left and right subtree each must also be a binary search tree.
There must be no duplicate nodes.

**Searching a Key in Binary Search Tree**

Search operation in Binary Search Tree is very similar to **Binary Search in Arrya**.  Searching an element in the binary search tree is basically this traversal in which at each step we will go either towards left or right and hence in at each step we discard one of the sub-trees.

**Time Complexity:**

The worst case time complexity of search operation is O(h) where h is height of Binary Search Tree. In worst case, we may have to travel from root to the deepest leaf node.
