# Possible Bipartition

Given a set of `N` people (numbered 1, 2, ..., N), we would like to split everyone into `two groups of any size.`

Each person may dislike some other people, and they should not go into the same group. 

Formally, if `dislikes[i] = [a, b]`, it means it is not allowed to put the people numbered a and b into the same group.

Return `true` if and only if it is possible to split everyone into two groups in this way.

**Example 1**

```
Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
```

**Example 2**

```
Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
```

**Example 3**

```
Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
```

**Constraints**
* `1 <= N <= 2000`
* `0 <= dislikes.length <= 10000`
* `1 <= dislikes[i][j] <= N`
* `dislikes[i][0] < dislikes[i][1]`
* `There does not exist i != j for which dislikes[i] == dislikes[j]`

## Solution

The question asks us to divide given people into two groups such that no two people in the same group dislike each other.

For ease of understanding, we can represent this problem as a **graph**, with people being the **vertices** and dislike-pairs being the **edges** of this graph.

We have to find out if the vertices can be divided into two sets such that there aren't any edges between vertices of the same set. A graph satisfying this condition is called a **bipartite graph**.

We try to color the two sets of vertices, with **RED** and **BLUE** colors. In a bipartite graph, a RED vertex must be connected only with BLUE vertices and a BLUE vertex must be connected only with RED vertices. In other words, there must NOT be any edge connecting two vertices of the same color. Such an edge will be a **conflict edge**.

**The presence of conflict edges indicate that bipartition is NOT possible**.

The graph may consist of many connected components. For each connected component, we run our **BFS algorithm** to find conflict edges, if any. For each component, we start by coloring one vertex RED, and all it's neighbours BLUE. Then we visit the BLUE vertices and color all their neighbours as RED, and so on. During this process, if we come across any **RED-RED** edge or **BLUE-BLUE** edge, we have found a **conflict edge** and we immediately return **false**, as bipartition will not be possible.

If no conflict edges are found at the end of the algorithm, it means bipartition is possible, hence we return **true**.
