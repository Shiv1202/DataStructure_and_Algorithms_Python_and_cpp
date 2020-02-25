""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
You have an array of Binary digits(0's and 1's).
Your task to sort that Binary array in 
Time Complexity : O(n).
    where n is size of array.
Space Complexity : O(1)

------------------> Example <---------------
For nums = [1,0,0,1,0,1,0,0,0,1,0]
the output should be
binary_sort(nums).
Output = [0,0,0,0,0,0,0,1,1,1,1]
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""

# Binary Sort Function.
def binary_sort(nums):
    no_0s = nums.count(0)
    no_1s = nums.count(1)
    output = [0] * no_0s
    output.extend(([1] * no_1s))
    return output

# Main Function.
def main():
    n = [1,0,0,1,0,1,0,0,0,1,0]
    res = binary_sort(n)
    print(res)

# Driver Code.
if __name__ == "__main__":
    main()