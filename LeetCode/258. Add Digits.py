class Solution:
    def addDigits(self, num: int) -> int:
    
        if num == 0:
            return 0
            
        # Check if no. is perfectly devisible by 9 then return 9 or return remender
        return num % 9 or 9
