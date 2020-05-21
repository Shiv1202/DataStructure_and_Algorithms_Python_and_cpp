class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        if n == 0:
            return -1
        till_max = curr_max = till_min = curr_min = A[0]
        for num in A[1:]:
            curr_max = max(num, curr_max + num)
            till_max = max(till_max, curr_max)
            curr_min = min(num, curr_min + num)
            till_min = min(till_min, curr_min)
        if till_min == sum(A):
            return till_max
        return max(till_max, sum(A) - till_min)
