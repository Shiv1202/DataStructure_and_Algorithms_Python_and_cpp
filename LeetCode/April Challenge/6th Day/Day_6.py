from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for i in strs:
            temp[str(sorted(i))].append(i)
        return list(temp.values())
