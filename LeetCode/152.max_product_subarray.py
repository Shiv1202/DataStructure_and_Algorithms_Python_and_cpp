""" -------------> Questions <----------
Given an integer array nums, find the
contiguous subarray within an array
(containing at least one number) which
has the largest product.
**************** Example 1 **************
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest
product 6.
*************** Example 2 ***************
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2,
because [-2,-1] is not a subarray.
---------------> END <------------------"""
# Solution Class.
class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return -1
        curr_max = nums[0]
        curr_min = nums[0]
        final_product = nums[0]
        for i in range(1, len(nums)):
            temp = curr_max
            curr_max = max(max(curr_max * nums[i], curr_min * nums[i]), nums[i])
            curr_min = min(min(temp * nums[i], curr_min * nums[i]), nums[i])
            
            if curr_max > final_product:
                final_product = curr_max
        return final_product

# Main Code.
def main():
    arr = [2, 3, -2, 0, 4]
    s = Solution()
    result = s.maxProduct(arr)
    print(result)

# Driver Code.
if __name__ == "__main__":
    main()