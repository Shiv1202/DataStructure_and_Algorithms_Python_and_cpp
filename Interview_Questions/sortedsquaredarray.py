# Python Program to print Sorted Square Array.
""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
NOTE : Question From FaceBook Interview.
Question : Given an Integer array of size n.
1 <= n <= 10000 and 
-10000<= eleOfArray <= 10000
we have to return Output array square of element
in sorted order with time Complexity O(n).
Example : 
Input : [-6, -4, -3, 1, 2, 5]
Output : [1, 4, 9, 16, 25, 36]
Time Complexity = O(n)
Space Complexity = O(n)
NOTE:
As we Know sort() method is having time
complexity O(nlogn).
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""
# Function for sorted square array.
def sorted_square_arr(arr, n):
    output = [0] * n
    i, j, x = 0, n - 1, n - 1
    while i <= j:
        if abs(arr[i]) > arr[j]:
            output[x] = arr[i] ** 2
            i += 1
            x -= 1
        else:
            output[x] = arr[j] ** 2
            j -= 1
            x -= 1
    return output

# Main Function.
def main():
    l = [-6, -4, -3, 1, 2, 5]
    n = len(l)
    print(sorted_square_arr(l, n))

# Driver Code.
if __name__ == "__main__":
    main()