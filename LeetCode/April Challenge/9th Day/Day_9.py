from itertools import zip_longest
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def check(s):
            skip = 0
            for x in reversed(s):
                if x == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
        return all(x == y for x, y in zip_longest(check(S), check(T)))
        
