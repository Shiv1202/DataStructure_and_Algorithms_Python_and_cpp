# Implementation of Radix sort on an unsorted array.
"""*************************************************
The idea of Radix sort is to do digit by digit sort
starting from least significant digit to most significant
digit. Radix sort uses counting sort as a subroutine to
sort.
****************************************************"""
# Counting sort function
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        ind = (arr[i] // exp)
        count[(ind) % 10] += 1

    # Position of this digit in output array.
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Build the output array.
    i = n - 1
    while  i >= 0:
        ind = (arr[i] // exp)
        output[count[ind % 10] - 1] = arr[i]
        count[ind % 10] -= 1
        i -= 1
    # Copying the output array in arr.
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

# Function for radix sort.
def radix_sort(arr):
    # find the maximum number of know number 
    # of Digit
    max1 = max(arr)
    # Do Counting sort for every digit
    # exp is 10^i where i is the current digit number.
    exp = 1
    while max1 / exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Main Function
def main():
    A = [170, 45, 40, 75, 90, 803, 24, 2, 666]
    radix_sort(A)
    for i in A:
        print(i, end = " ")

if __name__ == "__main__":
    main()