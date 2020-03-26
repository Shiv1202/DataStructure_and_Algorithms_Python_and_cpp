# Solution Class.
class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        for i, x, y in sorted(zip(indexes,sources,targets),reverse = True):
            if S[i:].startswith(x):
                S = S[:i] + y + S[i+len(x):]
        return S
# Main Function.
def main():
    S = "abcd"
    ix = [0, 2]
    sources = ['a', 'cd']
    targets = ['eee', 'ffff']
    obj = Solution()
    print(obj.findReplaceString(S, ix, sources, targets))
# Driver Code.
if __name__ == "__main__":
    main()