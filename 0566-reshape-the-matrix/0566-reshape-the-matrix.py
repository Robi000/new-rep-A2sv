class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(mat)
        col = len(mat[0])
        if row * col != r*c :
            return mat
        new = [[] for x in range(r)]
        newr = 0
        newc = 0
        for i in range(row):
            for j in range(col):
                new[newr].append(mat[i][j])
                newc += 1
                if newc == c:
                    newr += 1
                    newc = 0
        return new