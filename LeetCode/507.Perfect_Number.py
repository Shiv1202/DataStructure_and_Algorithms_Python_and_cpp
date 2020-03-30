import math
# Solution Class.
class Solution:
    def checkPerfectNumber(self, num):
        def divisors(n):
            div = []
            for i in range(1, int(math.sqrt(n) + 1)):
                if n % i == 0:
                    yield i
                    if i * i != n:
                        div.append(int(n / i))
            for d in reversed(div):
                yield d
        if num <= 0: return False
        return sum(list(divisors(num))[:-1]) == num
                        
# Main Function.
def main():
    n = 28
    obj = Solution()
    print(obj.checkPerfectNumber(n))

# Driver Code.
if __name__ == "__main__":
    main()

