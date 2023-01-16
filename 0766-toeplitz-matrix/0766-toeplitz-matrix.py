class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        col = len(matrix[0])
        row = len(matrix)
        d = {}
        for i in range(row):
            for j in range(col):
                check  = d.get(j-i , matrix[i][j])
                # print(i , j , check == matrix[i][j])
                if check != matrix[i][j]:
                    
                    return False
                d[j-i] = matrix[i][j]
        return True