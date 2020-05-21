class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num).replace("0b", "")
        new_b = ""
        for i in b:
            if i == "1":
                new_b += "0"
            else:
                new_b += "1"
        return int(new_b, 2)
