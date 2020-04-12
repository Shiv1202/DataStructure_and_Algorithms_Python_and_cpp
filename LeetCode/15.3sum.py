class Solution:
    def threeSum(self, nums):
        def twoSum(self, nums, target, start):
            d = {}
            res2 = []
            for i, num in enumerate(nums[start + 1:]):
                n = target - num
                if n not in d:
                    d[num] = i
                else:
                    res2.append([num, n])
            return res2
        res3 = []
        seen = {}
        for i, c in enumerate(nums):
            if c in seen:
                continue
            else:
                seen[c] = 1
            ab = twoSum(self, nums, -c, i)
            
            if ab:
                for item in ab:
                    item.append(c)
                    res3.append(tuple(sorted(item)))
        return list(dict.fromkeys(res3))

# Main Function.
def main():
    nums = [-1, 0, 1, 2, -1, -4]
    obj = Solution()
    print(obj.threeSum(nums))

# Driver Code.
if __name__ == "__main__":
    main()