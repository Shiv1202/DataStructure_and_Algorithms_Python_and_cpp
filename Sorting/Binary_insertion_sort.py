# Implement Binary Insertion Sort over an unsorted array.
"""************************************************
In normal insertion sort, it takes O(n) comparisons(at nth iteration)
in worst case. We can reduce it to O(log n)
by using Binary Search.
************************************************"""

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    
    if start > end:
        return start
    
    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr

def main():
    A = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    result = insertion_sort(A)
    for i in result:
        print(i, end = " ")

if __name__ == "__main__":
    main()