# Solution Class
class Solution:
    def rotatedDigits(self, N):
        count = 0
        for i in range(1, N + 1):
            i = str(i)
            if "3" in i or '4' in i or '7' in i:
                continue
            if '2' in i or '5' in i or '6' in i or '9' in i:
                count += 1
        return count
    
# Main Function.
def main():
    N = 10
    obj = Solution()
    print(obj.rotatedDigits(N))

# Driver Code.
if __name__ == "__main__":
    main()