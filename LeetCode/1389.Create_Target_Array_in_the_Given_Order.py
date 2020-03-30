"""
    Method 1
"""
# class Solution:
#     def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
#         target = []
#         for i in range(len(nums)):
#             if index[i] == i:
#                 target.append(nums[i])
#             else:
#                 target = target[:index[i]] + [nums[i]] + target[index[i]:]
#         return target

"""
    1389. Create Target Array in the Given Order
    Solution Class.
"""
class Solution:
    def createTargetArray(self, nums, index):
        target = []
        map_x = list(zip(index, nums))
        for i, v in map_x:
            target.insert(i, v)
        return target
# Main Function.
def main():
    index = [0,1,2,2,1]
    nums = [0,1,2,3,4]
    obj = Solution()
    print(obj.createTargetArray(nums, index))

# Driver Code.
if __name__ == "__main__":
    main()