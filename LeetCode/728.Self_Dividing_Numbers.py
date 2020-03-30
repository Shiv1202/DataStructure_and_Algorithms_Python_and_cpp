# Solution Class.
class Solution:
    def selfDividingNumbers(self, left, right):
        output = []
        for i in range(left, right + 1):
            temp = i
            flag = True
            
            while temp > 0 and flag:
                digit = temp % 10
                if not digit or i % digit != 0:
                    flag = False
                temp = temp // 10
            if flag:
                output.append(i)
        return output

# Main Function.
def main():
    l = 1
    r = 22
    obj = Solution()
    print(obj.selfDividingNumbers(l, r))

# Driver Code.
if __name__ == "__main__":
    main()