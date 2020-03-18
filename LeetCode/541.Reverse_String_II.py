""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Given a string and an integer k, you need
to reverse the first k characters for
every 2k characters counting from the
start of the string. If there are less
than k characters left, reverse all of
them. If there are less than 2k but
greater than or equal to k characters,
then reverse the first k characters and
left the other as original.
1) The string consists of lower English
letters only.
2) Length of the given string and k will
in the range [1, 10000]
-------------> Example <---------------
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"""

# Solution Class.
class Solution:
    def reverseStr(self, s, k):
        L = len(s)
        if L<k: return s[::-1]
        if L>k and L<=k*2:
            return s[:k][::-1]+s[k:]
        ans = ''
        for i in range(0,L,2*k):
            ans+=(s[i:i+k][::-1]+s[i+k:i+2*k])
        return ans


# Main Function.
def main():
    a = 'abcdefg'
    k = 2
    s = Solution()
    res = s.reverseStr(a, k)
    print(res)

# Driver Code.
if __name__ == "__main__":
    main()