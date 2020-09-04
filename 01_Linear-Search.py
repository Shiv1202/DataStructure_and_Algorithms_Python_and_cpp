# Program for Linear Serach of given element in an array.
"""************************************************
 The time complexity of above algorithm is O(n).
************************************************"""
def linear_search(arr, x):
    for ele in arr:
        if ele == x:
            return True
             
    return False
# Main Function
def main():
    arr = [2, 3, 4, 10, 40, 45, 76]
    x = 45
    result = linear_search(arr, x)
    if(result == -1):
        print("Element is not present in array.")
    else:
        print("Element is present at position: " + str(result))

# calling main function
if __name__ == "__main__":
    main()