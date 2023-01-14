class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dic={}
        dic[0]=len(matrix[0])
        dic[1]=len(matrix) -1
        dic[2] = dic[0]-1
        dic[3] = dic[1] -1

        # print(dic)
        ans = []
        size = dic[0] * (dic[1]+1)
        indi , indj = 0 ,0
        while len(ans) < size:
            for k in range(dic[0]):
                if len(ans) == size:
                    break
                ans.append(matrix[indi][indj])
                if k != dic[0]-1:
                    indj += 1
                else:
                    dic[0] -= 2
                    indi += 1
            for k in range(dic[1]):
                if len(ans) == size:
                    break
                ans.append(matrix[indi][indj])
                if k != dic[1]-1:
                    indi += 1
                else:
                    dic[1] -= 2
                    indj -= 1
            for k in range(dic[2]):
                if len(ans) == size:
                    break
                ans.append(matrix[indi][indj])
                if k != dic[2]-1:
                    indj -= 1
                else:
                    dic[2] -= 2
                    indi -= 1
            for k in range(dic[3]):
                if len(ans) == size:
                    break
                ans.append(matrix[indi][indj])
                if k != dic[3]-1:
                    indi -= 1
                else:
                    dic[3] -= 2
                    indj += 1

        return (ans)
