class Solution:
    def repeat_missing(self, nums):
        repeating, missing = 0, 0
        n = len(nums)
        for i in range(n):
            item = abs(nums[i])
            if nums[item - 1] > 0:
                nums[item - 1] = -nums[item - 1]
            else:
                repeating = item
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
        return repeating, missing

if __name__ == "__main__":
    obj = Solution()
    arr = list(map(int, input().split()))
    print(obj.repeat_missing(arr))