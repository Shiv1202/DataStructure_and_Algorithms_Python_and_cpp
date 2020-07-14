class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        mid_res = 0
        max_len = 0
        temp = {0 : -1}
        for i, num in enumerate(nums):
            if num == 0:
                count += 1
            else:
                count -= 1
            if count in temp:
                mid_res = i - temp[count]
            else:
                temp[count] = i
            max_len = max(mid_res, max_len)
        return max_len
