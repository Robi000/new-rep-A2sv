class Solution:
    def arrparser (self , grid , row , col):
        arr = []
        check = []
        # print(grid[row])
        arr.append( grid[row][col:col+3])
        check.extend(grid[row][col:col+3])
        arr.append( grid[row+1][col:col+3])
        check.extend(grid[row+1][col:col+3])
        arr.append( grid[row+2][col:col+3])
        check.extend(grid[row+2][col:col+3])
        check.sort()
        arrc = list(range(1 , 10))

        return [arr , check == arrc]

    def checkx(self ,grid):
        row = 0
        col = 0
        check = []
        print(grid)
        check.append(sum(grid[row][col:col+3]))
        check.append(sum(grid[row+1][col:col+3]))
        check.append(sum(grid[row+2][col:col+3]))
        dsum1 = grid[row][col] + grid[row +1][col+1] + grid[row+2][col +2]
        dsum2 = grid[row][col+2] + grid[row +1][col+1] + grid[row+2][col]
        csum1 = grid[row][col] + grid[row+1][col] + grid[row+2][col]
        csum2 = grid[row][col +1] + grid[row+1][col +1] + grid[row+2][col +1]
        csum3 = grid[row][col +2 ] + grid[row+1][col +2 ] + grid[row+2][col +2]
        check.extend([dsum1 , dsum2 , csum1 , csum2 ,csum3])
        if len(set(check)) == 1:
            return 1
        else:
            return 0


    def numMagicSquaresInside(self ,grid):
        row = len(grid)
        col = len(grid[0])
        arrc = list(range(1 , 10))
        ans = 0
        for r in range(row -2):
            for c in range(col - 2):
                print(r , c)
                arr , check = self.arrparser(grid , r , c)
                if check:
                    ans += self.checkx(arr)

        return(ans)