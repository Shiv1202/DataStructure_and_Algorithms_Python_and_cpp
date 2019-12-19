# Implement Selection Sort over an unsorted array.
"""************************************************
 The time complexity of above algorithm is O(n^2).
 Due to two nested loops.
************************************************"""

def selection_sort(arr):
    for i in range(len(arr)):

        min_idx = i
        for j in range(i + 1, len(arr)):
            if(arr[min_idx] > arr[j]):
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr
# Main Function 
def main():
    A = [64, 25, 12, 22, 15, 2, 18]
    result = selection_sort(A)
    for i in result:
        print(i, end = " ")

if __name__ == "__main__":
    main()