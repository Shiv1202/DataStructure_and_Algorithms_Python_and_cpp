""" -----------> Question <----------------
The Problem is to count all the possible
paths from top left to botton right of a m*n
matrix with Constraints that 
NOTE:
From each cell you can either move only
to right or down.

*-*-*-*-*-*-*-*-*- Example *-*-*-*-*-*-*-
Input: m = 2, n = 3     Output: 3

Explanation: There are 3 Paths
(0 ,0)-->(0, 1)-->(0, 2)-->(1, 2)
(0 ,0)-->(0, 1)-->(1, 1)-->(1, 2)
(0 ,0)-->(1, 0)-->(1, 1)-->(1, 2)
----------------> END <-------------------"""
"""
    Basic Method.
    Time Complexity : exponential 
"""
def number_of_path(m, n):
    """
        If either m = 1 or n = 1
    """
    if m == 1 or n == 1:
        return 1
    return number_of_path(m-1,n)+number_of_path(m,n-1)

"""
    Solution with DP.
    Time Complexity: O(mn)
    Space Complexity: O(mn)
"""
def number_of_path_dp(m, n):
    count = [[0 for x in range(n)] for y in range(m)]
    print(count)
    # Count for path to reach any cell
    # in first column and row is 1
    for i in range(m):
        count[i][0] = 1
    for j in range(n):
        count[0][j] = 1
    for i in range(1, m):
        for j in range(n):
            count[i][j] = count[i-1][j] + count[i][j-1]
    return count[m-1][n-1]

"""
    Space Optimization of DP Problem.
    Space Complexity : O(n)
"""
def number_of_path_dp_optimise(m, n):
    # Create 1d array to store the result
    # of the subprogram.
    mid_res = [1 for i in range(n)]
    for i in range(m - 1):
        for j in range(1, n):
            mid_res[j] += mid_res[j - 1]
    return mid_res[n - 1]

# Main Function.
def main():
    m = 2
    n = 3
    print(number_of_path_dp_optimise(m, n))

# Driver Code.
if __name__ == "__main__":
    main()
