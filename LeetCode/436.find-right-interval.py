#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#

# @lc code=start
class Solution:
    def binary_search(self, arr, ele):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid][1][0] < ele:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if not intervals:
            return []
        if len(intervals) == 1:
            return [-1]
        n = len(intervals)
        result = [-1] * n
        verify_list = list(sorted([(idx, val) for idx, val in enumerate(intervals)], key=lambda x: x[1][0]))

        print(verify_list)
        for i, interval in enumerate(intervals):
            val = interval[1]
            position = self.binary_search(verify_list, val)

            if position == n:
                continue
            else:
                result[i] = verify_list[position][0]
        return result
# @lc code=end

