# Maximum Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Follow up:**

If you have figured out the `O(n)` solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Solutions

### Approach 1
**By Using Divide and Conquer approach we can find the answer in `O(nlogn)` time.

**Steps**
  1. Divide the given array in two halves
  1. Return the maximum of following three
  
    i) Maximum subarray sum in left half (Make a recursive call)
    ii) Maximum subarray sum in right half (Make a recursive call)
    iii) Maximum subarray sum such that the subarray crosses the midpoint
    
  For Source Code visit: https://github.com/Shiv1202/DataStructure_and_Algorithms_Python_and_cpp/blob/master/LeetCode/max_subarray_by_divide_and_conquer.py
 
**Time Complexity:**
maxSubArraySum() is a recursive method and time complexity can be expressed as following recurrence relation.
T(n) = 2T(n/2) + Θ(n)
The above recurrence is similar to Merge Sort and can be solved either using Recurrence Tree method or Master method. It falls in case II of Master Method and solution of the recurrence is Θ(nLogn).


### Approach 2
**By Using The Kadane’s Algorithm we can find the answer in `O(n)` time.

Algorithm:

  ```
  Initialize:
    max_so_far = 0
    max_ending_here = 0

  Loop for each element of the array
    (a) max_ending_here = max_ending_here + a[i]
    (b) if(max_ending_here < 0)
            max_ending_here = 0
    (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  return max_so_far
  ```
Example:
  ```
  Lets take the example:
    {-2, -3, 4, -1, -2, 1, 5, -3}

    max_so_far = max_ending_here = 0

    for i=0,  a[0] =  -2
    max_ending_here = max_ending_here + (-2)
    Set max_ending_here = 0 because max_ending_here < 0

    for i=1,  a[1] =  -3
    max_ending_here = max_ending_here + (-3)
    Set max_ending_here = 0 because max_ending_here < 0

    for i=2,  a[2] =  4
    max_ending_here = max_ending_here + (4)
    max_ending_here = 4
    max_so_far is updated to 4 because max_ending_here greater 
    than max_so_far which was 0 till now

    for i=3,  a[3] =  -1
    max_ending_here = max_ending_here + (-1)
    max_ending_here = 3

    for i=4,  a[4] =  -2
    max_ending_here = max_ending_here + (-2)
    max_ending_here = 1

    for i=5,  a[5] =  1
    max_ending_here = max_ending_here + (1)
    max_ending_here = 2

    for i=6,  a[6] =  5
    max_ending_here = max_ending_here + (5)
    max_ending_here = 7
    max_so_far is updated to 7 because max_ending_here is 
    greater than max_so_far

    for i=7,  a[7] =  -3
    max_ending_here = max_ending_here + (-3)
    max_ending_here = 4
  ```
