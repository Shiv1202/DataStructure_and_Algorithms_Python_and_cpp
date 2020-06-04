class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j] :
                i += 1
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
