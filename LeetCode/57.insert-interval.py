#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        if new_start > new_end:
            new_start, new_end = new_end, new_start
        ans, i = [], 0
        while i < len(intervals) and new_start > intervals[i][1]:
            ans.append(intervals[i])
            i += 1
        while i < len(intervals) and new_end >= intervals[i][0]:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        ans.append([new_start, new_end])
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
            
        return ans
# @lc code=end

