# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = n
        def helper(start, end):
            if start == end:
                if isBadVersion(start):
                    self.ans = start
            if start < end:
                mid = (start + end) // 2
                if isBadVersion(mid):
                    self.ans = mid
                    helper(start, mid)
                else:
                    helper(mid+1, end)
            return self.ans
        return helper(1, n)
                    
