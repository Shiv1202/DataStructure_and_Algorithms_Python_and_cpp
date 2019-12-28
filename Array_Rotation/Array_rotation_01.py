# Implementation of Array Rotation in python 3.
"""********************************************
NOTE: ++++++++++ METHOD 1 +++++++++++++++++++++
(Using temp array).
Basic Algo:
arr = [1,2,3,4,5,6,7,8], d = 2, n = 8
1) Store d element in a temp array.
    temp = [1, 2]
2) Shift rest of the arr[].
    arr = [3,4,5,6,7,8]
3) Store back the d element at the end of array.
    arr = [3,4,5,6,7,8,1,2]
4) OUTPUT: [3,4,5,6,7,8,1,2]
================================================
Time Complexity : O(n)
Auxiliary Space : O(d)
***********************************************"""
""" Function for left rotation of arr[]
of size n by d. """
def left_rotate(arr, d, n):
    for i in range(d):
        left_rotate_one(arr, n)

""" function to left rotate arr[] of
size n by 1. """
def left_rotate_one(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i+1]
    arr[n -1] = temp

# function for print array.
def print_array(arr, size):
    for i in range(size):
        print(arr[i], end = " ")

# main function (Driver code).
def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    left_rotate(arr, d = 2, n = len(arr))
    print_array(arr, len(arr))

if __name__ == "__main__":
    main()
