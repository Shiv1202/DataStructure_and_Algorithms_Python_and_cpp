class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def editDistance(str1, str2, m, n):
            c = [[0 for _ in range(n + 1)] for x in range(m + 1)]
            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0:
                        c[i][j] = j
                    elif j == 0:
                        c[i][j] = i
                    
                    elif str1[i - 1] == str2[j - 1]:
                        c[i][j] = c[i - 1][j - 1]
                    
                    else:
                        c[i][j] = 1 + min(c[i][j - 1],
                                         c[i - 1][j],
                                         c[i - 1][j - 1]
                                         )
            return c[m][n]
        return editDistance(word1, word2, len(word1), len(word2))
