# Function for finding sum of crossing mid point.
def croosing_mid_sum(arr, l, m, h):
    curr_sum = 0
    left_sum = -100000
    for i in range(m, l - 1, -1):
        curr_sum += arr[i]
        if curr_sum > left_sum:
            left_sum = curr_sum
    curr_sum = 0
    right_sum = -100000
    for i in range(m + 1, h, 1):
        curr_sum += arr[i]
        if curr_sum > right_sum:
            right_sum = curr_sum
    return left_sum + right_sum

# Function for find sum of two half and also return max.
def max_subarray_sum(arr, l, h):
    if l == h:
        return arr[1]
    mid = (l + h) // 2
    return max(max(max_subarray_sum(arr, l, mid),
                    max_subarray_sum(arr, mid + 1, h)),
                    croosing_mid_sum(arr, l, mid, h))
# Main Function.
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    n = len(nums)

    print(max_subarray_sum(nums, 0, n - 1))
# Driver Code.
if __name__ == "__main__":
    main()