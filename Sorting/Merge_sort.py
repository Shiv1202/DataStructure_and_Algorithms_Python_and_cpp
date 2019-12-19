# Implementing Merge Sort Algorithm on an unsorted array.
""" ************************************************************************
Merge Sort is based on Divide-and-conquer Algorithm.
The best, Avg, and Worst case time complexity in O(n log n)
**************************************************************************** """ 

def merge_sort(arr):
    print("\tSplitting: ", arr)
    print("-----------------------------------------------")
    if(len(arr) > 1):
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0
        while(i < len(left_arr) and j < len(right_arr)):
            if(left_arr[i] < right_arr[j]):
                arr[k] = left_arr[i]
                i = i + 1
            else:
                arr[k] = right_arr[j]
                j = j + 1
            k = k + 1

        while(i < len(left_arr)):
            arr[k] = left_arr[i]
            i = i + 1
            k = k + 1

        while(j < len(right_arr)):
            arr[k] = right_arr[j]
            j = j + 1 
            k = k + 1
    
    print("\tMerging: ", arr)
    print("---------------------------------------------")

def main():
    A = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    merge_sort(A)

if __name__ == "__main__":
    main()