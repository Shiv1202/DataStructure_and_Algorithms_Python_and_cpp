# Implementation of Array Rotation in python 3.
"""********************************************
NOTE: ++++++++++ METHOD 2 +++++++++++++++++++++
(A Juggling Algorithm).
In this Instead of moving One by One, divide
the array in different sets where number of 
set is equal to GCD of n and d and move the 
elements within the set.
Basic Algo:
left_rotate(arr, d, n)
start
    for i = 0 to i < d
        Left rotate all element of array by 
        one.
end.
4) OUTPUT: [3,4,5,6,7,8,1,2]
================================================
Time Complexity : O(n)
Auxiliary Space : O(1)
***********************************************"""
""" Function to left rotate array of size
n by d."""
def left_rotate(arr, d, n):
    for i in range(gcd(d, n)):
        # Move i-th value of block.
        temp = arr[i]
        j = i
        while 1:
            k = j + d 
            if k >= n:
                k = k - n
            if k == 1:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

# function for array print.
def print_array(arr, size):
    for i in range(size):
        print(arr[i], end = " ")

# function to get gcd of d and n.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Main function.
def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    left_rotate(arr, d = 2, n = len(arr))
    print_array(arr, len(arr))

if __name__ == "__main__":
    main()