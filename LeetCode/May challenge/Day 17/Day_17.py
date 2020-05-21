from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p) or not(set(s) >= set(p)):
            return []
        
        p_size = len(p)
        counter_p = Counter(p)
        i_counter = Counter(s[:p_size])
        
        ans = []
        if counter_p == i_counter:
            ans.append(0)
        for i, (out, add) in enumerate(zip(s, s[p_size:])):
            i_counter[out] -= 1
            i_counter[add] += 1
            
            if counter_p == +i_counter:
                ans.append(i + 1)
                
        return ans
