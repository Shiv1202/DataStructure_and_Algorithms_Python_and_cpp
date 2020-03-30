# Solution Class
class Solution:
    def oddCells(self, n, m, indices):
        row = [0] * n
        col = [0] * m
        ans = 0
        for i, j in indices:
            row[i] += 1
            col[j] += 1
        for r in row:
            for c in col:
                if (r + c) & 1:
                    ans += 1
        return ans

# Main Function.
def main():
    n = 2
    m = 3
    ix = [[0, 1], [1, 1]]
    obj = Solution()
    print(obj.oddCells(n, m, ix))

# Driver Code.
if __name__ == "__main__":
    main()