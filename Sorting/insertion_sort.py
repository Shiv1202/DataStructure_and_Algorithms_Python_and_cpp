# Implement Insertion Sort over an unsorted array.
"""************************************************
 The worst case time complexity of above algorithm is O(n^2).
 Due to two nested loops.
************************************************"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while (j >= 0 and key < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = key
    return arr

def main():
    A = [68, 45, 12, 10, 42, 5, 6]
    result = insertion_sort(A)
    for i in result:
        print(i, end = " ")

if __name__ == "__main__":
    main()