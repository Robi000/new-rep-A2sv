class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = {}
        for match in matches:
            change  = dic.get(match[0] , [0 , 0])
            change[0] += 1
            dic[match[0]] = change
            change = []
            change  = dic.get(match[1] , [0 , 0])
            change[1] += 1
            dic[match[1]] = change
        All = []
        once = []
        
        
        for key in dic.keys():
            if dic[key][1] == 0:
                All.append(key)
            if dic[key][1] == 1:
                once.append(key)
        All.sort()
        once.sort()
        return  [All , once]
            
        