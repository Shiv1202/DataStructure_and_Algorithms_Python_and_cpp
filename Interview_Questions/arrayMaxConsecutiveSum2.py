""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
NOTE : Question From FaceBook Interview.
Question : Given an array of integers,
find the maximum possible sum you can
get from one of its contiguous subarrays.
The subarray from which this sum comes
must contain at least 1 element.
************** Example ****************
inputArray = [-2, 2, 5, -11, 6], the
output should be
arrayMaxConsecutiveSum2(inputArray) = 7.
The contiguous subarray that gives the
maximum possible sum is [2, 5], with a
sum of 7.
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""

# Array Max Consecutive Sum Function.
def arrayMaxConsecutiveSum2(nums):
    if len(nums) == 0:
        return -1
    curr_max = nums[0]
    curr_min = nums[0]
    final_sum = nums[0]
    for i in range(1, len(nums)):
        temp = curr_max
        curr_max = max(max(curr_max + nums[i], curr_min + nums[i]), nums[i])
        curr_min = min(min(temp + nums[i], curr_min + nums[i]), nums[i])        
        if curr_max > final_sum:
            final_sum = curr_max
    return final_sum

# Main Function.
def main():
    n = [-2, 2, 5, -11, 6]
    res = arrayMaxConsecutiveSum2(n)
    print(res)

# Driver Code.
if __name__ == "__main__":
    main()