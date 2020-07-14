# Program for Recursive Binary Serach of given element in an array.
""" *****************************************************
 The time complexity of Binary Search algorithm is O(log n).
******************************************************** """
def binary_search(arr, first, last, ele):
    # Base case for recursion
    if(last >= first):
        mid = first + (last - 1) // 2

        if(arr[mid] == ele):
            return mid + 1
        if(arr[mid] > ele):
            return binary_search(arr, first, mid - 1, ele)
        else:
            return binary_search(arr, mid + 1, last, ele)
    else:
        return -1
# Main Function
def main():
    arr = [2, 4, 7, 8, 11, 15, 16, 25]
    x = 
    result = binary_search(arr, 0, len(arr) - 1, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at position: " + str(result))

if __name__ == "__main__":
    main()