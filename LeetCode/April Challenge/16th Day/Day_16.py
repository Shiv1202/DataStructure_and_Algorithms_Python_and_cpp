class Solution:
    def checkValidString(self, s: str) -> bool:
        left_paren_index = []
        star_index = []
        for i, val in enumerate(s):
            if val == "(":
                left_paren_index.append(i)
            elif val == ")":
                if left_paren_index:
                    left_paren_index.pop()
                elif star_index:
                    star_index.pop()
                else:
                    return False
            else:
                star_index.append(i)
        while left_paren_index:
            if len(star_index) == 0 or star_index.pop() < left_paren_index.pop():
                return False
        return True
