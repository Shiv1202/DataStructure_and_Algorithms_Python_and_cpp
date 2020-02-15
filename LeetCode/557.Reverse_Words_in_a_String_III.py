""" -----------> Question <----------------
*** 557. Reverse Words in a String III ***
Given a string, you need to reverse the
order of characters in each word within a
sentence while still preserving whitespace
and initial word order.

*-*-*-*-*-*-*-*- Example 1 *-*-*-*-*-*-*-*-*
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by
single space and there will not be any extra
space in the string.
----------------> END <-------------------"""

# Solution Class.
class Solution:
    def reverseWords(self, s):
        li = list(map(str, s.split()))
        for i in range(len(li)):
            li[i] = li[i][::-1]
        return " ".join(li)

# Main Function.
def main():
    s = "Let's take LeetCode contest"
    s1 = Solution()
    res = s1.reverseWords(s)
    print(res)

if __name__ == "__main__":
    main()