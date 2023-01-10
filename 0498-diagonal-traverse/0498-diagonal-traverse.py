class Solution:
    
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        m , n = len(mat) , len(mat[0])
        for i in range(m):
            self.diagonal(i , 0 , mat , ans)
        for i in range(1 , n):
            self.diagonal(m-1 , i , mat , ans)

        return (ans)
    def diagonal(self ,row , col , mat , ans):
        # print (row , col)
        check = row + col
        temp = []
        m , n = len(mat) , len(mat[0])
        while row >=0 and col < n:
            temp.append(mat[row][col])
            row -= 1 
            col += 1
        if check % 2 == 0:
            ans.extend(temp)
        else:
            temp.reverse()
            ans.extend(temp)

        
        