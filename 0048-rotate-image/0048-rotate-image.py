class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col],matrix[col][row] = matrix[col][row] , matrix[row][col]
        
        
        length = len(matrix[0])
        for row in range(len(matrix)):
            for col in range(len(matrix[row])//2):
                swap = length - 1 -col
                matrix[row][col],matrix[row][swap] = matrix[row][swap] , matrix[row][col]
        return 