# Count Square Submatrices with All Ones

**Example 1**

```
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
```

**Example 2**

```
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
```

**Constraints**
* `1 <= arr.length <= 300`
* `1 <= arr[0].length <= 300`
* `0 <= arr[i][j] <= 1`

## Solution
let's take an example
```
0 1 1 1
1 1 1 1
0 1 1 1
```
we know that every **1** in the matrix, makes a `1x1` matrix of itself. So, our task is to find out `2x2` and other bigger sub square matrices in the given matrix.
For this, let's traverse our matrix from (1,1) index (essentially leaving out the 0th row, and 0th column).  

0 1 1 1  
1 **1** 1 1  
0 1 1 1  

we now check the, `left, upper and diagonal element of this 1` and check whether it forms a square matrix  
to ensure this, we `replace the current value at index (1,1) by the min(left, top, diagonal)+1`
The matrix becomes:  

0 1 1 1  
1 **1** 1 1  
0 1 1 1  

where 0 is the min of the three values and 0+1=1
now for next value 

0 1 1 1  
1 1 **1** 1  
0 1 1 1  

here minimum of three values is 1 and 1+1=2. so matrix becomes

0 1 1 1  
1 1 **2** 1  
0 1 1 1 

**Note** the value `2` represents the completion of a `2x2` matrix. Now for subsequent values

0 1 1 1 &nbsp;&nbsp;&nbsp;&nbsp;0 1 1 1  
1 1 2 **1**--->1 1 2 **2**  
0 1 1 1 &nbsp;&nbsp;&nbsp;&nbsp;0 1 1 1    


0 1 1 1 &nbsp;&nbsp;&nbsp;&nbsp;0 1 1 1  
1 1 2 2--->1 1 2 2  
0 **1** 1 1 &nbsp;&nbsp;&nbsp;&nbsp;0 **1** 1 1   


0 1 1 1 &nbsp;&nbsp;&nbsp;&nbsp;0 1 1 1  
1 1 2 2--->1 1 2 2  
0 1 **1** 1 &nbsp;&nbsp;&nbsp;&nbsp;0 1 **2** 1  


0 1 1 1 &nbsp;&nbsp;&nbsp;&nbsp;0 1 1 1  
1 1 2 2--->1 1 2 2  
0 1 2 **1** &nbsp;&nbsp;&nbsp;&nbsp;0 1 2 **3**  


so final manipuated matrix is  
```
0 1 1 1  
1 1 2 2  
0 1 2 3
```
Now, the result or `count` of the total number of square sub matrices present is `the sum of all the values in this manipulated matrix` because each value represents the completion of a square matrix.
