class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = len(strs[0])
        rows = len(strs)
        ans = 0
        for col in range(cols):
            minn = strs[0][col]
            for row in range(rows):
                if strs[row][col] < minn:
                    ans += 1
                    break
                minn = strs[row][col]
        return (ans)