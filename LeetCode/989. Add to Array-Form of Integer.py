class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        x = ""
        for i in A:
            x += str(i)
        x = int(x) + K
        o = []
        for i in range(len(str(x))):
            x = str(x)
            o.append(x[i])
        return o
