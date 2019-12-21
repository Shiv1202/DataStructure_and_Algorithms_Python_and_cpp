# Implementing Quick Sort algorithm on unsorted array.
"""**************************************************
Quick sort is based on Divide-and-conquer Algorithms.
The worst case time complexity is O(n^2).
The Best and Avg case time complexity is O(nlogn).
*****************************************************"""

def partition(arr, start, end):
    i = (start - 1)     # Index of smaller element
    pivot = arr[end]    # Pivot element(last element as pivot)
    for j in range(start, end):
        if(arr[j] < pivot):
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return (i + 1)

def quick_sort(arr, start, end):
    if(start < end):
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi - 1)
        quick_sort(arr, pi + 1, end)

def main():
    A = [10, 7, 17, 8, 9, 1, 5]
    quick_sort(A, 0, len(A) - 1)
    print("Sorted array: ")
    for i in range(len(A)):
        print(A[i], end = " ")

if __name__ == "__main__":
    main()
