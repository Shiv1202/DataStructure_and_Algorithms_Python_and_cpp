from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1) or not(set(s2) >= set(s1)):
            return []
        
        s1_size = len(s1)
        counter_s1 = Counter(s1)
        i_counter = Counter(s2[:s1_size])
        
        # ans = []
        if counter_s1 == i_counter:
            return True
        for i, (out, add) in enumerate(zip(s2, s2[s1_size:])):
            i_counter[out] -= 1
            i_counter[add] += 1
            
            if counter_s1 == +i_counter:
                return True
                break
                
        return False
