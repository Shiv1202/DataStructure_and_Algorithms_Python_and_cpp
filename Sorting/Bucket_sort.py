# Implemeting Bucket sort on an unsorted array.
"""**********************************************
This is mainly useful when input is uniformaly distributed 
over a range. Ex(0.0 to 1.0)
ALgorithm:
bucket_sort(arr, n)
1) Create n empty buckets(or lists).
2) Do Following for every array element arr[i].
....a) Insert arr[i] into bucket[n*array[i]].
3) Sort individual buckets using insertion sort.
4) Concatenate all sorted buckets.
*************************************************"""

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > up:
            bucket[j+1] = bucket[j]
            j -= 1
            bucket[j+1] = up
    return bucket

def bucket_sort(arr):
    A = []
    slot_num = 10 # 10 means 10 slots, each slot's size is 0.1.
    for i in range(slot_num):
        A.append([])
    # Put array element in different bucket.
    for i in arr:
        buc_index = int(slot_num * i)
        A[buc_index].append(i)
    # Sort individual buckets
    for i in range(slot_num):
        A[i] = insertion_sort(A[i])
    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(A[i])):
            arr[k] = A[i][j]
            k += 1
    return arr
# Main code.
def main():
    arr = [0.897, 0.565, 0.656, 0.12345, 0.665, 0.3535]
    print("Sorted Array is:")
    print(bucket_sort(arr))

if __name__ == "__main__":
    main()
    