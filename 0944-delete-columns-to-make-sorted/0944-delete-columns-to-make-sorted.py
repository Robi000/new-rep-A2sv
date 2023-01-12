class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = len(strs[0])
        rows = len(strs)
        minn = 0
        ans = 0
        for col in range(cols):
            minn = 0
            for row in range(rows):
                _ASCII = ord(strs[row][col])
                if _ASCII < minn:
                    ans += 1
                    break
                minn = _ASCII
        return (ans)