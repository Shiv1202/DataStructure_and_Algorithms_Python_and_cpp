class Solution:
    def isHappy(self, n: int) -> bool:
        notHappy  = set()
        n = str(n)
        while n != '1':
            notHappy.add(n)
            s = 0
            for d in n:
                s += int(d)*int(d)
            n = str(s)
            if n in notHappy:
                return False
        return True
            
