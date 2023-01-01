class Solution:
    import math
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        for x in nums:
            dic[x] = dic.get(x , 0) + 1
        ans = 0
        for y in dic.keys():
            if dic[y] != 1:
                ans += math.comb(dic[y], 2)
        return ans 
            
               
        