class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        n = row -2
        m = col - 2
        ans = []
        for i in range(0 , row - 2):
            tempmax = []
            for j in range(0 , col -2):
                temp = []
                for rw in range(i , i + 3):
                    temp.append(max(grid[rw][j:j+3]))
                tempmax.append( max(temp))
            ans.append(tempmax)
        return (ans)
        