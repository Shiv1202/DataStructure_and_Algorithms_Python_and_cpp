# Implement Trie (Prefix Tree)

Implement a trie with `insert`, `search`, and `startsWith` methods.

**Example**

```
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
```

**Note**
* You may assume that all inputs are consist of lowercase letters a-z.
* All inputs are guaranteed to be non-empty strings.

## Solution

**What is Tries?**

A Trie is a special **data structure** used to store strings that can be visualized like a graph. It consists of nodes and edges. Each node consists of at max 26 children and edges connect each parent node to its children. ... Actually, **Tries** are generally used on groups of strings, rather than a single string.

```
            root
          /   |   \
          t   a    b
          |   |    |
          h   n    y
          |   | \  | \
          e   s  y t  e
        / |   |    |
       i  r   w    e
      |   |   |
      r   e   e
              |
              r
```

```

TrieNode
{
  map<character, TrieNode> children;
  boolean isEndofword;
}
```
So, every trie node has 2 main components:
1. **a `map`** - where key is the character, and value is the TrieNode.
This is used to establish a parent-child relationship between the subsequent nodes.
Initially the map is empty or you can assign NULL value to the key-value pairs.

2. **a `boolean`**- that represents that the character represnting this trie node is a end of word or not.
Initially the bollean value is set to false for every new trie node.

##### Main idea- If two words have same prefix, they share common ancestors.

The complexity of creating this datastructure is `O(l*n)`, where `'l'` is the average length of the words,
and `'n'` is the total no. of words stored in the trie datastructure.

complexity for searching(prefix based and whole word search) is `O(l)`
complexity for deletion of any word `O(l*n)`
