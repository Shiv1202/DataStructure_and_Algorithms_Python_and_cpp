# Implementing Counting sort on an unsorted array.
"""***********************************************
This sorting technique based on keys between a specific range.
**************************************************"""
def counting_sort(arr, range):
    
    m = range + 1
    count = [0] * m                
    for a in arr:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            arr[i] = a
            i += 1
    return arr

def main():
    A = [1, 5, 4, 8, 7, 6, 9, 2, 1, 5, 4]
    range = 9
    print(counting_sort(A, range))

if __name__ == "__main__":
    main()



