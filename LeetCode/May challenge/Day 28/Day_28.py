class Solution:
    def countBits(self, num: int) -> List[int]:
        i, b = 0, 1
        bits = [0] * (num + 1)
        while b <= num:
            while i < b and i + b <= num:
                bits[i + b] = bits[i] + 1
                i += 1
            i = 0; b = b * 2
        return bits
