# Python Program For First Duplicate in a list.
"""*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Objective: We want to find first Duplicate 
no. in a given array.
Example : 
Given array = [2, 1, 3, 5, 3, 2]
Output = 4 (At 4th index we found first
            Duplicate.)
Time Complexity : O(n^2).
Space Complexity : O(1)
*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""
# Function For Finding Duplicate.
def first_duplicate(l, n):
    duplicate_index = n
    for i in range(n):
        for j in range(i + 1, n):
            if l[j] == l[i]:
                duplicate_index = min(duplicate_index, j)

    if duplicate_index == n:
        return -1
    return duplicate_index

def main():
    l = [2,1,3,5,3,2]
    n = len(l)
    print(first_duplicate(l, n))

# Driver Code.
if __name__ == "__main__":
    main()