class Solution:
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            item =abs(nums[i])
            if nums[item - 1] > 0:
                nums[item - 1] = -nums[item - 1]
            else:
                return item

if __name__ == "__main__":
    obj = Solution()
    arr = list(map(int, input().split()))
    print(obj.findDuplicate(arr))