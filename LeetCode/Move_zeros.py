""" ------------> QUESTION <------------
Given an array nums, write a function to
move all 0's to the end of it while
maintaining the relative order of the 
non-zero elements.
**************************************
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
NOTE: You must do this in-place without
making a copy of the array.
---------------> END <-----------------"""

class Solution:
    def moveZeroes(self, nums):
        new_len = len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                new_len -= 1
        for i in range(new_len):
            if nums[i] == 0:
                for j in range(i + 1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
        return nums
def main():
    arr = [0, 1, 0, 3, 12]
    s = Solution()
    result = s.moveZeroes(arr)
    print(result)

if __name__ == "__main__":
    main()