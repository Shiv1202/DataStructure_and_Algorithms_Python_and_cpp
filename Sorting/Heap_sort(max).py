# Implementing Heap Sort on an unsorted array (Max Heap).
"""*****************************************************
Heap sort is based on Binary Heap Data Structure.
Binary Heap build of Complete binary Tree.
********************************************************"""

def heapify(arr, n, i):
    largest = i # Intializi largest as root node.

    left = 2 * i + 1    # Left node
    right = 2 * i + 2   # Right node

    # Now Check if left child exists and is greater then root.
    if left < n and arr[i] < arr[left]:
        largest = left
    # Now Check if right child exists and is greater then root.
    if right < n and arr[largest] < arr[right]:
        largest = right
    # Now Changing the root if needed.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap
        # Heapify the root.
        heapify(arr, n, largest)

# Main Heap Sort function.
def heap_sort(arr):
    n = len(arr)
    # Build a max heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    # Extract element one by one.
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Main Function.
def main():
    arr = [12, 11, 45, 2, 13, 7, 56, 14]
    heap_sort(arr)
    print("Sorted array is: ")
    for i in range(len(arr)):
        print(arr[i], end = " ")

if __name__ == "__main__":
    main()


