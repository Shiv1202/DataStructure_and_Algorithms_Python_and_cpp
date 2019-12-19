# Implement Bubble Sort over an unsorted array.
"""************************************************
 The worst case time complexity of above algorithm is O(n*n).
 The Best case time complexity is O(n)
 Due to two nested loops.
************************************************"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if(swap == False):
            break
    return arr

def main():
    A = [64, 38, 25, 12, 77, 22, 11]
    result = bubble_sort(A)
    for i in result:
        print(i, end = " ")

if __name__ == "__main__":
    main()