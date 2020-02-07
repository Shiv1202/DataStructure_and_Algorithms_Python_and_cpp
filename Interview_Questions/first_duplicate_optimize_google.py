# Python Program For First Duplicate in a list.
"""*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Objective: We want to find first Duplicate 
no. in a given array.
Example : 
Given array = [2, 1, 3, 5, 3, 2]
Numbers are from 1 to len(array).
Output = 3 (3 is the first Duplicate).
Time Complexity : O(n).
*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""
# Function for First Duplicate.
def first_duplicate(arr, n):
    output_arr = []
    for i in range(n):
        index = abs(arr[i]) - 1
        if arr[index] < 0:
            output_arr.append(index + 1)
        arr[index] = -arr[index]
    return output_arr

# Main Function.
def main():
    l = [1,2,1,2,3,3]
    n = len(l)
    result = first_duplicate(l, n)
    if result:
        print(result[0])
    else:
        print(-1)

# Driver Code.
if __name__ == "__main__":
    main()